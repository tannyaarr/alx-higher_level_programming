#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("- Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
