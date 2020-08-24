"""
    完成登录业务层实现
"""

# 导包 unittest Api_addCon
import unittest
from api.api_addCon import ApiaddCon
# 新建测试类


class TestaddCon(unittest.TestCase):
    # 新建测试方法
    def test_addCon(self):
        # 暂时存放数据 url name value
        url = "http://hn216.api.yesapi.cn/?&s=App.Config.AddConfig"
        name = "testAPi2"
        value = "2"
        # 调用登录方法
        s = ApiaddCon().api_post_add(url,name,value)
        print("查看打印接口",s.json())
        # 断言响应信息 及 状态码
        self.assertEqual("V", s.json()['msg'])
        # 断言响应状态吗
        self.assertEqual(200, s.status_code)


if __name__ == 'main':
    unittest.main()
