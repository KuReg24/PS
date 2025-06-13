import socket

def scan_ports(host, start_port, end_port):

    open_ports = []

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"port{port}: open")
            open_ports.append(port)
        s.close()

    if not open_ports:
        print("")
    else:
        print(f"open port: {len(open_ports)}")
        print(open_ports)

if __name__ == "__main__":
    scan_ports("127.0.0.1", 1, 1024)
