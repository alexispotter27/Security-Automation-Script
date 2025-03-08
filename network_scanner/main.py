from scanner import scan_network
from port_scanner import scan_ports
from file_handler import save_results_to_csv
from whitelist_checker import load_whitelist, check_unauthorized_devices
from email_alert import send_email_alert
from telegram_alert import send_telegram_alert
import requests

DASHBOARD_URL = "http://127.0.0.1:8000/add-scan-result/"

def main():
    network = input("Enter network IP range (e.g., 192.168.1.1/24): ")
    devices_found = scan_network(network)

    for device in devices_found:
        device["Open Ports"] = scan_ports(device["IP"])

    whitelist = load_whitelist()
    unauthorized_devices = check_unauthorized_devices(devices_found, whitelist)

    print("\nDevices Found:")
    for device in devices_found:
        print(f"{device['IP']} - {device['MAC']} - Open Ports: {device['Open Ports']}")

    if unauthorized_devices:
        print("\nALERT! Unauthorized Devices Found:")
        for device in unauthorized_devices:
            print(f"{device['IP']} - {device['MAC']}")

    save_results_to_csv(devices_found, "network_scan_with_ports.csv")

if __name__ == "__main__":
    main()

def alert_security_breach(device_ip):
    message = f"🚨 Security Alert: Unauthorized device detected!\nIP: {device_ip}"

    # Send email alert
    send_email_alert("Security Alert 🚨", message)

    # Send Telegram alert
    send_telegram_alert(message)

# Example Usage
if __name__ == "__main__":
    alert_security_breach("192.168.1.100")


def alert_security_breach(device_ip):
    message = f"🚨 Security Alert: Unauthorized device detected!\nIP: {device_ip}"
    send_email_alert("Security Alert 🚨", message)
    send_telegram_alert(message)

def run_security_scan():
    print("[🔄] Running security scan...")
    suspicious_devices = scan_network()  # Modify based on your scanner output
    for device in suspicious_devices:
        alert_security_breach(device)

if __name__ == "__main__":
    run_security_scan()

def report_scan_result(ip, status):
    data = {"ip": ip, "status": status}
    requests.post(DASHBOARD_URL, params=data)

# Example Usage
if __name__ == "__main__":
    report_scan_result("192.168.1.100", "Unauthorized Device")