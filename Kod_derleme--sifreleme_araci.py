#!/usr/bin/env python

import os
import py_compile

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BHECY")
os.system("figlet PY KOD DERLEME/ŞİFRELEME ARACI")

print("""

Python Dosyaları aracına Hoş geldin...

""")

derle=input("Derlemek/şifrelemek istediğiniz kod dosyasının yolunu giriniz : ")
py_compile.compile(derle)
print("Kodu Derleme/şifreleme işlemi tamamlanmıştır.")