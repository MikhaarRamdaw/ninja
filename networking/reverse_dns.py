# networking/reverse_dns.py

import socket
from colorama import Fore


def reverse_dns_lookup(ip: str) -> str:
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return f"{Fore.GREEN}{ip} → {hostname}"
    except socket.herror:
        return f"{Fore.RED}{ip} → No PTR record found"
    except Exception as e:
        return f"{Fore.RED}Reverse DNS failed: {e}"
