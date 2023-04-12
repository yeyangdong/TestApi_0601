import os

# one_path = os.path.abspath(__file__)
# two_path = os.path.dirname(one_path)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录

CASE_PATH = os.path.join(BASE_DIR, "cases")
CONFS_PATH = os.path.join(BASE_DIR, "confs")
DATA_PATH = os.path.join(BASE_DIR, "data")
LIBS_PATH = os.path.join(BASE_DIR, "libs")
LOGS_PATH = os.path.join(BASE_DIR, "logs")
REPORTS_PATH = os.path.join(BASE_DIR, "reports")
SCRIPTS_PATH = os.path.join(BASE_DIR, "scripts")
pass