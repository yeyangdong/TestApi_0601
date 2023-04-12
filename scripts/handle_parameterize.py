import re


class GlobalData:
    pass


class Parameterize:
    @staticmethod
    def to_parma(src):
        result = re.findall(r"\${.*?}", src)  # 返回正则获取的list
        for item in result:
            data = getattr(GlobalData, item)
            src = src.replace(item, str(data))

        return src


if __name__ == '__main__':
    one_str = '{"mobile_phone":"${not_existed_tel}","pwd":"12345678","uid":"${user_id},"type":1, "reg_name": "keyou"}'
    setattr(GlobalData, "${not_existed_tel}", "18911112222")
    setattr(GlobalData, "${user_id}", "3333")
    Parameterize.to_parma(one_str)