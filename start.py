from conect.sqlServer import connection
from datetime import datetime
from tabulate import tabulate
from Views.text import View

class start(connection):
    def __init__(self):
        super().__init__()
        self.login()

    def login(self):
        try:
            self.createDB() #First Step Only
            View.clear()
            uname = input("Masukkan Username: ").lower()
            pword = input("Masukkan Password: ")
            tempNama = []
            tempUname = []
            tempPword = []
            tempRole = []
            tempUserID = []
            tempJ = 0
            query = ('SELECT ID_Person, Nama, username, passwords, role FROM person')
            for x in self.select_all(query):
                tempUserID.append(x[0])
                tempNama.append(x[1])
                tempUname.append(x[2])
                tempPword.append(x[3])
                tempRole.append(x[4])
            for i in range(len(tempUname)):
                if uname == tempUname[i] and pword == tempPword[i]:
                    self.namaUser = tempNama[i]
                    self.UserID = tempUserID[i]
                    View.clear()
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
                        View.clear()
                        y = input("Login Failed. Silahkan coba lagi\nKetik 'exit' untuk exit : ").lower()
                        if y == "exit":
                            self.close()
                        else :
                            View.clear()
                            start()
        except:
            pass

    def ownerMenu(self):
        while True:
            jawab = input("""Selamat Datang {}, Berikut adalah menu yang tersedia:
    1.Tambah karyawan
    2.Tampilkan tabel database karyawan
    3.Delete Karyawan
    4.Tampilkan tabel history
    5.Tampilkan tabel barang
    6.Ambil Barang
    7.Tambah Stok Barang
    8.Tambah Barang
    9.Exit

Jawab : """.format(self.namaUser))
            if jawab == '1':
                View.clear()
                print("Menambah Karyawan")
                self.createKaryawan()
                print()
            elif jawab == '2':
                View.clear()
                self.showKaryawan()
                print()
            elif jawab == '3':
                View.clear()
                self.deleteKaryawan()
                print()
            elif jawab == '4':
                View.clear()
                self.history()
                print()
            elif jawab == '5':
                View.clear()
                self.showBarang()
                print()
            elif jawab == '6':
                View.clear()
                self.ambilBarang()
                print()
            elif jawab == '7':
                View.clear()
                self.tambahStokBarang()
                print()
            elif jawab == '8':
                View.clear()
                self.tambahBarang()
                print()
            elif jawab == '9':
                return self.close()
            else:
                View.clear()
                View.jawabFalse()

    def karyawanMenu(self):
        while True:
            jawab = input("""Selamat Datang {}, Berikut adalah menu yang tersedia:
    1.Tampilkan tabel history
    2.Tampilkan tabel barang
    3.Ambil Barang
    4.Tambah Stok Barang
    5.Tambah Barang
    6.Exit

Jawab : """.format(self.namaUser))
            if jawab == '1':
                View.clear()
                self.history()
                print()
            elif jawab == '2':
                View.clear()
                self.showBarang()
                print()
            elif jawab == '3':
                View.clear()
                self.ambilBarang()
                print()
            elif jawab == '4':
                View.clear()
                self.tambahStokBarang()
                print()
            elif jawab == '5':
                View.clear()
                self.tambahBarang()
                print()
            elif jawab == '6':
                return self.close()
            else:
                View.clear()
                View.jawabFalse()

        
    def createKaryawan(self):
        self.nama = input("Masukkan Nama Karyawan : ").title()
        self.umur = int(input("Masukkan umur Karyawan : "))
        self.jenisKelamin = input("Masukkan jenis kelamin Karyawan (L/P) : ").upper()
        self.role = "Karyawan"
        self.username = input("Masukkan username Karyawan : ").lower()
        self.password = input("Masukkan password Karyawan : ")
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
        return print(tabulate(tempResult, headers=header))

    def deleteKaryawan(self):
        self.showKaryawan()
        jawabDelete = int(input("\nMasukkan id yang mau di hapus : "))
        sql = "DELETE FROM person WHERE ID_Person = {}".format(jawabDelete)
        self.fetchone(sql)
        return View.done()

    def ambilBarang(self):
        self.showBarang()
        jawabID = int(input("\nMasukkan id yang mau di ambil : "))
        jawabStok = int(input("Masukkan stock yang mau di ambil : "))
        sql = """
        Select Jumlah_Barang
        FROM barang
        WHERE ID_Barang = {}
        """.format(jawabID)
        res = self.fetchone(sql)
        for x in res :
            if jawabStok > x :
                print("Barang yang diambil melebihi stok")
                break
            else :
                hasilStok = x - jawabStok
                sql = """
                UPDATE barang
                SET Jumlah_Barang = {}
                WHERE ID_Barang = {}
                """.format(hasilStok,jawabID)
                self.fetchone(sql)
                
                sql =  """SELECT Satuan FROM barang
                WHERE ID_Barang = {}""".format(jawabID)
                res = self.fetchone(sql)
                for y in res :
                    satuan = y

                sql = """INSERT INTO history (PersonID,
                BarangID, Keterangan, Jumlah, Satuan, Tanggal)
                VALUES (%s, %s, %s, %s, %s, %s)"""
                val = (self.UserID, jawabID, "Output", jawabStok, satuan, datetime.now())
                self.inputDB(sql, val)
                View.done()
        return 

    def tambahBarang(self):
        self.nama = input("Masukkan nama barang : ").title()
        self.stok = int(input("Masukkan jumlah barang : "))
        self.satuan = input("Masukkan nama satuannya : ").lower()
        self.tanggal = input("Masukkan tanggal kadaluarsa barang (YYYY-MM-DD) : ")

        sql = """INSERT INTO barang (Nama_Barang , Jumlah_Barang , Satuan, Tanggal_Kadaluarsa)
        VALUES (%s, %s, %s, %s)"""
        val = (self.nama, self.stok, self.satuan, self.tanggal)
        self.inputDB(sql, val)

        sql =  """SELECT ID_Barang FROM barang
        WHERE Nama_Barang = '{}'""".format(self.nama)
        res = self.fetchone(sql)
        for x in res :
            self.barangID = x

        sql = """INSERT INTO history (PersonID,
        BarangID, Keterangan, Jumlah, Satuan, Tanggal)
        VALUES (%s, %s, %s, %s, %s, %s)"""
        val = (self.UserID, self.barangID, "Input", self.stok, self.satuan, datetime.now())
        self.inputDB(sql, val)
        View.done()

    def tambahStokBarang(self):
        self.showBarang()
        jawabID = int(input("\nMasukkan id yang mau di ambil : "))
        jawabStok = int(input("Masukkan stock yang mau di ambil : "))
        sql = """
        Select Jumlah_Barang
        FROM barang
        WHERE ID_Barang = {}
        """.format(jawabID)
        res = self.fetchone(sql)
        for x in res :
            jumlahStok = x + jawabStok
            sql = """
            UPDATE barang
            SET Jumlah_Barang = {}
            WHERE ID_Barang = {}
            """.format(jumlahStok,jawabID)
            self.fetchone(sql)

            sql =  """SELECT Satuan FROM barang
            WHERE ID_Barang = {}""".format(jawabID)
            res = self.fetchone(sql)
            for y in res :
                satuan = y

            sql = """INSERT INTO history (PersonID,
            BarangID, Keterangan, Jumlah, Satuan, Tanggal)
            VALUES (%s, %s, %s, %s, %s, %s)"""
            val = (self.UserID, jawabID, "Input", jawabStok, satuan, datetime.now())
            self.inputDB(sql, val)
            View.done()
        return 

    def history(self): 
        query = ("SELECT * FROM history")
        result = self.select_all(query)
        header = ["HistoryID","PersonID","BarangID","Keterangan","Jumlah","Satuan","Tanggal"]
        tempResult = []
        for x in result:
            tempResult.append(x)
        return print(tabulate(tempResult, headers=header))

    def showBarang(self):
        query = ('SELECT * FROM barang')
        result = self.select_all(query)
        header = ["ID_Barang","Nama_Barang","Jumlah_Barang","Satuan","Tanggal_Kadaluarsa"]
        tempResult = []
        for x in result:
            tempResult.append(x)
        return print(tabulate(tempResult, headers=header))
start()