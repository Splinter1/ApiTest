# 导包json
import json
import os
import types
from tools.handle_ini import HandleIni


# 打开json文件并获取文件流
# with open("../data/addCon.json","r",encoding="utf-8") as f:
#     # 调用load方法加载
#     data = json.load(f)
#     print("获取的数据位",data)

# 使用函数进行封装
# def read_json():
#     with open("../data/addCon.json", "r", encoding="utf-8") as f:
#         # 调用load方法加载
#         return json.load(f)

# 使用参数替换 静态文件名

class ReadJson():
    path = os.path.dirname(os.path.dirname(__file__))
    filepath = path + "/data/"

    # def __init__(self):
    #     self.filepath = "../data/"+filename

    def read_json(self,filename):
        path = os.path.dirname(os.path.dirname(__file__))
        filepath = path + "/data/" + filename
        # print(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            # 调用load方法加载
            return json.load(f)

    def get_value(self, key, filename):
        data = self.read_json(filename)
        # 检验传入的url是否含有http字段，若含有则自动删减
        if "http" in key:
            base_url = HandleIni().read_ini("host")
            key = key.replace(base_url,'')
        else:
            pass
        return data[key]

    def key_tovalue(self, dict1, key, default=None):
        tmp = dict1
        for k,v in tmp.items():
            if k == key:
                return v
            else:
                if isinstance(v, dict):
                    ret = ReadJson.key_tovalue(self, dict1=v, key=key)
                    if ret is not default:
                        return ret
        return default

    def write_value(self, data):
        data_value = json.dumps(data ,ensure_ascii=False)
        with open(self.filepath + "cookie.json", "w")as f:
            f.write(data_value)




if __name__ == '__main__':
    # data = ReadJson().read_json("addCon.json")
    #
    # # 新建空列表，添加读取json数据
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("name"),
    #              data.get("value"),
    #              data.get("expect_result"),
    #              data.get("status_code")))
    # print(arrs)
    data = {'aaa' : 'bbbb'}
    ReadJson().write_value(data)

