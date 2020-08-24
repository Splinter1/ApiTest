"""
    目标实现接口对象封装
"""
# 导包 requsts
# 新建类 登录接口对象
# 新建方法 登录方法

import requests
# 新建类 登录接口对象
class ApiaddCon(object):
    # 新建方法 登录方法
    def api_post_add(self,url, name, value):
        # headers
        headers= {"Content-Type":"application/json"}
        # data
        data={"app_key":"6A3D030D071263AEDC8F8E115C30CA3E","config_name":name,"config_value":value}

        return requests.post(url, headers=headers , json=data)