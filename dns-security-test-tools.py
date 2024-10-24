#!/usr/bin/env python3
import dns.resolver
import dns.zone
import dns.query
import socket
import sys
import subprocess
import threading
import time
import logging
from datetime import datetime
import os
from colorama import Fore, Back, Style, init

# Colorama'yı başlat
init(autoreset=True)

class DNSSecurityTester:
  def __init__(self):
      self.domain = None
      self.nameservers = []
      self.results = {}

  def clear_screen(self):
      """Ekranı temizle"""
      os.system('cls' if os.name == 'nt' else 'clear')

  def print_banner(self):
      """Program başlığını göster"""
      banner = """
╔══════════════════════════════════════════════════════════════╗
║           DNS GÜVENLİK // DNS SECURITY TEST TOOL             ║
║          *****************************************           ║
║              Created by: [Emre Çağlar YILDIZ]                ║
║                    Version: 1.0.0                            ║
╚══════════════════════════════════════════════════════════════╝
      """
      print(Fore.CYAN + banner)

  def print_menu(self):
      """Ana menüyü göster"""
      menu = """
[1] Tüm Testleri Çalıştır
[2] Zone Transfer Testi
[3] DNSSEC Kontrolü
[4] Recursive Sorgu Testi
[5] DNS Versiyon Kontrolü
[6] Rate Limiting Testi
[7] DNS Kayıt Kontrolü
[8] Rapor Oluştur
[9] Çıkış

Seçiminiz: """
      return input(Fore.GREEN + menu)

  def get_domain(self):
      """Kullanıcıdan domain adı al"""
      while True:
          self.domain = input(Fore.YELLOW + "\nTest edilecek alan adını girin: ").strip()
          if self.domain:
              return True
          print(Fore.RED + "Geçerli bir alan adı girmelisiniz!")

  def get_nameservers(self):
      """Domain'in NS kayıtlarını al"""
      try:
          print(Fore.CYAN + "\nNS sunucuları alınıyor...")
          ns_records = dns.resolver.resolve(self.domain, 'NS')
          self.nameservers = [str(ns) for ns in ns_records]
          print(Fore.GREEN + f"Bulunan NS sunucuları: {', '.join(self.nameservers)}")
          return True
      except Exception as e:
          print(Fore.RED + f"Hata: NS kayıtları alınamadı - {str(e)}")
          return False

  def test_zone_transfer(self):
      """Zone transfer testi"""
      if not self.nameservers:
          if not self.get_nameservers():
              return
      
      print(Fore.CYAN + "\nZone Transfer testi yapılıyor...")
      results = []
      for ns in self.nameservers:
          try:
              ns_ip = socket.gethostbyname(ns)
              z = dns.zone.from_xfr(dns.query.xfr(ns_ip, self.domain))
              records = [str(name) for name in z.nodes.keys()]
              results.append({
                  'nameserver': ns,
                  'status': 'Vulnerable',
                  'records': records
              })
              print(Fore.RED + f"[!] Zone Transfer Açığı: {ns}")
          except Exception:
              results.append({
                  'nameserver': ns,
                  'status': 'Protected',
                  'records': []
              })
              print(Fore.GREEN + f"[+] Zone Transfer Korumalı: {ns}")
      
      input(Fore.YELLOW + "\nDevam etmek için Enter'a basın...")
      return results

  def check_dnssec(self):
      """DNSSEC kontrolü"""
      print(Fore.CYAN + "\nDNSSEC kontrolü yapılıyor...")
      try:
          answer = dns.resolver.resolve(self.domain, 'DNSKEY')
          print(Fore.GREEN + "[+] DNSSEC aktif")
          input(Fore.YELLOW + "\nDevam etmek için Enter'a basın...")
          return True
      except Exception:
          print(Fore.RED + "[-] DNSSEC pasif")
          input(Fore.YELLOW + "\nDevam etmek için Enter'a basın...")
          return False

  def check_recursive_query(self):
      """Recursive sorgu kontrolü"""
      if not self.nameservers:
          if not self.get_nameservers():
              return
      
      print(Fore.CYAN + "\nRecursive sorgu testi yapılıyor...")
      results = []
      for ns in self.nameservers:
          try:
              resolver = dns.resolver.Resolver()
              resolver.nameservers = [socket.gethostbyname(ns)]
              resolver.query('google.com', 'A')
              results.append({
                  'nameserver': ns,
                  'status': 'Vulnerable'
              })
              print(Fore.RED + f"[!] Recursive sorgu açık: {ns}")
          except Exception:
              results.append({
                  'nameserver': ns,
                  'status': 'Protected'
              })
              print(Fore.GREEN + f"[+] Recursive sorgu kapalı: {ns}")
      
      input(Fore.YELLOW + "\nDevam etmek için Enter'a basın...")
      return results

  def check_version(self):
      """DNS versiyon bilgisi kontrolü"""
      if not self.nameservers:
          if not self.get_nameservers():
              return
      
      print(Fore.CYAN + "\nDNS versiyon kontrolü yapılıyor...")
      results = []
      for ns in self.nameservers:
          try:
              resolver = dns.resolver.Resolver()
              resolver.nameservers = [socket.gethostbyname(ns)]
              answer = resolver.query('version.bind', 'TXT', 'CH')
              version = str(answer[0])
              results.append({
                  'nameserver': ns,
                  'version': version,
                  'status': 'Vulnerable'
              })
              print(Fore.RED + f"[!] Versiyon bilgisi açık: {ns} - {version}")
          except Exception:
              results.append({
                  'nameserver': ns,
                  'version': 'Hidden',
                  'status': 'Protected'
              })
              print(Fore.GREEN + f"[+] Versiyon bilgisi gizli: {ns}")
      
      input(Fore.YELLOW + "\nDevam etmek için Enter'a basın...")
      return results

  def test_rate_limiting(self):
      """Rate limiting testi"""
      if not self.nameservers:
          if not self.get_nameservers():
              return
      
      print(Fore.CYAN + "\nRate limiting testi yapılıyor...")
      results = []
      for ns in self.nameservers:
          try:
              start_time = time.time()
              success_count = 0
              total_queries = 100

              for _ in range(total_queries):
                  try:
                      resolver = dns.resolver.Resolver()
                      resolver.nameservers = [socket.gethostbyname(ns)]
                      resolver.query(f"test{_}.{self.domain}", 'A')
                      success_count += 1
                      print(Fore.CYAN + f"\rSorgular: {success_count}/{total_queries}", end='')
                  except Exception:
                      pass

              duration = time.time() - start_time
              qps = success_count / duration

              results.append({
                  'nameserver': ns,
                  'qps': qps,
                  'status': 'Protected' if qps < 50 else 'Vulnerable'
              })
              print(Fore.GREEN + f"\n[+] Rate limiting testi: {ns} - {qps:.2f} QPS")
          except Exception as e:
              results.append({
                  'nameserver': ns,
                  'qps': 0,
                  'status': 'Error'
              })
              print(Fore.RED + f"\n[-] Rate limiting test hatası: {ns} - {str(e)}")
      
      input(Fore.YELLOW + "\nDevam etmek için Enter'a basın...")
      return results

  def check_record_consistency(self):
      """DNS kayıt tutarlılığı kontrolü"""
      print(Fore.CYAN + "\nDNS kayıt kontrolü yapılıyor...")
      record_types = ['A', 'AAAA', 'MX', 'NS', 'SOA', 'TXT']
      results = {}
      
      for record_type in record_types:
          try:
              answers = dns.resolver.resolve(self.domain, record_type)
              results[record_type] = [str(rdata) for rdata in answers]
              print(Fore.GREEN + f"[+] {record_type} kayıtları bulundu: {len(results[record_type])}")
              for record in results[record_type]:
                  print(Fore.CYAN + f"  - {record}")
          except Exception:
              results[record_type] = []
              print(Fore.YELLOW + f"[-] {record_type} kaydı bulunamadı")
      
      input(Fore.YELLOW + "\nDevam etmek için Enter'a basın...")
      return results

  def generate_report(self):
      """Test sonuçlarını raporla"""
      if not self.results:
          print(Fore.RED + "\nHenüz test sonucu bulunmuyor!")
          input(Fore.YELLOW + "\nDevam etmek için Enter'a basın...")
          return

      report_file = f"dns_security_report_{self.domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
      
      with open(report_file, 'w') as f:
          f.write(f"""
DNS Güvenlik Testi Raporu
Domain: {self.domain}
Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*50}
""")
          
          for test_name, results in self.results.items():
              f.write(f"\n{test_name.upper()} Sonuçları:\n")
              if isinstance(results, list):
                  for result in results:
                      f.write(f"  {result}\n")
              elif isinstance(results, dict):
                  for key, value in results.items():
                      f.write(f"  {key}: {value}\n")
              else:
                  f.write(f"  {results}\n")

      print(Fore.GREEN + f"\nRapor oluşturuldu: {report_file}")
      input(Fore.YELLOW + "\nDevam etmek için Enter'a basın...")

  def run_all_tests(self):
      """Tüm testleri çalıştır"""
      if not self.get_nameservers():
          return

      self.results['zone_transfer'] = self.test_zone_transfer()
      self.results['dnssec'] = self.check_dnssec()
      self.results['recursive_query'] = self.check_recursive_query()
      self.results['version'] = self.check_version()
      self.results['rate_limiting'] = self.test_rate_limiting()
      self.results['records'] = self.check_record_consistency()
      
      self.generate_report()

def main():
  tester = DNSSecurityTester()
  
  while True:
      tester.clear_screen()
      tester.print_banner()
      
      choice = tester.print_menu()
      
      if choice == '9':
          print(Fore.YELLOW + "\nProgramdan çıkılıyor...")
          break
          
      if not tester.domain and choice != '9':
          if not tester.get_domain():
              continue

      if choice == '1':
          tester.run_all_tests()
      elif choice == '2':
          tester.results['zone_transfer'] = tester.test_zone_transfer()
      elif choice == '3':
          tester.results['dnssec'] = tester.check_dnssec()
      elif choice == '4':
          tester.results['recursive_query'] = tester.check_recursive_query()
      elif choice == '5':
          tester.results['version'] = tester.check_version()
      elif choice == '6':
          tester.results['rate_limiting'] = tester.test_rate_limiting()
      elif choice == '7':
          tester.results['records'] = tester.check_record_consistency()
      elif choice == '8':
          tester.generate_report()

if __name__ == "__main__":
  try:
      main()
  except KeyboardInterrupt:
      print(Fore.RED + "\n\nProgram kullanıcı tarafından sonlandırıldı!")
  except Exception as e:
      print(Fore.RED + f"\n\nBeklenmeyen hata: {str(e)}")
