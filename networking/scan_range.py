# networking/scan_range.py

import ipaddress
import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore


def is_alive(ip: str, port: int = 443, timeout: float = 1.0) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            return True
    except:
        return False


def scan_cidr_range(cidr: str, port: int = 443, max_threads: int = 100) -> list:
    try:
        network = ipaddress.IPv4Network(cidr, strict=False)
    except ValueError as e:
        return [f"{Fore.RED}Invalid CIDR: {cidr} ({e})"]

    live_hosts = []

    def scan(ip):
        if is_alive(str(ip), port):
            print(f"{Fore.GREEN}✅ {ip} is alive on port {port}")
            live_hosts.append(str(ip))

    print(f"{Fore.CYAN}🔍 Scanning {cidr} on TCP port {port}...\n")

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(scan, network.hosts())

    if not live_hosts:
        print(f"{Fore.YELLOW}No live hosts found on port {port} in range {cidr}")

    return live_hosts
