# Scapy is a powerful Python library used for network packet manipulation
# including sniffing, crafting, and injecting packets.
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

# checks if the packet contains an IP layer and extracts source and destination IP addresses and protocol type.
# also checks for TCP and UDP packets.
def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # Print general information about the packet
        print(f"IP Packet:\tSource: {ip_src} ->\t\tDestination: {ip_dst}, \tProtocol: {protocol}")

        # Check for TCP packets
        if TCP in packet:
            tcp_src_port = packet[TCP].sport
            tcp_dst_port = packet[TCP].dport
            print(f"TCP Packet:\tSource: {ip_src}:{tcp_src_port} ->\t\tDestination: {ip_dst}:{tcp_dst_port}")

        # Check for UDP packets
        elif UDP in packet:
            udp_src_port = packet[UDP].sport
            udp_dst_port = packet[UDP].dport
            print(f"UDP Packet:\tSource: {ip_src}:{udp_src_port} ->\t\tDestination: {ip_dst}:{udp_dst_port}")


# Sniff packets
print("Starting packet capture. Press Ctrl+C to stop.")
# specifies the callback function to process each packet.
sniff(prn=packet_callback, store=0)
