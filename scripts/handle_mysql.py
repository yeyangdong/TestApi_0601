import random
import pymysql
from handle_yaml import HandleYaml

do_yaml = HandleYaml()


class handle_mysql():
    def __init__(self):
        # 1.链接库
        self.connect = pymysql.connect(
            host="api.lemonban.com",
            user="future",
            password='123456',
            port=3306,
            database="futureloan",
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor  # DictCursor的意义是将结果，以字典类型返回
        )
        # 2.创建游标
        self.cursor = self.connect.cursor()

    def get_one_value(self, sql, args=None):
        self.cursor.execute(sql, args=args)  # 使用该游标对象的execute()方法向MySQL发送SQL命令，MySQL服务器接收后解析SQL语句才能返回结果
        self.connect.commit()
        return self.cursor.fetchone()

    def get_values(self, sql, args=None):
        self.cursor.execute(sql, args=args)
        self.connect.commit()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connect.close()

    @staticmethod
    def creat_mobile():
        # 随机生成11位的手机号
        start_mobile = ['138', '139', '188']
        start_mobile = random.choice(start_mobile)
        end_num = ''.join(random.sample('0123456789', 8))
        return start_mobile+end_num

    def is_existed_mobile(self, mobile):
        '''
        判断手机号在数据库中是否存在
        :param mobile:
        :return:
        '''
        # sql = "select mobile_phone from member where mobile_phone = %s"
        sql = do_yaml.get_data("mysql", "select_user_sql")
        if self.get_values(sql, args=[mobile]):  # 手机号存在返回True,否则返回False
            return True
        else:
            return False

    def creat_not_existed_mobile(self):
        '''
        随机生成一个数据库中不存在的手机号
        :return:
        '''
        while True:
            one_mobile = self.creat_mobile()
            if not self.is_existed_mobile(one_mobile):
                break

        return one_mobile


if __name__ == '__main__':
    do_mysql = handle_mysql()
    do_mysql.creat_not_existed_mobile()
    pass
'''
# 3.通过游标去执行sql语句
one_mobile = input('请输入手机号:')
sql = f'select * from member where mobile_phone = %s'
one_cursor.execute(sql, args=[one_mobile])
# '18659384516'


# 4.获取sql值,并提交
# result = one_cursor.fetchone()  # 获取一条数据
result2 = one_cursor.fetchall()  # 获取多条数据
connect.commit()  # 提交数据,如果是插入或者修改数据,一定要commit,查询的话可以不用

# 5.关闭链接,先关闭游标,再关闭链接
one_cursor.close()
connect.close()
'''
