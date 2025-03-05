from scanner import scan_network
from port_scanner import scan_ports
from file_handler import save_results_to_csv
from whitelist_checker import load_whitelist, check_unauthorized_devices

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
