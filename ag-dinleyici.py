from scapy.all import *

def packet_sniffer(packet):
    if packet.haslayer(IP):
        print(f"Packet: {packet.summary()}")

sniff(prn=packet_sniffer, count=10)
