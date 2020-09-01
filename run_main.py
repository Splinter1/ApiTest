import unittest
from tools.handle_excel import HandExcel
from api.api_base import ApiPost

class RunMain:
    def run_case(self):
        rows = HandExcel.get_rows()
        for i in rows:
            data = HandExcel.get_rows_value(i+2)
            is_run = data[2]
            if is_run == 'YES':
                method = data[3]
                url = data[2]
                handlers = data[4]
                body = data[5]
                ApiPost.api_post()


