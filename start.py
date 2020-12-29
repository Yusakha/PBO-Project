from conect.sqlServer import connection
from datetime import datetime
from tabulate import tabulate
import os

class start(connection):
    def __init__(self):
        super().__init__()
        self.login()

    def login(self):
        try:
            os.system('cls')
            uname = input("Masukkan Username: ").lower()
            pword = input("Masukkan Password: ")
            tempUname = []
            tempPword = []
            tempRole = []
            tempJ = 0
            query = ('SELECT username, password, role FROM person')
            for x in self.select_all(query):
                tempUname.append(x[0])
                tempPword.append(x[1])
                tempRole.append(x[2])
            for i in range(len(tempUname)):
                if uname == tempUname[i] and pword == tempPword[i]:
                    os.system('cls')
                    print("Login Sucsess\n")
                    self.createDB()
                    if tempRole[i] == "Owner":
                        self.ownerMenu()
                    else:
                        self.karyawanMenu()
                else:
                    tempJ += 1
                    if tempJ != len(tempUname):
                        pass
                    else :
                        os.system('cls')
                        y = input("Login Failed. Silahkan coba lagi\nKetik 'y' untuk exit : ").lower()
                        if y == "y":
                            self.close()
                        else :
                            os.system('cls')
                            start()
        except:
            pass
    def ownerMenu(self):
        while True:
            jawab = input("""Selamat Datang, Berikut adalah menu yang tersedia:
    1.Register Karyawan
    2.Tampilkan database karyawan
    5.Exit

Jawab : """)
            print("p")
            if jawab == '1':
                os.system('cls')
                self.createKaryawan()
                print()
            if jawab == '2':
                os.system('cls')
                self.showKaryawan()
                print()
            # # if jawab == '3':
            # #     return editData()
            # if jawab == '4':
            #     return delete()
            if jawab == '5':
                return self.close()
            else:
                print('Silahkan masukkan nomor yang tersedia')

    def karyawanMenu(self):
        jawab = input("""Selamat Datang, Berikut adalah menu yang tersedia:
    1.Tampilkan Tabel Barang
    2.Inputkan barang
    3.Edit stok barang
    4.Delete barang
    5.Exit Program
        
Jawab : """)
        if jawab == '1':
            return self.show()
        # if jawab == '2':
        #     return inputData()
        # # if jawab == '3':
        # #     return editData()
        # if jawab == '4':
        #     return delete()
        if jawab == '5':
            return self.close()
        else:
            print('Silahkan masukkan nomor yang tersedia')
            return self.karyawanMenu()
    
    
    def createKaryawan(self):
        self.nama = input("Masukkan Nama Karyawan :")
        self.umur = int(input("Masukkan umur Karyawan :"))
        self.jenisKelamin = input("Masukkan jenis kelamin Karyawan :").upper()
        self.role = "Karyawan"
        self.username = input("Masukkan username Karyawan :")
        self.password = input("Masukkan password Karyawan :")
        self.created = datetime.now()
        sql = """INSERT INTO person (Nama , Umur , Jenis_Kelamin, Role ,
        username , password , created) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        val = (self.nama, self.umur, self.jenisKelamin, self.role, self.username, self.password, self.created)
        self.inputDB(sql, val)

    def showKaryawan(self):
        query = ("SELECT * FROM person WHERE Role='Karyawan'")
        result = self.select_all(query)
        header = ["ID_Person","Nama","Umur","Jenis_Kelamin","Role","username","password","created"]
        tempResult = []
        for x in result:
            tempResult.append(x)
        print(tabulate(tempResult, headers=header))

    def show(self):
        query = ('SELECT * FROM barang')
        for x in self.select_all(query):
            print(x)

    def close(self):
        print("Exit. . .")
        self.__con.close()

start()