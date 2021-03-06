# 导包json
import json


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

    def __init__(self, filename):
        self.filepath = "../data/"+filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            # 调用load方法加载
            return json.load(f)


if __name__ == '__main__':
    datas = ReadJson().read_json("addCon_more.json")
    # 新建空列表，添加读取json数据
    arrs = []
    # 使用遍历
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("name"),
                     data.get("value"),
                     data.get("expect_result"),
                     data.get("status_code")))
    print(arrs)
