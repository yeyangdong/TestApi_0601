# 讲在Unittest中,调用读取Excel的数据,去发起接口请求
# 讲了ddt数据驱动
import ddt
import unittest
from scripts.handle_request import HandleRequest
from scripts.handle_excel import HandleExcel
from scripts.handle_yaml import handleYaml
from scripts.handle_mysql import handle_mysql
from scripts.handle_parameterize import GlobalData, Parameterize


do_yaml = handleYaml()
do_excel = HandleExcel(do_yaml.get_data('excel', 'filename'), 'register1')
testcase_data = do_excel.read_data()  # 返回sheet页的数据
# 1.要继承父类
# 使用ddt的时候在类前面加@ddt.ddt作为类的装饰器
@ddt.ddt()
class Register(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.do_request = HandleRequest()
        cls.do_mysql = handle_mysql()
        headers_dict = {
            "X-Lemonban-Media-Type": "lemonban.v2",
            "User-Agent": "Mozilla/5.0",
        }
        cls.do_request.add_headers(headers_dict)

    @classmethod
    def tearDownClass(cls):
        print('teardown_class')
        cls.do_request.close()
        cls.do_mysql.close()

    # 使用ddt.data函数来装饰用例的实例方法
    # 第一个参数将序列类型(字典列表元祖)拆包
    # 用例所在的序列类型
    # ddt模块,会自动且动态创建多个实例方法,实例方法名为test_register_用例的数量,从1开始
     # 每次循环会将data中的位置参数一次传给实例方法,由testcase_dict接收
    @ddt.data(*testcase_data)
    def test_register(self, testcase_dict):
        setattr(GlobalData, "${not_existed_tel}", self.do_mysql.creat_not_existed_mobile())
        new_data = Parameterize.to_parma(testcase_dict.data)
        res = Register.do_request.send(testcase_dict['method'],
                                       url=testcase_dict['url'],
                                       json=testcase_dict['data'])

        real_code = res.json()['code']  # 实际结果
        # 被try捕获的异常,执行case时是直接通过,不会报错的
        row = testcase_dict['id']+1
        do_excel.write_data(row, 7, res.text)
        try:
            self.assertEqual(testcase_dict['expected_value'], real_code, testcase_dict['name'])
        except AssertionError as e:
            do_excel.write_data(row, 8, '失败')
            raise e
        else:
            do_excel.write_data(row, 8, '成功')



if __name__ == '__main__':
    unittest.main()
