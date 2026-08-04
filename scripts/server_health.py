import requests
import socket
from datetime import datetime

SITES = [
    #site(s)
]

TIMEOUT = 5

print("=" * 60)
print(f"Server Health Check - {datetime.now()}")
print("=" * 60)

for site in SITES:
    try:
        response = requests.get(site, timeout=TIMEOUT)

        hostname = site.split("//")[1].split("/")[0]
        ip = socket.gethostbyname(hostname)

        print(f"\nSite: {site}")
        print(f"IP Address: {ip}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response.elapsed.total_seconds():.3f}s")

        if response.ok:
            print("Status: ONLINE")
        else:
            print("Status: ERROR")

    except Exception as e:
        print(f"\nSite: {site}")
        print("Status: OFFLINE")
        print(f"Reason: {e}")