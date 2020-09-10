import json
from tools.read_json import ReadJson
from deepdiff import DeepDiff


def handle_result(url, code):
    data = ReadJson().get_value(url, "code_message.json")
    for i in data:
        message = i.get(str(code))
        # 如果message不等于空则返回message
        if message:
            return message
    return None


def read_json(url, status):
    data = ReadJson().get_value(url, "code_message.json")
    for i in data:
        message = i.get(status)
        # 如果message不等于空则返回message
        if message:
            return message
    return None


def handle_result_json(dict1, url, status):
    if status == 0:
        status="success"
    else:
        status="fail"
    dict2 = read_json(url, status)
    cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
    if cmp_dict.get("dictionary_item_added"):
        return False
    else:
        return True




if __name__ == '__main__':
    pass
    # msg = handle_result("/?&s=App.Config.AddConfig", 0)
    # print(msg)
    # dict1 = {'ret': 200, 'data': {'err_code': 1, 'err_msg': '配置已存在，不能重复添加'}, 'msg': 'V3.1.0 YesApi App.Config.AddConfig'}
    # dict2 = {'ret': 200, 'msg': 'V3.1.0 YesApi App.Config.AddConfig', 'sd':12}
    # print(handle_result_json(dict1, dict2))
