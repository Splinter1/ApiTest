import openpyxl
import os

path = os.path.dirname(os.path.dirname(__file__))
filepath = path + "/data/"

# open_excel = openpyxl.load_workbook(filepath+"excel.xlsx")
# sheet_name = open_excel.sheetnames
# excel_value = open_excel[sheet_name[0]]
# print(excel_value)

# 获取一个单元格的数据
# print(excel_value.cell(1,2).value)
# print(excel_value.cell(2,3).value)
# print(excel_value.max_row)


class HandExcel:
    def load_excel(self):
        open_excel = openpyxl.load_workbook(filepath + "excel.xlsx")
        return open_excel

    def get_sheet_data(self,index=None):
        sheet_name = self.load_excel().sheetnames
        if index == None:
            index = 0
        data = self.load_excel()[sheet_name[index]]
        return data

    def get_cell_value(self, row, cell):
        data = self.get_sheet_data().cell(row, cell).value
        return data

    def get_rows(self):
        #   获取行数
        rows = self.get_sheet_data().max_row
        return rows

    def get_rows_value(self, row):
        # 获取一行的内容
        row_list = []
        for i in self.get_sheet_data()[row]:
            row_list.append(i.value)
        return row_list


if __name__ == '__main__':
    print(HandExcel().get_cell_value(2, 3))
    print(HandExcel().get_rows_value(2))