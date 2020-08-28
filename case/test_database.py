# 导包
import pymysql

# 获取接连对象
conn = pymysql.connect("114.115.203.110", "root", "1qaz!QAZ", "iot_center_dev", charset="utf8")
# 获取游标对象
cursor = conn.cursor()
# 执行sql语句
sql = "SELECT name,is_deleted FROM `tb_device_category` WHERE code=9996"
cursor.execute(sql)
# 获取结果，并进行断言
# print(cursor.fetchone())
result = cursor.fetchone()
print(result)
assert '安诺信Anosi' == result[0]

# 关闭游标对象
cursor.close()
# 关闭连接对象
conn.close()