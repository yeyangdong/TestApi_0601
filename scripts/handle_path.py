import os

# one_path = os.path.abspath(__file__)  #查询当前文件的路径：       '/Users/yeyangdong/Desktop/自己写的代码/PycharmProjects/TestApi_0601/scripts/handle_path.py'
#
# two_path = os.path.dirname(one_path)  #查询当前文件上级录路径：     '/Users/yeyangdong/Desktop/自己写的代码/PycharmProjects/TestApi_0601/scripts'
#
# BASE_DIR = os.path.dirname(two_path)  #查询查询当前文件上级录路径：   '/Users/yeyangdong/Desktop/自己写的代码/PycharmProjects/TestApi_0601'

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 简化

# 用例路径
CASE_PATH = os.path.join(BASE_DIR, 'cases')  # 拼接cases目录的路径

CONFS_PATH = os.path.join(BASE_DIR, 'confs')

DATA_PATH = os.path.join(BASE_DIR, 'data')

LOGS_PATH = os.path.join(BASE_DIR, 'logs')

REPORTS_PATH = os.path.join(BASE_DIR, 'reports')

SCRIPTS_PATH = os.path.join(BASE_DIR, 'scripts')


pass
