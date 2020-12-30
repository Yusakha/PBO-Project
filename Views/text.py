import os

class View:
    @staticmethod
    def clear():
        os.system('cls')
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
    def errors(arg):
        print("Ada yang Error :\n{}".format(arg))