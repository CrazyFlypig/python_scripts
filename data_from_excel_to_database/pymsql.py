#coding=utf-8
import pymysql

def init_jdbc_conn(jdbc_params):
    conn = pymysql.connect(
        host = jdbc_params['host'],
        port = int(jdbc_params['port']),
        user = jdbc_params['user'],
        passwd = jdbc_params['passwd'],
        db = jdbc_params['db'],
        charset = 'utf8',
        #pymysql默认select获取的数据是元祖类型，使用此参数获取字典类型的数据
        cursorclass = pymysql.cursors.DictCursor,
    )
    return conn

def insert_data(jdbc_params,sql_statements):
    result = False
    conn = init_jdbc_conn(jdbc_params)
    cursor = conn.cursor()
    field_params = []
    value_params = []
    for statement in sql_statements:
        fields = statement.get('fields')
        values = statement.get('values')
        field_param = ''
        for field in fields:
            field_param += (field + ',')
        field_param = field_param[0:len(field_param)-1]
        field_params.append(field_param)
        value_param = ''
        for value in values:
            value_param += ("'" + str(value) + '\',')
        value_param = value_param[0:len(value_param)-1]
        value_params.append(value_param)
    try:
        num = 0
        if len(value_params) == len(field_params):
            num = len(field_params)
        for i in range(num):
            sql = "INSERT INTO " + jdbc_params['table'] + "(" + field_params[i] + ") VALUES(" + value_params[i] + ")"
            cursor.execute(sql)
        conn.commit()
        result = True
    except Exception as e:
        # 如果sql语句出现问题，则执行回滚操作
        conn.rollback()
        print(e)
    finally:
        # 不论是否成功，执行关闭游标和数据库连接
        cursor.close()
        conn.close()
        return result





if __name__ == '__main__':
    pass