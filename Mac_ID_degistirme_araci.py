#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BHECY")
os.system("figlet MAC ID DEGISTIRME ARACI")

print("""

Mac ID Değiştirme aracı aracına Hoş geldin...

""")

agbag=input("Ag bagdastirici adi : ")
os.system("ifconfig "+agbag+" "+"down")
os.system("macchanger -r "+agbag)
os.system("ifconfig "+agbag+" "+"up")

print("\033[92mMac id değişitirildi.")