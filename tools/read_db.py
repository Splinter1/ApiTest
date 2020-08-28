import pymysql


# 新建工具库 数据库
class ReadDB:
    # 定义连接对象 类方法
    conn = None

    # 获取连接对象方法封装
    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect("114.115.203.110",
                                        "root",
                                        "1qaz!QAZ",
                                        "iot_center_dev",
                                        charset="utf8")
        # 返回连接对象
        return self.conn

    # 获取游标对象方法
    def get_cursor(self):
        return self.get_conn().cursor()

    # 关闭游标对象方法
    def close_cursor(self, cursor):
        # 如果cursor不为空
        if cursor:
            cursor.close()

    # 关闭连接对象
    def close_conn(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    # 主要执行方法 - 在外界调用
    def get_sql_one(self, sql):
        # 定义游标对象及数据
        sursor = None
        data = None
        try:
            # 获取游标对象
            sursor = self.get_cursor()
            # 执行调用方法
            sursor.execute(sql)
            # 获取结果
            data = sursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            # 关闭对象
            self.close_cursor(sursor)
            self.close_conn()
            # 返回执行结果
            return data

    def get_sql_all(self, sql):
        # 定义游标对象及数据
        sursor = None
        data = None
        try:
            # 获取游标对象
            sursor = self.get_cursor()
            # 执行调用方法
            sursor.execute(sql)
            # 获取结果
            data = sursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            # 关闭对象
            self.close_cursor(sursor)
            self.close_conn()
            # 返回执行结果
            return data