import unittest
from tools.read_db import ReadDB

class TestDB(unittest.TestCase):
    def test_db(self):
        sql = "SELECT name,is_deleted FROM `tb_device_category` WHERE code=9996 OR code=9997"
        data = ReadDB().get_sql_all(sql)
        # self.assertEqual(0, data[1])
        data1 = data[1][0]
        print(data1)


if __name__ == '__main__':
    unittest.main()