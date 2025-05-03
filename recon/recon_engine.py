# recon/recon_engine.py

import socket
import whois
from .ports import scan_ports
from .fingerprint import get_tech_stack
from .subdomains import enumerate_subdomains
from colorama import init, Fore, Style

# Init colorama
init(autoreset=True)


def get_ip(domain: str) -> str:
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return "Unable to resolve domain."


def get_whois_info(domain: str) -> str:
    try:
        w = whois.whois(domain)
        return str(w)
    except Exception as e:
        return f"{Fore.RED}WHOIS lookup failed: {e}"


def run_recon(domain: str):
    print(f"\n{Fore.CYAN}🔍 Starting Recon on: {Fore.YELLOW}{domain}\n")
    
    ip = get_ip(domain)
    print(f"{Fore.BLUE}🌐 IP Address: {Fore.GREEN}{ip}")

    if ip != "Unable to resolve domain.":
        open_ports = scan_ports(ip)
        port_str = ", ".join(str(p) for p in open_ports) if open_ports else "None"
        print(f"\n{Fore.MAGENTA}🚪 Open Ports Found: {Fore.GREEN}{port_str}")
    else:
        open_ports = []

    print(f"\n{Fore.YELLOW}🧱 Technology Stack Fingerprint:")
    for tech in get_tech_stack(domain):
        print(f"   - {Fore.CYAN}{tech}")

    print(f"\n{Fore.YELLOW}📄 WHOIS Info:")
    print(get_whois_info(domain))

    print(f"\n{Fore.YELLOW}🔎 Subdomains Found:")
    subdomains = enumerate_subdomains(domain)
    if subdomains:
        for sub, ip in subdomains:
            print(f"   - {Fore.GREEN}{sub} → {Fore.BLUE}{ip}")
    else:
        print(f"{Fore.RED}   - No subdomains found or wordlist missing.")
