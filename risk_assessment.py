from datetime import datetime

def generate_report(analysis):
    with open("wifi_report.txt", "w") as f:
        f.write("Wi-Fi Security Analysis Report\n")
        f.write(f"Date: {datetime.now()}\n\n")

        for ssid, security, risk in analysis:
            f.write(f"SSID: {ssid}\n")
            f.write(f"Security: {security}\n")
            f.write(f"Risk Level: {risk}\n")
            f.write("-" * 30 + "\n")
