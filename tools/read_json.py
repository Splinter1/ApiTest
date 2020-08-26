# 导包json
import json
import os


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

    # def __init__(self):
    #     self.filepath = "../data/"+filename

    def read_json(self,filename):
        path = os.path.dirname(os.path.dirname(__file__))
        filepath = path + "/data/" + filename
        # print(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            # 调用load方法加载

            return json.load(f)


if __name__ == '__main__':
    data = ReadJson().read_json("addCon.json")

    # 新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("name"),
                 data.get("value"),
                 data.get("expect_result"),
                 data.get("status_code")))
    print(arrs)
