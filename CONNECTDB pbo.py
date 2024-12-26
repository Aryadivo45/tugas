import pymysql

class MyDB:
    def connect(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='UNIVERSITAS')
        cur = con.cursor()
        return con, cur