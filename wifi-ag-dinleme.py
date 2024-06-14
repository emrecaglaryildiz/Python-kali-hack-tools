from scapy.all import *

def sniff_wifi(packet):
    if packet.haslayer(Dot11):
        print(f"SSID: {packet.info}, BSSID: {packet.addr2}")

sniff(iface="wlan0mon", prn=sniff_wifi)  # "wlan0mon" monitör modunda olmalıdır
