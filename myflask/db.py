import pymysql
def getconn():
    conn=pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='1234',
        database='python_mysql',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor


    )
    return conn



def query_data(sql):
    conn=getconn()
    try:
        cursor=conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn.close()

if __name__=='__main__':
    sql='select * from user'
    datas = query_data(sql)
    import pprint
    pprint.pprint(datas)
