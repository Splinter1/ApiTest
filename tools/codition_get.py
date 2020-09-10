from tools.handle_excel import HandExcel
from jsonpath_rw import  parse


def split_data(data):
    # addDevice1>data:err_code
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id, rule_data


def depend_data(data):
    # 获取依赖数据结果集
    case_id = split_data(data)[0]
    row_num = HandExcel().get_rows_num(case_id)
    excel_data = HandExcel().get_cell_value(row_num, 12)
    return excel_data


def get_depend_data(res_data, res_key):
    # 获取依赖字段
    json_exe = parse(res_key)
    res_data = eval(res_data)
    madle = json_exe.find(res_data)
    for math in madle:
        return math.value


def get_data(data):
    # 获取依赖数据
    res_data = depend_data(data)
    rule_data = split_data(data)[1]
    return get_depend_data(res_data, rule_data)





if __name__ == '__main__':
    # print(depend_data("addDevice1>data:err_code"))
    # print(split_data("addDevice1>data:err_code")[1])
    print(get_data("addDevice1>data.err_code"))


