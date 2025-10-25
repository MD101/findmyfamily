import socket
import struct
import time
import os

def checksum(source_string):
    """
    Calculates the Internet checksum for a given string of bytes.
    """
    sum_val = 0
    count_to = (len(source_string) // 2) * 2
    for count in range(0, count_to, 2):
        this_val = source_string[count + 1] * 256 + source_string[count]
        sum_val = sum_val + this_val
    if count_to < len(source_string):
        sum_val = sum_val + source_string[len(source_string) - 1]
    sum_val = (sum_val >> 16) + (sum_val & 0xffff)
    sum_val = sum_val + (sum_val >> 16)
    answer = ~sum_val & 0xffff
    return answer

def create_packet(id_val):
    """
    Creates an ICMP Echo Request packet.
    """
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    icmp_type = 8  # Echo Request
    icmp_code = 0
    icmp_checksum = 0
    icmp_id = id_val & 0xFFFF  # Ensure it fits in 16 bits
    icmp_sequence = 1

    # Payload (optional)
    payload = b'Python Ping Payload'

    # Pack the ICMP header without checksum first
    header = struct.pack("bbHHh", icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_sequence)

    # Calculate checksum with a dummy checksum of 0
    icmp_checksum = checksum(header + payload)

    # Repack the header with the correct checksum
    header = struct.pack("bbHHh", icmp_type, icmp_code, socket.htons(icmp_checksum), icmp_id, icmp_sequence)

    return header + payload

def send_ping(dest_addr, timeout=1):
    """
    Sends an ICMP Echo Request and attempts to receive an Echo Reply.
    """
    try:
        # Create a raw socket for ICMP
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    except socket.error as e:
        if e.errno == 1:
            print("Operation not permitted. You need root/administrator privileges to create raw sockets.")
            return

    packet_id = os.getpid() & 0xFFFF
    packet = create_packet(packet_id)

    s.settimeout(timeout)
    s.sendto(packet, (dest_addr, 1))  # The '1' is a dummy port for raw sockets

    start_time = time.time()
    try:
        while True:
            # Receive the response
            rec_packet, addr = s.recvfrom(1024)
            time_received = time.time()

            # Unpack the IP header (first 20 bytes)
            ip_header = rec_packet[:20]
            iph = struct.unpack("!BBHHHBBH4s4s", ip_header)
            
            # Extract ICMP part (after IP header)
            icmp_header = rec_packet[20:28]
            icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_sequence = struct.unpack("bbHHh", icmp_header)

            if icmp_type == 0 and icmp_id == packet_id:  # Echo Reply and matching ID
                rtt = (time_received - start_time) * 1000  # Round Trip Time in ms
                print(f"Reply from {addr[0]}: time={rtt:.2f}ms")
                break
            elif time.time() - start_time > timeout:
                print("Request timed out.")
                break
    except socket.timeout:
        print("Request timed out.")
    finally:
        s.close()

# Example usage:
if __name__ == "__main__":
    target_host = "8.8.8.8"  # Google DNS server
    print(f"Pinging {target_host}...")
    send_ping(target_host)