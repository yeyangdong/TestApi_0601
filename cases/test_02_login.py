# 0.导入unittest模块
import unittest
import json
import ddt
from handle_request import HandleRequest
from handle_excel import HandleExcel
from handle_yaml import HandleYaml
from handle_log import do_log

do_yaml = HandleYaml()

@ddt.ddt()  # 1.使用ddt.ddt作为类的装饰器
class TestRegister(unittest.TestCase):  # 需要继承unittest.TestCase父类
    do_excel = HandleExcel(do_yaml.get_data('excel', 'filename'), "login")
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

    @ddt.data(*testcase_data)
    def test_login_success(self, testcase_dict):
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
            do_log.error(f"用例执行失败，具体的异常为：{e}")
            self.do_excel.write_data(row, 8, "失败")
            raise e
        else:
            self.do_excel.write_data(row, 8, "成功")



if __name__ == '__main__':
    unittest.main()  # 这个也会执行该文件下的所有用例
