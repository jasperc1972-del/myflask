import pymysql

def getconn():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='1234',
        database='python_mysql',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def query_data(sql, params=None):
    conn = getconn()
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn.close()

def insert_or_update_data(sql, params=None):
    conn = getconn()
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()



if __name__=='__main__':
    sql="insert user(name,sex,age,email) values('david','man',34,'david@gmail.com')"
    insert_or_update_data(sql)

    sql='select * from user'
    datas = query_data(sql)
    import pprint
    pprint.pprint(datas)
