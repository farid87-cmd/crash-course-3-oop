from geometry.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    #fungsi __init__adalah fungsi khusus untuk memberikan value
    def __init__(self, p, l):
        # funsi ynag dipanggil pertama kali saat object diciptakan
        self.p = p
        self.l = l


    def info(self):
        return f'ini adalah object dari persegi panjang dengan panjang = {self.p} dan lebar = {self.l}'


    def hitung_luas(self):
        return f'hasilnya = {self.p * self.l}'

