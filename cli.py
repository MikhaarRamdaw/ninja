# cli.py

import argparse
from recon.recon_engine import run_recon
from networking.reverse_dns import reverse_dns_lookup
from networking.asn_lookup import lookup_asn
from networking.dns_records import fetch_dns_records
from networking.ping import tcp_ping
from colorama import init

init(autoreset=True)


def main():
    parser = argparse.ArgumentParser(description="Ninja AI - Terminal Recon Tool")
    subparsers = parser.add_subparsers(dest="command")

    # recon
    parser_recon = subparsers.add_parser("recon", help="Run full recon on domain")
    parser_recon.add_argument("domain", help="Target domain (e.g., example.com)")

    # reverse-dns
    parser_rdns = subparsers.add_parser("reverse-dns", help="Perform reverse DNS lookup")
    parser_rdns.add_argument("ip", help="Target IP address (e.g., 8.8.8.8)")

    # asn-lookup
    parser_asn = subparsers.add_parser("asn-lookup", help="Get ASN and ownership info for an IP")
    parser_asn.add_argument("ip", help="Target IP address")

    # dns-records
    parser_dns = subparsers.add_parser("dns-records", help="Fetch DNS records for a domain")
    parser_dns.add_argument("domain", help="Target domain")

    # ping
    parser_ping = subparsers.add_parser("ping", help="Check if a host is alive using TCP ping")
    parser_ping.add_argument("host", help="Target host or IP address")
    parser_ping.add_argument("--port", type=int, default=443, help="TCP port to ping (default: 443)")

    args = parser.parse_args()

    if args.command == "recon":
        run_recon(args.domain)
    elif args.command == "reverse-dns":
        print("\n🛰️ Reverse DNS:")
        print(reverse_dns_lookup(args.ip))
    elif args.command == "asn-lookup":
        print("\n📡 ASN Lookup:")
        print(lookup_asn(args.ip))
    elif args.command == "dns-records":
        print(f"\n🧬 DNS Records for {args.domain}:")
        for record in fetch_dns_records(args.domain):
            print(record)
    elif args.command == "ping":
        print("\n⚡ TCP Ping:")
        print(tcp_ping(args.host, args.port))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
