import mysql.connector, os
from datetime import datetime
from Views.text import View

class connection:
    def __init__(self):
        try:
            self.__con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="management"
            )
            self.__cursor = self.__con.cursor()
            
        except mysql.connector.Error as e:
            View.errors(e)

    def close(self):
        print("\nExit. . .")
        return self.__con.close()

    def fetchalll(self, query):
        try:
            self.__cursor.execute(query)
            res = self.__cursor.fetchall()
            return res
        except mysql.connector.Error as e:
            View.errors(e)

    def fetchone(self, query):
        try:
            self.__cursor.execute(query)
            res = self.__cursor.fetchone()
            self.__con.commit()
            return res
        except mysql.connector.Error as e:
            View.errors(e)

    def inputDB(self, sql, val):
        try:
            self.__cursor.execute(sql, val)
            self.__con.commit()
        except mysql.connector.Error as e:
            View.errors(e)

    def createDB(self):
        # try:
        #     self.__cursor.execute("DROP TABLE history")
        #     print(self.__cursor)
        #     self.__cursor.execute("DROP TABLE barang")
        #     print(self.__cursor)
        #     self.__cursor.execute("DROP TABLE person")
        #     self.__con.commit()
        #     print(self.__cursor)
        # except:
        #     pass

        try:
            self.__cursor.execute("CREATE DATABASE Management")
            print(self.__cursor)
        except:
            pass

        try:
            self.__cursor.execute("""CREATE TABLE person (ID_Person int PRIMARY KEY NOT NULL AUTO_INCREMENT,
            Nama VARCHAR(255) NOT NULL, Umur int(255) NOT NULL,
            Jenis_Kelamin ENUM ('L', 'P') NOT NULL, Role ENUM ('Owner', 'Karyawan') NOT NULL,
            username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL,
            created datetime NOT NULL)""")
            print(self.__cursor)
        except:
            pass

        try:
            sql = """INSERT INTO person (ID_Person, Nama , Umur , Jenis_Kelamin, Role ,
            username , password , created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

            val = ("1", "Yoga", "18", "L", "Owner", "yusakha", "yusakha", datetime.now())
            self.__cursor.execute(sql, val)

            val = ("2", "Afandy", "19", "L", "Karyawan", "kiyan", "kiyan", datetime.now())
            self.__cursor.execute(sql, val)

            val = ("3", "Dayat", "20", "L", "Karyawan", "dayat", "dayat", datetime.now())
            self.__cursor.execute(sql, val)

            val = ("4", "Mahesa", "20", "L", "Karyawan", "mahesa", "mahesa", datetime.now())
            self.__cursor.execute(sql, val)

            self.__con.commit()
            print(self.__cursor)

        except:
            pass

        try:
            self.__cursor.execute("""CREATE TABLE barang (ID_Barang int PRIMARY KEY NOT NULL AUTO_INCREMENT,
            Nama_Barang VARCHAR(255) NOT NULL, Jumlah_Barang int(255) NOT NULL,
            Satuan VARCHAR(255) NOT NULL, Tanggal_Kadaluarsa datetime NOT NULL)""")
            print(self.__cursor)
        except:
            pass
        
        try:
            sql = """INSERT INTO barang (ID_Barang, Nama_Barang,
            Jumlah_Barang, Satuan, Tanggal_Kadaluarsa)
            VALUES (%s, %s, %s, %s, %s)"""

            val = ("1", "Telur", "18", "pcs", "2021-1-6")
            self.__cursor.execute(sql, val)

            val = ("2", "Beras 10kg", "20", "karung", "2021-3-10")
            self.__cursor.execute(sql, val)

            val = ("3", "Beras 25kg", "20", "karung", "2021-3-10")
            self.__cursor.execute(sql, val)

            val = ("4", "INDOMIE Cabe Ijo", "5", "dus", "2021-4-10")
            self.__cursor.execute(sql, val)

            self.__con.commit()
            print(self.__cursor)

        except:
            pass
            
        try:
            self.__cursor.execute("""CREATE TABLE history (ID_History int PRIMARY KEY NOT NULL AUTO_INCREMENT,
            PersonID int NOT NULL, FOREIGN KEY (PersonID) REFERENCES person (ID_Person),
            BarangID int NOT NULL, FOREIGN KEY (BarangID) REFERENCES barang (ID_Barang),
            Keterangan ENUM('Input', 'Output') NOT NULL,
            Jumlah int(255) NOT NULL,
            Satuan VARCHAR(255) NOT NULL,
            Tanggal datetime NOT NULL)""")
            print(self.__cursor)
        except:
            pass

        try:
            sql = """INSERT INTO history (ID_History, PersonID,
            BarangID, Keterangan, Jumlah, Satuan, Tanggal)
            VALUES (%s, %s, %s, %s, %s, %s, %s)"""

            val = ("1", "1", "1", "Input", "18", "pcs", datetime.now())
            self.__cursor.execute(sql, val)

            val = ("2", "1", "2", "Input", "20", "karung", datetime.now())
            self.__cursor.execute(sql, val)

            val = ("3", "1", "3", "Input", "20", "karung", datetime.now())
            self.__cursor.execute(sql, val)

            val = ("4", "1", "4", "Input", "5", "dus", datetime.now())
            self.__cursor.execute(sql, val)

            self.__con.commit()
            print(self.__cursor)
        except:
            pass