#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("apt-get install netdiscover")
os.system("clear")
os.system("figlet BHECY")
os.system("figlet WORDPRESS TARAMA")

print("""

Ağ İçi Cihaz tarayıcıya Hoş Geldin !

By BHECY


""")

ip=input("Tarama yapılacak ip aralığı giriniz(ör:192.168.1.0) : ")
os.system("netdiscover -r{}/24".format(ip))



