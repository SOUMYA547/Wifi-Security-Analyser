def analyze_encryption(networks):
    analysis = []

    for ssid, security in networks:
        if "WPA3" in security:
            risk = "Low"
        elif "WPA2" in security:
            risk = "Medium"
        elif "Open" in security:
            risk = "High"
        else:
            risk = "Unknown"

        analysis.append((ssid, security, risk))

    return analysis
