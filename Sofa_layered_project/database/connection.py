import mysql.connector 
class Database:
    def connect(self):
        print("Database connected")
        conn=mysql.connector.connect(host='localhost',port=3306,user='root',password='root',database='sofa_customizer')
        return conn
