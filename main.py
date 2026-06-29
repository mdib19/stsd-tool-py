import socket
import subprocess
import psutil

def run_full_diagnosis():
    print("\n=== FULL SYSTEM DIAGNOSIS ===")
    warnings = []


    #internet
    print("\n[1/5] Checking Internet Connection...")
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("\n Status: OK")
        internet_ok = True
    except:
        print("\n Status: FAILED")
        warnings.append("No internet connection detected.\n Check your router or try Renew IP / Reset Winsock in Fixes.")
        internet_ok = False
        
        
    #ping
    print("\n[2/5] Checking Ping...")
    if internet_ok:
        result = subprocess.run(
            ["ping", "8.8.8.8", "-n", "2"],
            capture_output=True,
            text=True
        )
        if "TTL=" in result.stdout:
            print("\n Status: OK")
        else:
            print("\n Status: FAILED")
            warnings.append("Ping test failed.\n Try Flush DNS or Reset TCP/IP Stack in Fixes.")
    else:
        print("\n Status: SKIPPED (No internet)")
        
        
        
    #cpu
    print("\n[3/5] Checking CPU Usage...")
    cpu = psutil.cpu_percent(interval=1)
    if cpu >= 80:
        print(f"\n Status: WARNING ({cpu}%)")
        warnings.append(f"CPU usage is critically high ({cpu}%).\n Use Kill High CPU Process in Fixes.")
    elif cpu >= 50:
        print(f"\n Status: MODERATE ({cpu}%)")
        warnings.append(f"CPU usage is moderately high ({cpu}%).\n Monitor and consider closing heavy applications.")
    else:
        print(f"\n Status: OK ({cpu}%)")
        
        
    #ram
    print("\n[4/5] Checking RAM Usage...")
    ram = psutil.virtual_memory().percent
    if ram >= 80:
        print(f"\n Status: WARNING ({ram}%)")
        warnings.append(f"RAM usage is critically high ({ram}%).\n Close unused applications.")
    elif ram >= 50:
        print(f"\n Status: MODERATE ({ram}%)")
        warnings.append(f"RAM usage is moderately high ({ram}%).\n Monitor and close unused applications if it rises.")
    else:
        print(f"\n Status: OK ({ram}%)")



    #disk
    print("\n[5/5] Checking Disk Usage...")
    disk = psutil.disk_usage('/').percent
    if disk >= 85:
        print(f"\n Status: WARNING ({disk}%)")
        warnings.append(f"Disk space is critically low ({disk}%).\n Use Clear Temp Files in Fixes and uninstall unused programs.")
    elif disk >= 60:
        print(f"\n Status: MODERATE ({disk}%)")
        warnings.append(f"Disk space is getting low ({disk}%).\n Consider clearing Temp Files in Fixes and uninstall unused programs.")
    else:
        print(f"\n Status: OK ({disk}%)")


    #summ
    print("\n=== DIAGNOSIS SUMMARY ===")
    if not warnings:
        print("\nAll checks passed.")
        print("Overall Status: GOOD")
    else:
        print(f"\n{len(warnings)} issue(s) found:\n")
        for i, warning in enumerate(warnings, 1):
            print(f"[{i}] {warning}\n")

        if len(warnings) >= 3:
            print("Overall Status: POOR")
        elif len(warnings) >= 1:
            print("Overall Status: WARNING")
