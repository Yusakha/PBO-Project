import mysql.connector, os
from datetime import datetime

class sqlServer:
    def __init__(self):
        self.startDB()
        
    def startDB(self):
        try:
            con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="management"
            )
            cursor=con.cursor()
            
            
        except mysql.connector.Error as e:
            print(e)
        
        try:
            cursor.execute("CREATE DATABASE Management")
            print(cursor)
        except:
            print("CREATE DATABASE Management pass")
            pass
        
        try:
            cursor.execute("drop TABLE person")
            print(cursor)
        except:
            print("DROP TABLE person pass")
            pass

        try:
            cursor.execute("CREATE TABLE person (ID_Person int PRIMARY KEY NOT NULL AUTO_INCREMENT, Nama VARCHAR(255) NOT NULL, Umur int(255) NOT NULL, Jenis_Kelamin ENUM ('L', 'P') NOT NULL, Role ENUM ('Owner', 'Karyawan') NOT NULL, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, created datetime NOT NULL)")
            print(cursor)
        except:
            print("CREATE TABLE person pass")
            pass

        try:
            sql = "INSERT INTO person (Nama , Umur , Jenis_Kelamin, Role , username , password , created) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = ("Yoga", "18", "L", "Owner", "yusakha", "yusakha", datetime.now())
            cursor.execute(sql, val)

            sql = "INSERT INTO person (Nama , Umur , Jenis_Kelamin, Role , username , password , created) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = ("Afandy", "19", "L", "Owner", "kiyan", "kiyan", datetime.now())
            cursor.execute(sql, val)

            sql = "INSERT INTO person (Nama , Umur , Jenis_Kelamin, Role , username , password , created) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = ("Dayat", "20", "L", "Karyawan", "dayat", "dayat", datetime.now())
            cursor.execute(sql, val)

            sql = "INSERT INTO person (Nama , Umur , Jenis_Kelamin, Role , username , password , created) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = ("Mahesa", "20", "L", "Karyawan", "mahesa", "mahesa", datetime.now())
            cursor.execute(sql, val)

            con.commit()
            print(cursor)

        except:
            print("Insert INTO person pass")
            pass
        
        try:
            cursor.execute("drop TABLE barang")
            print(cursor)
        except:
            print("DROP TABLE barang pass")
            pass

        try:
            cursor.execute("CREATE TABLE barang (ID_Barang int PRIMARY KEY NOT NULL AUTO_INCREMENT, Nama_Barang VARCHAR(255) NOT NULL, Jumlah_Barang int(255) NOT NULL, Satuan VARCHAR(255) NOT NULL, Tanggal_Kadaluarsa datetime NOT NULL)")
            print(cursor)
        except:
            print("CREATE TABLE barang pass")
            pass
        
        try:
            sql = "INSERT INTO barang (Nama_Barang, Jumlah_Barang, Satuan, Tanggal_Kadaluarsa) VALUES (%s, %s, %s, %s)"
            val = ("Telur", "18", "pcs", "2021-1-6")
            cursor.execute(sql, val)

            sql = "INSERT INTO barang (Nama_Barang, Jumlah_Barang, Satuan, Tanggal_Kadaluarsa) VALUES (%s, %s, %s, %s)"
            val = ("Beras 10kg", "20", "karung", "2021-3-10")
            cursor.execute(sql, val)

            sql = "INSERT INTO barang (Nama_Barang, Jumlah_Barang, Satuan, Tanggal_Kadaluarsa) VALUES (%s, %s, %s, %s)"
            val = ("Beras 25kg", "20", "karung", "2021-3-10")
            cursor.execute(sql, val)

            sql = "INSERT INTO barang (Nama_Barang, Jumlah_Barang, Satuan, Tanggal_Kadaluarsa) VALUES (%s, %s, %s, %s)"
            val = ("INDOMIE Cabe Ijo", "5", "dus", "2021-4-10")
            cursor.execute(sql, val)

            con.commit()
            print(cursor)

        except:
            print("Insert INTO barang pass")
            pass
            
        try:
            cursor.execute("CREATE TABLE history (ID_History int PRIMARY KEY NOT NULL AUTO_INCREMENT, FOREIGN KEY(ID_History) REFERENCES person(ID_Person) NOT NULL, FOREIGN KEY(ID_History) REFERENCES barang(ID_Barang) NOT NULL, Keterangan ENUM('Input', 'Output') NOT NULL, Jumlah int(255) NOT NULL, Tanggal datetime NOT NULL)")
            print(cursor)
        except:
            print("CREATE TABLE history pass")
            pass

sqlServer()
# os.system('cls')