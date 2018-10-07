#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BHECY")
os.system("figlet VPN KONTROL ARACI")

print("""

Vpn kontrol aracı aracına Hoş geldin...

""")

hedefip=input("Hedef ip : ")
os.system("ike-scan "+hedefip)
