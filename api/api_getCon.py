import requests
# 新建类 登录接口对象


class ApiaddCon(object):
    # 新建方法 登录方法
    def api_get_config(self,url):
        # headers
        headers= {"Content-Type":"application/json"}
        # 调用post并返回响应对象
        return requests.get(url, headers=headers)