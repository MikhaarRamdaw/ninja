# networking/dns_records.py

import dns.resolver
from colorama import Fore


def fetch_dns_records(domain: str) -> list:
    record_types = ["A", "MX", "TXT", "NS", "CNAME"]
    results = []

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype, raise_on_no_answer=False)
            for rdata in answers:
                results.append(f"{Fore.CYAN}{rtype}: {Fore.GREEN}{rdata}")
        except dns.resolver.NoAnswer:
            continue
        except Exception as e:
            results.append(f"{Fore.RED}{rtype} lookup failed: {e}")
    
    return results
