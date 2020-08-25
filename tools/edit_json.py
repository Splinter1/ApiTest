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

class EditJson():

    # def __init__(self, filename):
    #     self.filepath = "../data/"+filename

    def edit_json(self, filename, key, value):
        self.filepath = "../data/" + filename
        with open(self.filepath, "r", encoding="utf-8") as load_f:
            load_dict = json.load(load_f)
            load_dict[key] = value

        with open(self.filepath, "w", encoding="utf-8") as dump_f:
            json.dump(load_dict, dump_f)
        return load_dict



if __name__ == '__main__':
    data = EditJson().edit_json("addCon.json", 'name', '牛逼')
    print(data)


