import subprocess

def get_interfaces():
    result = subprocess.run(
        ["netsh", "wlan", "show", "interfaces"],
        capture_output=True,
        text=True
    )
    print(result.stdout)

if __name__ == "__main__":
    get_interfaces()
