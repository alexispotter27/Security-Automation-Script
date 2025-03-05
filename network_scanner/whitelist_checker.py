def load_whitelist(filename="whitelist.txt"):
    try:
        with open(filename, "r") as file:
            return {line.strip() for line in file}
    except FileNotFoundError:
        print("Whitelist file not found. Skipping check.")
        return set()

def check_unauthorized_devices(devices, whitelist):
    unauthorized_devices = [device for device in devices if device["MAC"] not in whitelist]
    return unauthorized_devices
