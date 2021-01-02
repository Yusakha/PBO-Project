from conect.sqlServer import connection
from datetime import datetime
from tabulate import tabulate
from Views.text import View
from getpass import getpass

class start(connection):
    def __init__(self):
        super().__init__()
        self.login()

    def login(self):
        while True:
            try:
                self.createDB() #First Step Only
                View.clear()
                uname = input("Masukkan Username: ").lower()
                pword = getpass("Masukkan Password: ")
                tempNama = []
                tempUname = []
                tempPword = []
                tempRole = []
                tempUserID = []
                tempJ = 0
                query = ('SELECT ID_Person, Nama, username, password, role FROM person')
                for x in self.fetchalll(query):
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
            except KeyboardInterrupt:
                View.interrupt()
                break

    def ownerMenu(self):
        while True:
            try:
                View.printOmenu(self.namaUser)
                jawab = input('Jawab : ')
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
            except KeyboardInterrupt:
                View.interrupt()
                break

    def karyawanMenu(self):
        while True:
            try:
                View.printKmenu(self.namaUser)
                jawab = input('Jawab : ')
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
            except KeyboardInterrupt:
                View.interrupt()
                break

        
    def createKaryawan(self):
        while True:
            try:
                self.nama = input("Masukkan Nama Karyawan : ").title()
                query = ('SELECT Nama, username role FROM person')
                tempNama = []
                tempUsername = []
                for x in self.fetchalll(query):
                    tempNama.append(x[0])
                    tempUsername.append(x[1])
                if len(self.nama) == 0:
                    View.inputError()
                else:
                    self.umur = int(input("Masukkan umur Karyawan : "))
                    self.jenisKelamin = input("Masukkan jenis kelamin Karyawan (L/P) : ").upper()
                    if len(self.jenisKelamin) == 0:
                        View.inputError()
                    elif self.jenisKelamin != 'L' or self.jenisKelamin != 'P':
                        self.role = "Karyawan"
                        self.username = input("Masukkan username Karyawan : ").lower()
                        for i in range(len(tempNama)):
                            if self.username == tempUsername[i]:
                                print("username sudah ada!")
                            elif len(self.username) == 0:
                                View.inputError()
                            else:
                                self.password = input("Masukkan password Karyawan : ")
                                if len(self.password) == 0:
                                    View.inputError()
                                else:
                                    self.created = datetime.now()
                                    sql = """INSERT INTO person (Nama , Umur , Jenis_Kelamin, Role ,
                                    username , password , created) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                                    val = (self.nama, self.umur, self.jenisKelamin, self.role, self.username, self.password, self.created)
                                    self.inputDB(sql, val)
                                    break
                    else:
                        print("Silahkan Masukkan L / P")
            except ValueError:
                View.inputError()
            except KeyboardInterrupt:
                View.interrupt()
                break


    def showKaryawan(self):
        query = ("SELECT * FROM person WHERE Role='Karyawan'")
        result = self.fetchalll(query)
        header = ["ID_Person","Nama","Umur","Jenis_Kelamin","Role","username","password","created"]
        tempResult = []
        for x in result:
            tempResult.append(x)
        return print(tabulate(tempResult, headers=header))

    def deleteKaryawan(self):
        self.showKaryawan()
        while True:
            try:
                jawabDelete = int(input("\nMasukkan id yang mau di hapus : "))
                tempAnswer = []
                query = ('SELECT ID_Person FROM person WHERE Role = "Karyawan"')
                for x in self.fetchalll(query):
                    tempAnswer.append(x[0])
                if jawabDelete in tempAnswer:
                    tempID = []
                    query = ('SELECT ID_Person FROM person WHERE Role = "Karyawan"')
                    for x in self.fetchalll(query):
                        tempID.append(x[0])
                    if jawabDelete in tempID:
                        sql = "DELETE FROM person WHERE ID_Person = {}".format(jawabDelete)
                        self.fetchone(sql)
                        View.done()
                        break
                else:
                    View.inputError()
            except KeyboardInterrupt:
                View.interrupt()
                break
            except:
                View.inputError()

    def history(self): 
        query = ("SELECT * FROM history")
        result = self.fetchalll(query)
        header = ["HistoryID","PersonID","BarangID","Keterangan","Jumlah","Satuan","Tanggal"]
        tempResult = []
        for x in result:
            tempResult.append(x)
        return print(tabulate(tempResult, headers=header))

    def showBarang(self):
        query = ('SELECT * FROM barang')
        result = self.fetchalll(query)
        header = ["ID_Barang","Nama_Barang","Jumlah_Barang","Satuan","Tanggal_Kadaluarsa"]
        tempResult = []
        for x in result:
            tempResult.append(x)
        return print(tabulate(tempResult, headers=header))

    def ambilBarang(self):
        self.showBarang()
        while True:
            try:
                jawabID = int(input("\nMasukkan id yang mau di ambil : "))
                tempID = []
                query = ('SELECT ID_Barang FROM barang')
                for x in self.fetchalll(query):
                    tempID.append(x[0])
                if jawabID in tempID:
                    jawabStok = int(input("Masukkan stock yang mau di ambil : "))
                    if jawabStok <= 0:
                        View.inputZero()
                    else:
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
                        break
                else:
                    Views.jawabFalse()        
            except KeyboardInterrupt:
                View.interrupt()
                break
            except:
                View.inputError()

    def tambahStokBarang(self):
        self.showBarang()
        while True:
            try:
                tempJawab = []
                jawabID = int(input("\nMasukkan id yang mau di ambil : "))
                query = ('SELECT ID_Barang FROM barang')
                for x in self.fetchalll(query):
                    tempJawab.append(x[0])
                if jawabID in tempJawab:
                    jawabStok = int(input("Masukkan stock yang mau di ambil : "))
                    if jawabStok <= 0:
                        View.inputZero()
                    else:
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
                        break
                else:
                    View.jawabFalse()
            except KeyboardInterrupt:
                View.interrupt()
                break
            except:
                View.inputError()

    def tambahBarang(self):
        while True:
            try:
                self.nama = input("Masukkan nama barang : ").title()
                tempNama = []
                query = ('SELECT Nama_Barang FROM barang')
                for x in self.fetchalll(query):
                    tempNama.append(x[0])
                if self.nama in tempNama:
                    print("Nama barang sudah ada!!")
                elif len(self.nama) == 0:
                    View.inputError()
                else:
                    self.stok = int(input("Masukkan jumlah barang : "))
                    self.satuan = input("Masukkan nama satuannya : ").lower()
                    if len(self.satuan) == 0:
                        View.inputError()
                    else:
                        self.tahun = int(input("Masukkan tahun kadaluarsa barang (YYYY) : "))
                        if len(str(self.tahun)) != 4:
                            View.inputError()
                        else:
                            self.bulan = int(input("Masukkan bulan kadaluarsa barang (MM) : "))
                            if len(str(self.bulan)) != 2:
                                View.inputError()
                            else:
                                self.hari = int(input("Masukkan hari kadaluarsa barang (DD) : "))
                                if len(str(self.hari)) != 2:
                                    View.inputError()
                                else:
                                    self.tanggal = "{}-{}-{}".format(self.tahun,self.bulan,self.hari)

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
                                    break
            except KeyboardInterrupt:
                View.interrupt()
                break
            except:
                View.inputError()

start()