#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BHECY")
os.system("figlet ZAAFİYET ANALİZİ")

print("""
Hedef zaafiyet arama aracina HosGeldiniz
 """)
 
hedefip=input("Hedef ip giriniz : ")
os.system("nikto -h "+hedefip)