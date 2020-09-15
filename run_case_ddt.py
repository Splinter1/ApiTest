import ddt
import unittest
import json
import time
import os
from tools.handle_excel import HandExcel
from api.api_base import BaseRequest
from tools.handle_result import handle_result,handle_result_json
from tools.read_json import ReadJson
from tools.codition_get import get_data
from tools.HTMLTestRunnerNew import HTMLTestRunner
base_path = os.getcwd()
data = HandExcel().get_excel_data()

@ddt.ddt()
class TestRunCaseDdt(unittest.TestCase):

    @ddt.data(*data)
    def test_main_case(self, data):
        try:
            deepen_data = None
            i = HandExcel().get_rows_num(data[1])
            body = data[5]
            body_json = json.loads(body)
            is_run = data[0]
            if is_run == 'YES':
                is_depend = data[10]
                # 前置处理
                if is_depend is None:
                    pass
                else:
                    deepen_key = data[12]
                    deepen_data = get_data(is_depend)
                    body_json[deepen_key] = deepen_data
                excepect_method = data[6]  # 预期结果获取方式
                method = data[3]
                url = data[2]
                headers = data[4]
                headers_json = json.loads(headers)
                res = BaseRequest().base_request(method, url, headers_json, body_json)
                # 讲结果写入excel
                HandExcel().excel_write_data(i, 12, json.dumps(res, ensure_ascii=False))
                print(res)
                code = ReadJson().key_tovalue(res, "err_code")
                msg = ReadJson().key_tovalue(res, "err_msg")
                # 验证方式的区分

                if excepect_method == 'message+errorcode':
                    config_msg = handle_result(url, code)
                    try:
                        self.assertEqual(msg, config_msg)
                        HandExcel().excel_write_data(i, 9, "成功")
                        print("成功了")
                    except Exception:
                        HandExcel().excel_write_data(i, 10, json.dumps(res, ensure_ascii=False))
                        print("失败了")
                        raise Exception

                if excepect_method == 'errorcode':
                    excepect_code = data[7]
                    try:
                        self.assertEqual(msg, excepect_code)
                        HandExcel().excel_write_data(i, 9, "成功")
                        print("成功了")
                    except Exception:
                        HandExcel().excel_write_data(i, 10, json.dumps(res, ensure_ascii=False))
                        print("失败了")
                        raise Exception

                if excepect_method == 'json':
                    boo = handle_result_json(res, url, code)
                    if boo:
                        print("成功了")
                    else:
                        print("失败了")
        except Exception:
            HandExcel().excel_write_data(i, 9, "失败")
            raise Exception


if __name__ == '__main__':
    # 组装测试套件
    suite = unittest.defaultTestLoader.discover(base_path, pattern="run_case_*.py")

    # 指定报告存放路径，及文件名称
    file_path = "./report/{}.html".format(time.strftime("%Y_%m_%d_%H_%M_%S"))

    # 运行测试套件并生成报告
    with open(file_path, "wb") as f:
        HTMLTestRunner(stream=f, verbosity=2, title='测试报告名称', description='这里是描述', tester='测试者').run(suite)
