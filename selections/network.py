import socket
import subprocess

def internet_status():
    print("\n=== NETWORK CHECK ===")
    try:
        #try google dns
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("Internet Status: CONNECTED")
    except OSError:
        print("Internet Status: NOT CONNECTED")


def show_ip():
    print("\n=== IP INFORMATION ===")
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print("Hostname:", hostname)
    print("IP Address:", ip_address)


def ping_test():
    print("\n=== PING TEST ===")
    result = subprocess.run(
        ["ping", "8.8.8.8", "-n", "2"],
        capture_output=True,
        text=True
    )

    if "TTL=" in result.stdout:
        print("Ping Result: SUCCESS")
    else:
        print("Ping Result: FAILED")
