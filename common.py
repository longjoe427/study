import json

import requests
import time
import yaml


# 需要把headers保存下来，避免每次都去登录，容易出错
class Public(object):

    def __init__(self, phone):
        self.phone = phone
        self.headers = None

    def send_code(self):
        url = 'http://capi.t.carsdaq.com/api/auth/send_code'
        payload = {
            "phone": self.phone
        }
        # global r
        r = requests.post(url, data=payload)
        print(r.text)
        if r.json()['code'] == 200:
            global code
            code = r.json()['data']['code']
            # return code
        else:
            r = requests.post(url, data=payload)

    def login(self):
        url = 'http://capi.t.carsdaq.com/api/auth/login'
        payload = {
            "phone": self.phone,
            "code": code
        }
        r = requests.post(url, data=payload)
        headers = {
            "carsdaq-app": "ios",
            "carsdaq-version": "1.8.2",
            "carsdaq-timestamp": "",
            "carsdaq-app-frame": "vue2x",
            "carsdaq-app-env": "test",
            "Authorization": "",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "carsdaq-signature": "",
            "carsdaq-driver-token": "64bb63bf6d1d552e3ec1164f4e12df66832ee2ec9bc536fa624288f7dd6a5e3a",
            "carsdaq-H5-env": "production",
            "host": 'http://cweb-t.carsdaq.com',

        }
        # global Authorization
        global Authorization
        Authorization = r.json()['data']['token_type'] + ' ' + r.json()['data']['access_token']
        headers['Authorization'] = Authorization
        # self.headers.update(headers)
        headers_yaml = yaml.dump(headers)
        # print(headers)
        # print(type(headers))
        self.headers = headers_yaml
        # return headers
        # 存到yaml文件
        filename = 'headers.yaml'
        with open(filename, 'w') as f:
            f.write(self.headers)


def get_headers():
    with open('headers.yaml', 'r') as f:
        headers = yaml.load(f, Loader=yaml.Loader)
        if headers != None:
            # print(headers)
            return headers
        else:
            p = Public(18000000066)
            p.send_code()
            p.login()
            headers = yaml.load(f, Loader=yaml.Loader)
            return headers



def be_json(data_name):
    data_name = json.dumps(data_name, ensure_ascii=False)
    print(data_name)
    return data_name


def get_current_time():
    now = time.time()
    # print(now)
    # # 时间戳转为时区时间
    struct_time_now = time.gmtime(now)
    # print(struct_time_now)
    current_time = time.strftime("%Y-%m-%d", struct_time_now)
    return current_time


if __name__ == "__main__":
    p = Public(18000000066)
    p.send_code()
    p.login()
    # get_current_time()
    print(get_headers())
    # print(type(get_headers()))