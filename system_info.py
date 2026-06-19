import platform
import socket
import getpass
import psutil


def show_system_info():
    print("\n=== SYSTEM INFORMATION ===")

    print("Computer Name:", socket.gethostname())

    print("User:", getpass.getuser())

    print("OS:", platform.system(), platform.release())

    cpu_name = platform.processor()
    print("CPU:", cpu_name)

    ram = psutil.virtual_memory().total / (1024 ** 3)
    print(f"RAM: {ram:.2f} GB")