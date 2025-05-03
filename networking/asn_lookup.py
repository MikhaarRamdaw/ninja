# networking/asn_lookup.py

import requests
from colorama import Fore


def lookup_asn(ip: str) -> str:
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        data = response.json()

        org = data.get("org", "Unknown ASN")
        city = data.get("city", "Unknown City")
        country = data.get("country", "Unknown Country")
        hostname = data.get("hostname", "N/A")

        return (
            f"{Fore.CYAN}ASN/Org: {Fore.GREEN}{org}\n"
            f"{Fore.CYAN}Hostname: {Fore.GREEN}{hostname}\n"
            f"{Fore.CYAN}Location: {Fore.GREEN}{city}, {country}"
        )

    except Exception as e:
        return f"{Fore.RED}ASN lookup failed: {e}"
