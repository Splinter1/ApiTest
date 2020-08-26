"""
    完成登录业务层实现
"""

# 导包 unittest Api_addCon
import unittest
from api.api_addCon import ApiaddCon
from parameterized import parameterized
from tools.read_json import ReadJson

# 读取数据函数
def get_data():
    datas = ReadJson().read_json("addCon_more.json")
    # 新建空列表，添加读取json数据
    arrs = []
    # 使用遍历
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("name"),
                     data.get("value"),
                     data.get("expect_result"),
                     data.get("status_code")))
    return arrs


class TestaddCon(unittest.TestCase):
    # 新建测试方法
    @parameterized.expand(get_data())
    def test_addCon(self,url,name,value,expect_result,status_code):
        # 暂时存放数据 url name value
        # url = "http://hn216.api.yesapi.cn/?&s=App.Config.AddConfig"
        # name = "testAPi2"
        # value = "2"
        # 调用登录方法
        s = ApiaddCon().api_post_add(url,name,value)
        print("查看打印接口",s.json())
        # 断言响应信息 及 状态码
        self.assertEqual(expect_result, s.json()['msg'])
        # 断言响应状态吗
        self.assertEqual(status_code, s.status_code)


if __name__ == '__main__':
    unittest.main()