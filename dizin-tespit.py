import requests

def dir_bruteforce(url, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            directory = line.strip()
            full_url = f"{url}/{directory}"
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"Found directory: {full_url}")

url = "http://example.com"
wordlist = "directories.txt"  # Dizin listesi dosya yolu
dir_bruteforce(url, wordlist)
