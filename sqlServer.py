import mysql.connector, os, datetime

class sqlServer:
    def __init__(self):
        self.startDB()
        
    def startDB(self):
        try:
            con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            # database="management"
            )
            cursor=con.cursor()
            
        except mysql.connector.Error as e:
            print(e)
        
        try:
            cursor.execute("CREATE DATABASE Management")
            print(cursor)
        except:
            print("pass")
            pass

        try:
            cursor.execute("CREATE TABLE Person (ID PRIMARY KEY NOT NULL AUTO_INCREMENT, Nama VARCHAR(2SS) NOT NULL, Umur int(255), Jenis_Kelamin ENUM ('L', 'P') NOT NULL, Role ENUM ('Owner', 'Karyawan') NOT NULL, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, created datetime NOT NULL)")
            print(cursor)
        except:
            print("pass")
            pass

sqlServer()



