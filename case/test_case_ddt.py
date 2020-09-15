import ddt
import unittest
from tools.handle_excel import HandExcel
data = HandExcel().get_excel_data()


@ddt.ddt
class TestCase01(unittest.TestCase):
    @ddt.data(*data)
    def test_01(self,data):
        # 是否执行  用例名称  URL  请求方法  headers  Body  检验方式  预期结果  result  失败数据  前置条件  返回数据  依赖Key
        is_run, case_name, url, method, headers, body, execpet_method, execpet, result, result_data, condition, request_key, depend_key = data
        print(is_run, case_name)


if __name__ == '__main__':
    unittest.main()