from geometry.bangun_ruang import BangunRuang


class Segitiga(BangunRuang):
    def __init__(self, a, t):
        # funsi ynag dipanggil pertama kali saat object diciptakan
        self.a = a
        self.t = t


    def info(self):
        return f'ini adalah object dari segitiga dengan alas = {self.a} dan tinggi = {self.t}'


    def hitung_luas(self):
        return f'hasilnya = {self.a * self.t / 2}'

