from wifi_scanner import scan_wifi
from encryption_analysis import analyze_encryption
from risk_assessment import generate_report

networks = scan_wifi()
analysis = analyze_encryption(networks)
generate_report(analysis)

print("Report generated in wifi_report.txt")
