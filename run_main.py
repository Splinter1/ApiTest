import json
import unittest
from tools.handle_excel import HandExcel
from api.api_base import BaseRequest



class RunMain:
    def run_case(self):
        rows = HandExcel().get_rows()
        for i in range(rows):
            data = HandExcel().get_rows_value(i+2)
            is_run = data[0]
            if is_run == 'YES':
                method = data[3]
                url = data[2]
                headers = data[4]
                headers_json = json.loads(headers)
                body = data[5]
                body_json = json.loads(body)
                BaseRequest().base_request(method, url, headers_json, body_json)
            else:
                pass


if __name__ == '__main__':
    RunMain().run_case()


