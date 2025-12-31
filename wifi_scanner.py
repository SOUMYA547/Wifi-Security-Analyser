import subprocess
import re

def scan_wifi():
    result = subprocess.run(
        ["netsh", "wlan", "show", "networks", "mode=bssid"],
        capture_output=True,
        text=True
    )

    networks = []
    ssid = None

    for line in result.stdout.split("\n"):
        if "SSID" in line and ":" in line:
            ssid = line.split(":")[1].strip()
        elif "Authentication" in line:
            auth = line.split(":")[1].strip()
            networks.append((ssid, auth))

    return networks

if __name__ == "__main__":
    wifi_networks = scan_wifi()
    for net in wifi_networks:
        print(f"SSID: {net[0]} | Security: {net[1]}")
