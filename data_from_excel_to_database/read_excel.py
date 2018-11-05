#对于excel文件行列都是从0开始编号
#coding=utf-8
import sys
import xlrd
from col_conversion_function import col_name_To_num
from col_conversion_function import col_num_To_name

def read_data_from_excel(file_path,sheet_name,row,col):
    #获取数据，获取合并单元格信息时需要将formatting_info参数设置为True，默认是False
    file_excel = xlrd.open_workbook(file_path,formatting_info=True)
    #获取sheet
    sheet = file_excel.sheet_by_name(sheet_name)
    #获取总行数、总列数
    rows = sheet.nrows
    cols = sheet.ncols
    row_start = int(row.get('start'))
    row_end = int(row.get('end'))
    col_start = col_name_To_num(col.get('start'))
    col_end = col_name_To_num(col.get('end'))
    #判断配置参数是否有误
    if row_start < 0 or row_start > row_end or row_end > rows or col_start < 0 or col_start > col_end or col_end > cols:
        print('excel文件参数有错，请检查......Error')
        sys.exit(1)
    #读取数据
    datas = []
    for x in range(row_start-1,row_end):
        item = {}
        for y in range(col_start,col_end+1):
            item[col_num_To_name(y)]=sheet.cell(x,y).value
        datas.append(item)
    return datas

if __name__ == '__main__':
    #文件路径转码
    #file_path = file_path.decode('utf-8')
    #获取所有合并单元格
    #merge_cells_index = table.merged_cells
    #print(len(merge_cells_index))
    pass