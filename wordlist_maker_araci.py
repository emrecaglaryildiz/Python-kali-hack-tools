#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BHECY")
os.system("figlet WORDLIST ARACI")

print("""

Wordlist Oluşturma aracına Hoş geldin...

""")

minimum=input("minimum karakter sayısı : ")
maximum=input("maximum karakter sayısı : ")
karakter=input("kullanılacak karakterleri giriniz : ")
kayityeri=input("kayıt yerinin yolunu giriniz : ")

os.system("chrunch "+minimum+" "+maximum+" "+karakter+" -o "+kayityeri)

print("İşlemler başarıyla tamamlandı...")