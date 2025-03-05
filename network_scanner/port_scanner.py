import socket

def scan_ports(ip, ports=None):
    if ports is None:
        ports = [22, 80, 443, 3389]  # Define default ports inside the function

    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))  # 0 means open
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports
