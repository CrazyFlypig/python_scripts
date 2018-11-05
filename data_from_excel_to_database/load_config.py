#coding=utf-8

import xml.dom.minidom

def load_config(path):
    #打开xml文档
    dom = xml.dom.minidom.parse(path)
    #得到文档元素对象
    root = dom.documentElement
    #初始化配置文件列表
    file_config = []
    #获取配置文件数目
    file_nums = int(root.getElementsByTagName('file-num')[0].firstChild.data)
    for i in range(file_nums):
        #初始化参数字典
        params = {}
        file = root.getElementsByTagName('file')[i]
        #获取文件路径
        params['file_path']=file.getElementsByTagName('path')[0].firstChild.data
        #获取excel的sheet名
        params['sheet_name']=file.getElementsByTagName('sheet')[0].firstChild.data
        #获取jdbc配置参数
        jdbc_params = {}
        jdbc = file.getElementsByTagName('jdbc')[0]
        jdbc_params['host']=jdbc.getAttribute('host')
        jdbc_params['port']=jdbc.getAttribute('port')
        jdbc_params['user']=jdbc.getAttribute('user')
        jdbc_params['passwd']=jdbc.getAttribute('passwd')
        jdbc_params['table']=jdbc.getAttribute('table')
        jdbc_params['db']=jdbc.getAttribute('db')
        params['jdbc_params']=jdbc_params
        #获取行列配置
        row_params = {}
        row = file.getElementsByTagName('row')[0]
        row_params['start']=row.getAttribute('start')
        row_params['end']=row.getAttribute('end')
        params['row']=row_params
        col_params = {}
        col = file.getElementsByTagName('col')[0]
        col_params['start']=col.getAttribute('start')
        col_params['end']=col.getAttribute('end')
        params['col']=col_params
        #获取列与字段的映射参数
        field_params = {}
        fields = file.getElementsByTagName('fields')[0]
        field_num = int(fields.getElementsByTagName('num')[0].firstChild.data)
        field = fields.getElementsByTagName('field')
        for j in range(0,field_num):
            excel_key = field[j].getElementsByTagName('excel')[0].firstChild.data
            db_key = field[j].getElementsByTagName('db')[0].firstChild.data
            field_params[excel_key]=db_key
        params['field_params']=field_params
        file_config.append(params)
    return file_config

if __name__ == '__main__':
    out = load_config('config.xml')
    print(out)