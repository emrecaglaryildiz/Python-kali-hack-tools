import requests

def xss_scanner(url, payloads):
    for payload in payloads:
        target_url = f"{url}?q={payload}"
        response = requests.get(target_url)
        if payload in response.text:
            print(f"Possible XSS vulnerability at: {target_url}")

url = "http://example.com/search"
payloads = ["<script>alert('XSS')</script>", "'><script>alert('XSS')</script>"]
xss_scanner(url, payloads)
