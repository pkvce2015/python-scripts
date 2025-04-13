import socket

def scan_ports(ip, start_port, end_port):
    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("\nScan cancelled by user.")
            break
        except socket.error:
            print(f"Couldn't connect to server: {ip}")
            break
    if open_ports:
        print("Open ports found:")
        for port in open_ports:
            print(f"- Port {port} is open")
    else:
        print("No open ports found in the specified range.")

def get_user_input():
    try:
        ip = input("Enter target IP address: ").strip()
        socket.inet_aton(ip)  # Validate IP format
        start_port = int(input("Enter start port: ").strip())
        end_port = int(input("Enter end port: ").strip())
        if start_port < 0 or end_port > 65535 or start_port > end_port:
            raise ValueError("Invalid port range.")
        return ip, start_port, end_port
    except socket.error:
        print("Invalid IP address.")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    return None, None, None

if __name__ == "__main__":
    ip, start_port, end_port = get_user_input()
    if ip:
        scan_ports(ip, start_port, end_port)
