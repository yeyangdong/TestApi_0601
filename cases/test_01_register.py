# 0.导入unittest模块
import json
import unittest
import ddt
from handle_request import HandleRequest
from handle_excel import HandleExcel
from handle_yaml import HandleYaml
from handle_log import do_log


do_yaml = HandleYaml()


@ddt.ddt()  # 1.使用ddt.ddt作为类的装饰器
class TestRegister(unittest.TestCase):  # 需要继承unittest.TestCase父类
    do_excel = HandleExcel(do_yaml.get_data('excel', 'filename'), "register")
    testcase_data = do_excel.read_data()  # 嵌套字典列表

    @classmethod
    def setUpClass(cls):
        cls.do_request = HandleRequest()
        cls.do_request.add_headers(do_yaml.get_data("api", "api_version"))
        do_log.info("开始执行用例")

    @classmethod
    def tearDownClass(cls):
        cls.do_request.close()
        do_log.info("用例执行结束")

    """
    2.使用ddt.data函数来装饰用例的实例方法
    3.@ddt.data(*testcase_data)将用例参数拆包，传给testcase_dict
    @ddt.data（用例参数1，用例参数2。。）
    ddt模块会自动创建多个实例方法，实例方法名为test_register_用例的索引号
    每次循环会将data中的位置参数依次传给实例方法
    
    什么是数据驱动：
    1.往往一个接口有多条用例
    2.每一条用例执行书，仅仅只有测试数据（参数）不同，而用例的执行逻辑几乎一直
    3.为了较少代码量，使框架更为简洁，所以会让用例数据和用例执行逻辑进行分离，这种机制成为：数据驱动
    """

    @ddt.data(*testcase_data)
    def test_register(self, testcase_dict):
        # 使用for循环读取数据存在的问题：
        # 1.用例总数始终只统计为一条
        # 2.一旦for循环中一条用例执行失败（比如抛出异常）， 那么整个for循环就会停止执行
        # 3.基于第一条，失败的用例无法正确统计
        # for testcase_dict in testcase_data:
        #     res = self.do_request.send(method=testcase_dict["method"],
        #                                url=testcase_dict["url"],
        #                                json=testcase_dict["data"])
        #     expected_value = testcase_dict["expected"]
        #     actual = res.json()["code"]
        #     try:
        #         self.assertEqual(expected_value, actual, testcase_dict["name"])
        #     except AssertionError as e:
        #         print("此处需要日志记录")
        #         print(f"具体异常为：{e}")
        res = self.do_request.send(method=testcase_dict["method"],
                                   url=testcase_dict["url"],
                                   json=json.loads(testcase_dict["data"]))
        expected_value = testcase_dict["expected"]
        actual = res.json()["code"]
        row = testcase_dict["id"] + 1
        self.do_excel.write_data(row, 7, res.text)
        try:
            self.assertEqual(expected_value, actual, testcase_dict["name"])
        except AssertionError as e:
            do_log.error(f"用例执行失败,异常为{e}")
            self.do_excel.write_data(row, 8, "失败")
            raise e
        else:
            self.do_excel.write_data(row, 8, "成功")


if __name__ == '__main__':
    unittest.main()  # 这个也会执行该文件下的所有用例
