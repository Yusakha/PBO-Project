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
            pass

        try:
            cursor.execute("CREATE TABLE person (ID_Person int PRIMARY KEY NOT NULL AUTO_INCREMENT, Nama VARCHAR(255) NOT NULL, Umur int(255) NOT NULL, Jenis_Kelamin ENUM ('L', 'P') NOT NULL, Role ENUM ('Owner', 'Karyawan') NOT NULL, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, created datetime NOT NULL)")
            print(cursor)
        except:
            pass

        try:
            sql = "INSERT INTO person (ID_Person, Nama , Umur , Jenis_Kelamin, Role , username , password , created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = ("1", "Yoga", "18", "L", "Owner", "yusakha", "yusakha", datetime.now())
            cursor.execute(sql, val)

            sql = "INSERT INTO person (Nama , Umur , Jenis_Kelamin, Role , username , password , created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = ("2", "Afandy", "19", "L", "Owner", "kiyan", "kiyan", datetime.now())
            cursor.execute(sql, val)

            sql = "INSERT INTO person (Nama , Umur , Jenis_Kelamin, Role , username , password , created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = ("3", "Dayat", "20", "L", "Karyawan", "dayat", "dayat", datetime.now())
            cursor.execute(sql, val)

            sql = "INSERT INTO person (Nama , Umur , Jenis_Kelamin, Role , username , password , created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = ("4", "Mahesa", "20", "L", "Karyawan", "mahesa", "mahesa", datetime.now())
            cursor.execute(sql, val)

            con.commit()
            print(cursor)

        except:
            pass

        try:
            cursor.execute("CREATE TABLE barang (ID_Barang int PRIMARY KEY NOT NULL AUTO_INCREMENT, Nama_Barang VARCHAR(255) NOT NULL, Jumlah_Barang int(255) NOT NULL, Satuan VARCHAR(255) NOT NULL, Tanggal_Kadaluarsa datetime NOT NULL)")
            print(cursor)
        except:
            pass
        
        try:
            sql = "INSERT INTO barang (ID_Barang, Nama_Barang, Jumlah_Barang, Satuan, Tanggal_Kadaluarsa) VALUES (%s, %s, %s, %s, %s)"
            val = ("1", "Telur", "18", "pcs", "2021-1-6")
            cursor.execute(sql, val)

            sql = "INSERT INTO barang (ID_Barang, Nama_Barang, Jumlah_Barang, Satuan, Tanggal_Kadaluarsa) VALUES (%s, %s, %s, %s, %s)"
            val = ("2", "Beras 10kg", "20", "karung", "2021-3-10")
            cursor.execute(sql, val)

            sql = "INSERT INTO barang (ID_Barang, Nama_Barang, Jumlah_Barang, Satuan, Tanggal_Kadaluarsa) VALUES (%s, %s, %s, %s, %s)"
            val = ("3", "Beras 25kg", "20", "karung", "2021-3-10")
            cursor.execute(sql, val)

            sql = "INSERT INTO barang (ID_Barang, Nama_Barang, Jumlah_Barang, Satuan, Tanggal_Kadaluarsa) VALUES (%s, %s, %s, %s, %s)"
            val = ("4", "INDOMIE Cabe Ijo", "5", "dus", "2021-4-10")
            cursor.execute(sql, val)

            con.commit()
            print(cursor)

        except:
            pass
            
        try:
            cursor.execute("CREATE TABLE history (ID_History int PRIMARY KEY NOT NULL AUTO_INCREMENT, FOREIGN KEY (ID_History) REFERENCES person (ID_Person) NOT NULL, FOREIGN KEY (ID_History) REFERENCES barang (ID_Barang) NOT NULL, Keterangan ENUM('Input', 'Output') NOT NULL, Jumlah int(255) NOT NULL, Tanggal datetime NOT NULL)")
            print(cursor)
        except:
            print("CREATE TABLE history pass")
            pass

        try:
            cursor.execute("CREATE TA BLE test (ID int PRIMARY KEY NOT NULL AUTO_INCREMENT, ID_History, FOREIGN KEY (ID_History) REFERENCES person (ID_Person))")
            print(cursor)
        except:
            print("CREATE TABLE history test")
            pass
        
        try:
            # os.system('cls')
            uname = input("Masukkan Username: ")
            pword = input("Masukkan Password: ")
            tempUname = []
            tempPword = []
            tempJ = 0
            cursor.execute('SELECT username, password FROM person')
            res = cursor.fetchall()
            for x in res:
                tempUname.append(x[0])
                tempPword.append(x[1])
            for i in range(len(tempUname)):
                    if uname == tempUname[i] and pword == tempPword[i]:
                        os.system('cls')
                        print("Login Sucsess")
                        # sqlServer.menu()
                    else:
                        tempJ += 1
                        if tempJ != len(tempUname):
                            pass
                        else :
                            os.system('cls')
                            print("Login Failed")
                            # sqlServer()
        except:
            pass

        # def menu():
        #     jawab = input("""Selamat Datang, Berikut adalah menu yang tersedia:
        #         1.Tampilkan Tabel Barang
        #         2.Inputkan barang
        #         3.Edit stok barang
        #         4.Delete barang
        #         5.Exit Program
            
        #         Jawab : """)
        #     if jawab == '1':
        #         return show()
        #     # if jawab == '2':
        #     #     return inputData()
        #     # # if jawab == '3':
        #     # #     return editData()
        #     # if jawab == '4':
        #     #     return delete()
        #     if jawab == '5':
        #         return close()
        #     else:
        #         print('Silahkan masukkan nomor yang tersedia')
        #     return menu()

        # def show():
        #     cursor.execute('SELECT * FROM barang')
        #     res = cursor.fetchall()
        #     for x in res:
        #         print(x)
        # def close():
        #     print("Exit. . .")
        #     con.close()
sqlServer()
# os.system('cls')