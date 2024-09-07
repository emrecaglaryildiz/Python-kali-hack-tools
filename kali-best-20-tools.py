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

# ... (Diğer fonksiyonlar aynı kalacak)

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
      print("\nKali Linux Araçları Menüsü:")
      for key, value in tools.items():
          print(f"{key}. {value[0]}")
      
      choice = input("Seçiminizi yapın (1-20): ")
      
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
print("kali_tools_extended_script.py")
