# recon/recon_engine.py

import socket
import whois
from .ports import scan_ports
from .fingerprint import get_tech_stack


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
        return f"WHOIS lookup failed: {e}"


def run_recon(domain: str):
    print(f"\n🔍 Starting Recon on: {domain}\n")
    
    ip = get_ip(domain)
    print(f"🌐 IP Address: {ip}")

    if ip != "Unable to resolve domain.":
        open_ports = scan_ports(ip)
        print(f"\n🚪 Open Ports Found: {open_ports}")
    else:
        open_ports = []

    print(f"\n🧱 Technology Stack Fingerprint:")
    for tech in get_tech_stack(domain):
        print(f"   - {tech}")

    print("\n📄 WHOIS Info:")
    print(get_whois_info(domain))
