#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BHECY")
os.system("figlet SITE BILGI TOPLAMA ARACI")

print("""

Hedef Site Bilgi Toplama aracına Hoş geldin...

""")

adress=input("incelemek istediğiniz site/ip adresini giriniz : ")

print("--- SONUCLAR --- ")

os.system("theharvester -d "+adress+" -l 1000 -b all")