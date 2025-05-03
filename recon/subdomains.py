# recon/subdomains.py

import socket


def enumerate_subdomains(domain: str, wordlist_path: str = "wordlists/common.txt"):
    found = []

    try:
        with open(wordlist_path, "r") as f:
            sub_names = [line.strip() for line in f if line.strip()]

        print(f"\n🌐 Enumerating subdomains for: {domain}")

        for name in sub_names:
            subdomain = f"{name}.{domain}"
            try:
                ip = socket.gethostbyname(subdomain)
                found.append((subdomain, ip))
            except socket.gaierror:
                continue

    except FileNotFoundError:
        print("❌ Wordlist file not found.")
    
    return found
