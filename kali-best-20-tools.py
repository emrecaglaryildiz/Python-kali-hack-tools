import os
import subprocess

def print_banner():
  banner = """                                                      
  ██████╗ ██╗   ██╗    ███████╗███╗   ███╗██████╗ ███████╗ ██████╗██╗   ██╗
  ██╔══██╗╚██╗ ██╔╝    ██╔════╝████╗ ████║██╔══██╗██╔════╝██╔════╝╚██╗ ██╔╝
  ██████╔╝ ╚████╔╝     █████╗  ██╔████╔██║██████╔╝█████╗  ██║      ╚████╔╝ 
  ██╔══██╗  ╚██╔╝      ██╔══╝  ██║╚██╔╝██║██╔══██╗██╔══╝  ██║       ╚██╔╝  
  ██████╔╝   ██║       ███████╗██║ ╚═╝ ██║██║  ██║███████╗╚██████╗   ██║   
  ╚═════╝    ╚═╝       ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝   ╚═╝   
  """
  print(banner)

def run_command(command):
  try:
      result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
      print(result.stdout)
  except subprocess.CalledProcessError as e:
      print(f"Hata oluştu: {e}")
      print(e.output)

def nmap_scan():
  target = input("Tarama yapılacak hedef IP veya alan adını girin: ")
  run_command(f"nmap -sV {target}")

def metasploit_console():
  print("Metasploit Console başlatılıyor...")
  os.system("msfconsole")

def aircrack_ng():
  interface = input("Kullanılacak kablosuz arayüzü girin (örn. wlan0): ")
  run_command(f"airmon-ng start {interface}")
  run_command(f"airodump-ng {interface}mon")

def sqlmap():
  url = input("Hedef URL'yi girin: ")
  run_command(f"sqlmap -u {url} --dbs")

def john_the_ripper():
  password_file = input("Şifre dosyasının yolunu girin: ")
  run_command(f"john {password_file}")

def wireshark():
  interface = input("Dinlenecek arayüzü girin (örn. eth0): ")
  run_command(f"wireshark -i {interface}")

def hydra():
  target = input("Hedef IP veya alan adını girin: ")
  service = input("Hedef servisi girin (örn. ssh, ftp): ")
  username = input("Kullanıcı adını girin: ")
  wordlist = input("Wordlist dosyasının yolunu girin: ")
  run_command(f"hydra -l {username} -P {wordlist} {target} {service}")

def nikto():
  target = input("Tarama yapılacak hedef URL'yi girin: ")
  run_command(f"nikto -h {target}")

def burp_suite():
  print("Burp Suite başlatılıyor...")
  run_command("burpsuite")

def dirb():
  target = input("Tarama yapılacak hedef URL'yi girin: ")
  wordlist = input("Wordlist dosyasının yolunu girin (varsayılan için boş bırakın): ")
  if wordlist:
      run_command(f"dirb {target} {wordlist}")
  else:
      run_command(f"dirb {target}")

def maltego():
  print("Maltego başlatılıyor...")
  run_command("maltego")

def beef():
  print("BeEF başlatılıyor...")
  run_command("beef-xss")

def hashcat():
  hash_file = input("Hash dosyasının yolunu girin: ")
  wordlist = input("Wordlist dosyasının yolunu girin: ")
  hash_type = input("Hash tipini girin (örn. 0 for MD5): ")
  run_command(f"hashcat -m {hash_type} -a 0 {hash_file} {wordlist}")

def netcat():
  action = input("Dinleme (l) veya bağlanma (c)? ")
  port = input("Port numarası girin: ")
  if action.lower() == 'l':
      run_command(f"nc -lvp {port}")
  elif action.lower() == 'c':
      host = input("Bağlanılacak host'u girin: ")
      run_command(f"nc {host} {port}")

def recon_ng():
  print("Recon-ng başlatılıyor...")
  run_command("recon-ng")

def set_toolkit():
  print("Social-Engineer Toolkit başlatılıyor...")
  run_command("setoolkit")

def wpscan():
  target = input("Tarama yapılacak WordPress sitesinin URL'sini girin: ")
  run_command(f"wpscan --url {target}")

def ettercap():
  interface = input("Kullanılacak arayüzü girin (örn. eth0): ")
  run_command(f"ettercap -G -i {interface}")

def responder():
  interface = input("Kullanılacak arayüzü girin (örn. eth0): ")
  run_command(f"responder -I {interface}")
  
def main_menu():
  print_banner()  # Banner'ı yazdır
  tools = {
      1: ("Nmap Taraması", nmap_scan),
      2: ("Metasploit Console", metasploit_console),
      3: ("Aircrack-ng", aircrack_ng),
      4: ("SQLMap", sqlmap),
      5: ("John the Ripper", john_the_ripper),
      6: ("Wireshark", wireshark),
      7: ("Hydra", hydra),
      8: ("Nikto", nikto),
      9: ("Burp Suite", burp_suite),
      10: ("Dirb", dirb),
      11: ("Maltego", maltego),
      12: ("BeEF", beef),
      13: ("Hashcat", hashcat),
      14: ("Netcat", netcat),
      15: ("Recon-ng", recon_ng),
      16: ("SET (Social-Engineer Toolkit)", set_toolkit),
      17: ("WPScan", wpscan),
      18: ("Ettercap", ettercap),
      19: ("Responder", responder),
      20: ("Çıkış", None)
  }

  while True:
      print("\nKali Linux Araçları :")
      for key, value in tools.items():
          print(f"{key}. {value[0]}")
      
      choice = input("Seçimi yapın (1-20): ")
      
      if choice.isdigit() and 1 <= int(choice) <= 20:
          choice = int(choice)
          if choice == 20:
              print("Programdan çıkılıyor...")
              break
          else:
              tools[choice][1]()
      else:
          print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
  if os.geteuid() != 0:
      print("Bu script'in root yetkisiyle çalıştırılması gerekmektedir.")
      exit(1)
  main_menu()

# Created/Modified files during execution:
print("kali_tools_byEmreCY_script.py")
