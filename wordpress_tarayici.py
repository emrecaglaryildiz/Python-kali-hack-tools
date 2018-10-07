#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BHECY")
os.system("figlet WORDPRESS TARAMA")

print("""

WORDPRESS TARAMA aracına Hoş Geldin...

1) Hızlı Tarama
2) Eklenti Tarama
3) Tema Tarama
4) Yönetici Kullanıcı Adı Tarama

""")

islemno=input("İşlem numarası giriniz : ")

if islemno=="1"
	site=input("site adresi : ")
	os.system("wpscan --url "+site)
elif islemno=="2"
	site=input("site adresi : ")
	os.system("wpscan --url "+site+" --enumerate p")
elif islemno=="3"
	site=input("site adresi : ")
	os.system("wpscan --url "+site+" --enumerate t")
elif islemno=="2"
	site=input("site adresi : ")
	os.system("wpscan --url "+site+" --enumerate u")
else:
	print("Yanlış seçim, program kapandı...")



