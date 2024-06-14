import re
import requests
from bs4 import BeautifulSoup

def email_harvest(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.get_text())
    for email in set(emails):
        print(f"Found email: {email}")

url = "http://example.com"
email_harvest(url)
