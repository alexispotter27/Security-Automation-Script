import csv

def save_results_to_csv(devices, filename="network_scan_results.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP Address", "MAC Address", "Open Ports"])
        for device in devices:
            writer.writerow([device["IP"], device["MAC"], ", ".join(map(str, device.get("Open Ports", [])))])
    print(f"Results saved to {filename}")
