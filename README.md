# Prodigy_CS_Task5
# 📡 Network Packet Analyzer 
Internship Task 5 at Prodigy InfoTech

## Overview🧐
This repository contains a Python program that implements a network packet analyzer using the Scapy library. The tool captures and analyzes network packets, displaying relevant information such as source and destination IP addresses, protocols, and payload data. This packet sniffer is intended for educational purposes and should be used ethically.

## Key Theoretical Explanations🧠
### Cybersecurity Topics🔒
1. **Packet Sniffing**📦: The process of intercepting and logging traffic that passes over a computer network.
2. **IP Packets**: Data packets that include source and destination IP addresses and protocol information.
3. **TCP/UDP Protocols**: Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) are core protocols of the Internet protocol suite.
4. **⚖️Ethical Considerations**: Ensuring that packet sniffing is conducted legally and ethically, typically in a controlled environment where monitoring is authorized.

### 🖧 Network Packets and Protocols
1. **Packets**: Small units of data transmitted over a network. Each packet contains header information (source, destination, protocol) and payload data.
2. **IP Layer**: Handles addressing and routing of packets across networks. It identifies the source and destination IP addresses.
3. **TCP/UDP Layers**: Protocols that define how data is transmitted. TCP is connection-oriented, ensuring reliable delivery, while UDP is connectionless and faster but less reliable.

## 💎Features
**IP Packet Information**: Source and destination IP addresses and protocol type.
**TCP and UDP Analysis**: Identifies TCP and UDP packets, displaying source and destination ports.

## 📌Software and Hardware Requirements
### Software
  - Python 3.x
  - Scapy library
### Hardware
- **Network Interface**: A network card capable of capturing packets.
- **Operating System**: Linux, macOS, or Windows (Linux recommended for network tasks).

## 📍Prerequisites
- Basic understanding of Python programming.
- Knowledge of network protocols (IP, TCP, UDP).
- Understanding of ethical considerations in cybersecurity.

## 🛠️ Tech Stack
- **Language**: Python
- **Libraries**: Scapy
- **IDE**: PyCharm

### ‼ Program Explanation
- **Scapy Library**: A powerful Python library used for network packet manipulation, including sniffing, crafting, and injecting packets.
- **Packet Callback Function**: Processes each packet, extracting and displaying source and destination IP addresses and protocol information.

## Steps to Execute the Program 🧩
1. **Clone the Repository**: 
   ```sh
   git clone https://github.com/mrudula0003/Prodigy_CS_Task5
   ```
2. **Navigate to the Project Directory**:
   ```sh
   cd Prodigy_CS_Task5
   ```
3. **Install Required Libraries**:
   ```sh
   pip install scapy
   ```
4. **Run the Program**:
   ```sh
   python packet_analyzer.py
   ```

## 🕹️Usage
Ensure you have the necessary permissions to capture network packets in your environment. Run the script and monitor the terminal for output on captured packets.

## ⚖️ Ethical Considerations
- **Educational Use Only**: This tool is intended for educational and research purposes. Always obtain proper authorization before monitoring network traffic.
- **Compliance with Laws**: Ensure compliance with local laws and regulations regarding network monitoring and data privacy.

## Acknowledgments 🙌
Thanks to the developers of the Scapy library for providing such a powerful tool for network analysis.

## Contact 📩
For any queries or support, contact mrudulakhedkar74@gmail.com

---
### Thanks & Contribute ✨
Special thanks to Prodigy Info Tech for the opportunity to work on this project. 
Your feedback and contributions are welcome. Please ensure your contributions align with ethical guidelines for cybersecurity tools.
Check out the repository and feel free to raise issues or submit pull requests.
