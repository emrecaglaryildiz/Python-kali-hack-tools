import requests

def subdomain_enum(domain, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            subdomain = line.strip()
            url = f"http://{subdomain}.{domain}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"Found subdomain: {url}")
            except requests.ConnectionError:
                pass

domain = "example.com"
wordlist = "subdomains.txt"
subdomain_enum(domain, wordlist)
