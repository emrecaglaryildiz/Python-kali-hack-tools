import requests

def analyze_http_headers(url):
    response = requests.get(url)
    headers = response.headers
    for header, value in headers.items():
        print(f"{header}: {value}")
    if 'X-Frame-Options' not in headers:
        print("Missing X-Frame-Options header. Possible Clickjacking vulnerability.")
    if 'Content-Security-Policy' not in headers:
        print("Missing Content-Security-Policy header. Possible XSS vulnerability.")

url = "http://example.com"
analyze_http_headers(url)
