import socket
import threading

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        print(f"Port {port} is open")
    except:
        pass
    finally:
        s.close()

ip = "192.168.1.1"  # Hedef IP adresi
for port in range(1, 1025):
    threading.Thread(target=scan_port, args=(ip, port)).start()
