# 封装yaml

import yaml
import os
from scripts.handle_path import CONFS_PATH

class handleYaml():
    testcase = 'testcase.yaml'
    testcase = os.path.join(CONFS_PATH,testcase)
    def __init__(self, filename=None):
        if filename is None:
            self.filename = handleYaml.testcase
        else:
            self.filename = filename
        with open(self.filename, encoding="utf-8") as file:
            self.config_data = yaml.full_load(file)  # yaml.full_load(file)返回的是file文件的所有信息
            pass
    def get_data(self, section, option=None):
        '''
        读取yaml配置文件数据
        :param section: 区域名
        :param option: 选项名
        :return: 返回选项名对应的值
        '''
        return self.config_data[section][option]


if __name__ == '__main__':
    do_yaml = handleYaml()
    print(do_yaml.get_data('excel', 'filename'))


