import requests


class HandleRequest:

    def __init__(self):
        self.session = requests.Session()

    def add_headers(self, one_dict):
        self.session.headers.update(one_dict)

    def send(self, method, url, **kwargs):
        one_method = method.upper()
        res = self.session.request(one_method, url, **kwargs)
        return res

    def close(self):
        self.session.close()


if __name__ == '__main__':
    do_request = HandleRequest()
    login_url = "http://api.lemonban.com:8788/futureloan/member/login"
    headers_dict = {
        "X-Lemonban-Media-Type": "lemonban.v2",
        "User-Agent": "Mozilla/5.0 LookSky",
        "Content-Type": "application/json"
    }
    do_request.add_headers(headers_dict)

    login_params = {
        "mobile_phone": "15158787682",
        "pwd": "12345678"
    }
    # 1.登陆
    login_res = do_request.send(method='post', url=login_url, json=login_params)
    response_data_dict = login_res.json()
    token = response_data_dict["data"]["token_info"]["token"]
    user_id = response_data_dict["data"]["id"]


    # 将token添加到请求头中
    token_dict = {
        "Authorization": f"Bearer {token}"
    }
    do_request.add_headers(token_dict)

    # 2.充值
    recharge_url = "http://api.lemonban.com:8788/futureloan/member/recharge"

    recharge_params = {
        "amount": "10000",
        "member_id": user_id
    }
    recharge_res = do_request.send(method='post', url=recharge_url, json=recharge_params)

    # 3.获取用户信息
    user_url = f"http://api.lemonban.com:8788/futureloan/member/{user_id}/info"
    member_res = do_request.send(method="get", url=user_url)
