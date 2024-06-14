import ssl
import socket

def check_ssl_cert(domain):
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
            print(f"Issuer: {cert['issuer']}")
            print(f"Subject: {cert['subject']}")
            print(f"Expiry Date: {cert['notAfter']}")

domain = "example.com"
check_ssl_cert(domain)
