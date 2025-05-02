# cli.py

import argparse
from recon.recon_engine import run_recon


def main():
    parser = argparse.ArgumentParser(description="Ninja AI - Reconnaissance Module")
    parser.add_argument("domain", help="Target domain (e.g., example.com)")
    args = parser.parse_args()

    run_recon(args.domain)


if __name__ == "__main__":
    main()
