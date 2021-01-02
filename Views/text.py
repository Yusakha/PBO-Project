import os

class View:
    @staticmethod
    def clear():
        os.system('cls')

    @staticmethod
    def interrupt():
        print('Keyboard interrupted')

    @staticmethod
    def jawabFalse():
        print('Silahkan masukkan nomor yang tersedia\n')

    @staticmethod
    def done():
        print('Selesai~')

    @staticmethod
    def inputError():
        print("Inputan Salah")

    @staticmethod
    def inputZero():
        print("Inputan tidak boleh <= 0")

    @staticmethod
    def errors(arg):
        print("Ada yang Error :\n{}".format(arg))

    @staticmethod
    def printOmenu(nama):
        print("""Selamat Datang {}, Berikut adalah menu yang tersedia:
    1.Tambah karyawan
    2.Tampilkan tabel database karyawan
    3.Delete Karyawan
    4.Tampilkan tabel history
    5.Tampilkan tabel barang
    6.Ambil Barang
    7.Tambah Stok Barang
    8.Tambah Barang
    9.Exit""".format(nama))

    @staticmethod
    def printKmenu(nama):
        print("""Selamat Datang {}, Berikut adalah menu yang tersedia:
    1.Tampilkan tabel history
    2.Tampilkan tabel barang
    3.Ambil Barang
    4.Tambah Stok Barang
    5.Tambah Barang
    6.Exit

Jawab : """.format(nama))