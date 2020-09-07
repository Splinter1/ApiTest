import json
from tools.read_json import ReadJson


def handle_result(url, code):
    data = ReadJson().get_value(url, "code_message.json")
    for i in data:
        message = i.get(str(code))
        # 如果message不等于空则返回message
        if message:
            return message
    return None

if __name__ == '__main__':
    msg = handle_result("/?&s=App.Config.AddConfig", 0)
    print(msg)
