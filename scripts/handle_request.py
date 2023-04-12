# 通过session会话去调用,推荐使用这种

import requests


class HandleRequest:
    def __init__(self):
        self.session = requests.Session()

    def send(self, method, url, **kwargs):
        one_method = method.upper()
        res = self.session.request(one_method, url, **kwargs)
        return res

    def add_headers(self, one_dict):
        self.session.headers.update(one_dict)

    def close(self):
        self.session.close()


if __name__ == '__main__':
    do_request = HandleRequest()

    # 1.登陆
    login_url = "http://api.lemonban.com/futureloan/member/login"

    headers_dict = {
        "X-Lemonban-Media-Type": "lemonban.v2",
        "User-Agent": "Mozilla/5.0"
    }

    # 添加上方的headers_dict到do_request这个会话对象里面,之后调用就自带请求头了
    do_request.add_headers(headers_dict)

    login_param = {
        "mobile_phone": "15158787622",
        "pwd": "12345678"
    }


    res = do_request.send('POST', url=login_url, json=login_param)
    pass

    # # 将res获取json转化为字典之后的响应数据
    # response_data_dict = res.json()
    #
    #
    # # 获取token(根据接口文档的参数层级来获取)
    # token = response_data_dict["data"]["token_info"]["token"]
    # user_id = response_data_dict["data"]["id"]
    #
    #
    # # 把token加入请求头中
    # token_dict = {
    #     "Authorization": f"Bearer {token}"
    # }
    # do_request.add_headers(token_dict)
    #
    #
    #
    #
    #
    #
    # # 2.调用充值接口
    # recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
    #
    #
    # recharge_param = {
    #     "member_id": user_id,
    #     "amount": 100
    # }
    # recharge_res = do_request.send('POST', url=recharge_url, json=recharge_param)
    #
    #
    #
    #
    #
    #
    #
    # # 获取用户信息
    # user_url = f'http://api.lemonban.com/futureloan/member/{user_id}/info'
    #
    # user_url_res = do_request.send('GET', url=user_url)
    # # Response对象中,可以通过headers属性获取响应头信息,通过key获取值相当于一个字典
    # # Response对象中,可以通过request.headers属性获取请求头信息,相当于一个字典
    # # do_request.close()
