import platform
import socket
import getpass
import psutil
from cpuinfo import get_cpu_info


def show_system_info():
    print("\n=== SYSTEM INFORMATION ===")

    print("Computer Name:", socket.gethostname())

    print("User:", getpass.getuser())

    print("OS:", platform.system(), platform.release())
    
    cpu_info = get_cpu_info()
    cpu_name = cpu_info["brand_raw"]

    print("CPU:", cpu_name)
    print("Cores:", psutil.cpu_count(logical=False))
    print("Threads:", psutil.cpu_count(logical=True))

    ram = psutil.virtual_memory().total / (1024 ** 3)
    print(f"RAM: {ram:.2f} GB")