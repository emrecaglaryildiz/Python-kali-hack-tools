#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BHECY")
os.system("figlet PORT TARAMA")

print("""
1) Hızlı Port Tarama
2) Servis ve Versiyon bilgisi
3) Isletim Sistemi Bilgisi
""")

islemno=input("Islem Numarası giriniz : ")

if islemno=="1":
	hedefip=input("Hedef ip giriniz : ")
	os.system("nmap "+hedefip)
elif islemno=="2":
	hedefip=input("Hedef ip giriniz : ")
	os.system("nmap -sS -sV "+hedefip)
elif islemno=="3":
	hedefip=input("Hedef ip giriniz : ")
	os.system("nmap -0 "+hedefip)
else:
	print("Yanlış tuşa bastınız...")