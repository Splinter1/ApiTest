
import unittest
from api.api_getCon import ApiaddCon


class TestgetCon(unittest.TestCase):
    # 新建测试方法
    def test_getCon(self):
        url = "http://hn216.api.yesapi.cn/?s=App.Config.GetConfig&config_name=test1&app_key=6A3D030D071263AEDC8F8E115C30CA3E&sign=4EE526BB3F702D0C7347460D2785C754"
        s = ApiaddCon().api_get_config(url)
        print("查看打印接口",s.json())

        self.assertEqual("V3.1.0 YesApi App.Config.GetConfig", s.json()['msg'])

        self.assertEqual(200, s.status_code)


if __name__ == '__main__':
    unittest.main()
