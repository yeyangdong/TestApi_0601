from scripts.handle_request import HandleRequest
from scripts.handle_mysql import handle_mysql
from scripts.handle_yaml import handleYaml
from scripts.handle_parameterize import GlobalData


def creat_user(reg_name, password=123456789, type=1):
    do_mysql = handle_mysql()
    do_request = HandleRequest()
    do_yaml = handleYaml()
    mobile_phone = do_mysql.creat_not_existed_mobile()

    param = {
        "mobile_phone": mobile_phone,
        "pwd": password,
        "reg_name": reg_name,
        "type": type
    }
    url = "http://api.lemonban.com/futureloan/member/register"
    do_request.add_headers(do_yaml.get_data("api", "api_version"))
    res = do_request.send("POST", url, json=param)

    user_id = res.json()["data"]["id"]
    do_request.close()
    do_mysql.close()

    # setattr(GlobalData, f"{reg_name}_user_tel", mobile_phone)
    # setattr(GlobalData, f"{reg_name}_user_pwd", password)
    # setattr(GlobalData, f"{reg_name}_user_id", user_id)

    setattr(GlobalData, "${" + reg_name + "_user_tel}", mobile_phone)
    setattr(GlobalData, "${" + reg_name + "_user_pwd}", password)
    setattr(GlobalData, "${" + reg_name + "_user_tel}", user_id)



def generate_three_user():
    creat_user("admin1")
    creat_user("admin2")
    creat_user("admin3")
    pass


if __name__ == '__main__':
    generate_three_user()
