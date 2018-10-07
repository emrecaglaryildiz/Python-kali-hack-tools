#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BHECY")
os.system("figlet GUVENLIK DUVARI TESPIT")

print("""
GUVENLIK DUVARI TESPIT aracina HosGeldiniz !
 """)
 
 site=input("Site adresi ya da ip giriniz : ")
 os.system("wafw00f "+site)