import unittest

from libs.HTMLTestRunner import HTMLTestRunner
from scripts.handle_yaml import do_yaml
from scripts.handle_log import do_log



suite = unittest.defaultTestLoader.discover(".")   #获取当前路径下的用例，以test_开头的：源码    def discover(self, start_dir, pattern='test*.py', top_level_dir=None):


# 2.执行用例
# 创建TextTestRunner()运行器
# runner = unittest.TextTestRunner()


html_name = do_yaml.get_data("reports", "filename")
with open(html_name, "wb") as file:
    runner = HTMLTestRunner(file,
                   verbosity=do_yaml.get_data("reports", "verbosity"),
                   title=do_yaml.get_data("reports", "title"),
                   description=do_yaml.get_data("reports", "description"),
                   tester=do_yaml.get_data("reports", "tester")
                            )
    # 3.运行套件里面的用例
    runner.run(suite)

