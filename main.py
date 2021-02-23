from geometry.bangun_ruang import BangunRuang
from geometry.persegipanjang import PersegiPanjang
from geometry.segitiga import Segitiga

print('menggunakan OOP')
p11 = PersegiPanjang(10, 3)
print(p11.info())
print(p11.hitung_luas())

s12 = Segitiga(10,3)
print (s12.info())
print(s12.hitung_luas())

print('\nMencoba membuat object dari kelas BangunRuang')
b11 = BangunRuang()
print(b11.info())
print(b11.hitung_luas())

#Polymorphism : kememapuan object untuk merespon berbeda,terhadap pemanggilan method yang sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p11)
daftar_bangun_ruang.append(s12)

print('\nPolymorphism')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())

