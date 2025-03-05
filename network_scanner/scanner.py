from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp

def scan_network(ip_range):
    arp_request = ARP(pdst=ip_range)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether_frame / arp_request

    answered, _ = srp(packet, timeout=2, verbose=False)

    devices = []
    for sent, received in answered:
        devices.append({"IP": received.psrc, "MAC": received.hwsrc})

    return devices
