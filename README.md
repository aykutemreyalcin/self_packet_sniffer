# Packet Sniffer in Python

## Overview

This Python script is a basic **packet sniffer** that captures and analyzes Ethernet frames. It extracts source and destination MAC addresses along with the protocol type from incoming network packets.

## How It Works

1. Creates a raw socket to capture network packets.
2. Extracts Ethernet frame headers, including:
   - Destination MAC address
   - Source MAC address
   - Protocol type
3. Continuously listens for packets and prints extracted data.

### Requirements

- Python 3.x
- Must be run with **root** privileges (on Linux)

### Running the script

```sh
sudo python packet_sniffer.py
```

### Expected Output

```
Ethernet Frame:
Destination: AA:BB:CC:DD:EE:FF, Source: 11:22:33:44:55:66, Protocol: 8
```

## Notes

- This script works **only on Linux** due to the use of `AF_PACKET` sockets.
- Requires **sudo/root** privileges to access raw network packets.
- Can be further expanded to parse IP headers, TCP/UDP packets, etc.
