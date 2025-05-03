# recon/fingerprint.py

import requests


def get_tech_stack(domain: str) -> list:
    url = f"http://{domain}"
    headers_of_interest = ["Server", "X-Powered-By", "Via", "X-CDN"]

    try:
        response = requests.get(url, timeout=5)
        tech_stack = []

        for header in headers_of_interest:
            value = response.headers.get(header)
            if value:
                tech_stack.append(f"{header}: {value}")

        if not tech_stack:
            tech_stack.append("No identifiable tech headers.")

        return tech_stack

    except requests.exceptions.RequestException as e:
        return [f"Failed to fingerprint: {e}"]
