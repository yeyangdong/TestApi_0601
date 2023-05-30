import logging
from handle_yaml import do_yaml


class HandleLog():
    def __init__(self):
        # 1，创建日志对象
        self.my_logger = logging.getLogger("我是日志记录器")

        # 2，设置日志等级；只能记录日志级别大于等于当前日志等级的日志
        # self.my_logger.setLevel("WARNING")
        self.my_logger.setLevel(do_yaml.get_data("log", "logger_level"))

        # 3。创建日志输出渠道（日志显示的地方）
        console_handler = logging.StreamHandler()  # 设置控制台输出
        file_handler = logging.FileHandler(do_yaml.get_data("log", "log_filename"), encoding="utf-8")  # 设置日志文件中输出

        # 4，创建日志的显示样式
        formater = logging.Formatter('%(asctime)s-[%(levelname)s]-[msg]:%(message)s - %(name)s - %(lineno)d')
        console_handler.setFormatter(formater)  # 设置控制台展示的日志样式
        file_handler.setFormatter(formater)  # 设置日志文件展示的日志样式

        # 5，日志器对象与日志输入渠道（展示的地方）进行关联
        self.my_logger.addHandler(console_handler)
        self.my_logger.addHandler(file_handler)

    def get_loger(self):
        return self.my_logger

do_log = HandleLog().get_loger()
if __name__ == '__main__':
    #  手动产生日志
    do_log = HandleLog()
    my_logger = do_log.get_loger()
    my_logger.debug("这是一条debug级别日志")
    my_logger.info("这是一条info级别日志")
    my_logger.warning("这是一条warning级别日志")
    my_logger.critical("这是一条critical级别日志")
    my_logger.error("这是一条error级别日志")
