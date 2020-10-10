import json
import unittest
from tools.handle_excel import HandExcel
from api.api_base import BaseRequest
from tools.handle_result import handle_result,handle_result_json
from tools.read_json import ReadJson
from tools.codition_get import get_data


class RunMain:
    def run_case(self):
        rows = HandExcel().get_rows()
        for i in range(rows-1):
            deepen_data = None
            data = HandExcel().get_rows_value(i+2)
            body = data[5]
            body_json = json.loads(body)
            # 根据名称查询列号，然后拿到数据
            is_run = data[HandExcel().get_cells_num("是否执行")]
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
                HandExcel().excel_write_data(i + 2, 12, json.dumps(res, ensure_ascii=False))
                print(res)
                code = ReadJson().key_tovalue(res, "err_code")
                msg = ReadJson().key_tovalue(res, "err_msg")
                # 验证方式的区分
                if excepect_method == 'message+errorcode':
                    config_msg = handle_result(url, code)
                    if msg == config_msg:
                        HandExcel().excel_write_data(i+2, 9, "成功")
                        print("成功了")
                    else:
                        HandExcel().excel_write_data(i+2, 10, json.dumps(res, ensure_ascii=False))
                        print("失败了")
                if excepect_method == 'errorcode':
                    excepect_code = data[7]
                    if code == excepect_code:
                        HandExcel().excel_write_data(i+2, 9, "成功")
                        print("成功了")
                    else:
                        HandExcel().excel_write_data(i+2, 10, json.dumps(res, ensure_ascii=False))
                        print("失败了")
                if excepect_method == 'json':
                    boo = handle_result_json(res, url, code)
                    if boo:
                        print("成功了")
                    else:
                        print("失败了")


if __name__ == '__main__':
    RunMain().run_case()


