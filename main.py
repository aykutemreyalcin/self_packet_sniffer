import socket

def get_mac_address(byte_address):
    return ':'.join(f'{byte:02x}' for byte in byte_address).upper()

def parse_ethernet_frame(data):
    dest_mac = get_mac_address(data[0:6])  # First 6 bytes: Destination MAC
    src_mac = get_mac_address(data[6:12])  # Next 6 bytes: Source MAC
    proto = int.from_bytes(data[12:14], 'big')  # Next 2 bytes: Protocol Type
    payload = data[14:]
    return dest_mac, src_mac, proto, payload

def start_sniffing():
    # Create a raw socket to listen for packets
    with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3)) as conn:
        print("Listening for network packets...")
        while True:
            raw_data, _ = conn.recvfrom(65536)  # Capture packet data
            dest_mac, src_mac, proto, _ = parse_ethernet_frame(raw_data)
            print("\nEthernet Frame:")
            print(f"Destination MAC: {dest_mac}")
            print(f"Source MAC: {src_mac}")
            print(f"Protocol: {proto}")

if __name__ == "__main__":
    start_sniffing()
