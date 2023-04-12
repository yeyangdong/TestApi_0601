import unittest
from libs.HTMLTestRunnerNew import HTMLTestRunner
from scripts.handle_yaml import handleYaml
from scripts.handle_path import CASE_PATH, REPORTS_PATH
from scripts.handle_user import generate_three_user
generate_three_user()


# 使用unittest.defaultTestLoader.discover方法,会返回套套件对象
# a.第一个参数为发现用例的路径,带引号
# b.第二个参数为用例模块的匹配方式(默认会自动找文件名为'test*.py'的文件,也可以自定义,例如'yyd*.py')
# c.用例的自动发现机制,查找test_的文件去执行,生成报告
suite = unittest.defaultTestLoader.discover(CASE_PATH, 'test_*.py')
do_yaml = handleYaml()

html_filename = do_yaml.get_data('reports', 'html_file')
# html_filename = os.path.join(REPORTS_PATH,html_filename)
pass
# 3.执行用例
# 创建TextTestRunner运行器
with open(html_filename, 'wb') as file:
    runner = HTMLTestRunner(file,
                            verbosity=1,
                            title='叶洋东的第一份测试报告',
                            description='牛逼666',
                            tester='叶洋东')
    runner.run(suite)

# 控制台中结果,
# .代表用例执行成功
# f代表用例执行失败
