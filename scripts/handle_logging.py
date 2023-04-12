import logging
from scripts.handle_path import LOGS_PATH
import os

# 1.创建logger对象,相当于日志记录工具
my_logger = logging.getLogger('log_file')


# 2.设置日志等级
my_logger.setLevel(
    'DEBUG'
)
log_save = 'loging.log'
log_save = os.path.join(LOGS_PATH,log_save)

# 3.创建日志输出渠道,把日志输出到控制台/文件中
console_handle = logging.StreamHandler()
file_handle = logging.FileHandler(log_save,encoding='utf-8')
# 3.1单独设置控制台的日志展示WARING级别以上,比较上面的DEBUG,控制台中WARING是单独的,不受影响,而file_handle是仍为DEBUG优先展示
console_handle.setLevel('WARNING')


# 4.创建日志的显示格式,样式
formater = logging.Formatter('%(asctime)s-[%(levelname)s]-[msg]:%(message)s - %(name)s - %(lineno)d')
# 4.1 让日志输出的渠道和日志的样式相关联
console_handle.setFormatter(formater)
file_handle.setFormatter(formater)


# 5.让日志器对象和日志输出渠道相关联
my_logger.addHandler(file_handle)
my_logger.addHandler(console_handle)


if __name__ == '__main__':
    my_logger.debug('这是一条debug日志')
    my_logger.info('这是一条info日志')
    my_logger.error('这是一条error日志')
    my_logger.warning('这是一条warning日志')
    my_logger.critical('这是一条critical日志')
