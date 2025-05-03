# cli.py

import argparse
from recon.recon_engine import run_recon
from networking.reverse_dns import reverse_dns_lookup
from networking.asn_lookup import lookup_asn
from networking.dns_records import fetch_dns_records
from networking.ping import tcp_ping
from networking.scan_range import scan_cidr_range
from colorama import init

init(autoreset=True)


def main():
    parser = argparse.ArgumentParser(description="Ninja AI - Terminal Recon Tool")
    subparsers = parser.add_subparsers(dest="command")

    # recon
    parser_recon = subparsers.add_parser("recon", help="Run full recon on domain")
    parser_recon.add_argument("domain", help="Target domain (e.g., example.com)")

    # reverse-dns (PTR)
    parser_rdns = subparsers.add_parser("ptr", help="Perform reverse DNS lookup (PTR)")
    parser_rdns.add_argument("ip", help="Target IP address (e.g., 8.8.8.8)")

    # asn lookup
    parser_asn = subparsers.add_parser("asn", help="Get ASN and ownership info for an IP")
    parser_asn.add_argument("ip", help="Target IP address")

    # dns records
    parser_dns = subparsers.add_parser("dns", help="Fetch DNS records for a domain")
    parser_dns.add_argument("domain", help="Target domain")

    # ping (TCP-based)
    parser_ping = subparsers.add_parser("ping", help="Check if a host is alive using TCP ping")
    parser_ping.add_argument("host", help="Target host or IP address")
    parser_ping.add_argument("--port", type=int, default=443, help="TCP port to ping (default: 443)")

    # scan-range
    parser_range = subparsers.add_parser("scan-range", help="Scan a CIDR for live hosts via TCP ping")
    parser_range.add_argument("cidr", help="CIDR (e.g., 192.168.1.0/24)")
    parser_range.add_argument("--port", type=int, default=443, help="TCP port to check (default: 443)")

    args = parser.parse_args()

    if args.command == "recon":
        run_recon(args.domain)
    elif args.command == "ptr":
        print("\n🛰️ Reverse DNS:")
        print(reverse_dns_lookup(args.ip))
    elif args.command == "asn":
        print("\n📡 ASN Lookup:")
        print(lookup_asn(args.ip))
    elif args.command == "dns":
        print(f"\n🧬 DNS Records for {args.domain}:")
        for record in fetch_dns_records(args.domain):
            print(record)
    elif args.command == "ping":
        print("\n⚡ TCP Ping:")
        print(tcp_ping(args.host, args.port))
    elif args.command == "scan-range":
        print()
        scan_cidr_range(args.cidr, args.port)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
