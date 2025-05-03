# networking/ping.py

import socket
from colorama import Fore


def tcp_ping(host: str, port: int = 443, timeout: float = 2.0) -> str:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((host, port))
            return f"{Fore.GREEN}✅ {host}:{port} is alive (TCP connect succeeded)"
    except (socket.timeout, ConnectionRefusedError):
        return f"{Fore.YELLOW}⚠️ {host}:{port} is reachable but refused connection"
    except socket.gaierror:
        return f"{Fore.RED}❌ Invalid host: {host}"
    except Exception as e:
        return f"{Fore.RED}❌ {host}:{port} is unreachable ({e})"
