# recon/ports.py

import socket
from concurrent.futures import ThreadPoolExecutor


COMMON_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445,
    993, 995, 1723, 3306, 3389, 5900, 8080, 8443
]


def scan_port(host: str, port: int, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            if result == 0:
                return port
    except:
        pass
    return None


def scan_ports(host: str, ports=COMMON_PORTS):
    open_ports = []
    print(f"\n🔎 Scanning ports on {host}...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(host, p), ports)

    for port in results:
        if port:
            open_ports.append(port)

    return open_ports
