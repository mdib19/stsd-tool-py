import ctypes
import sys
import os

def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return
    else:
        script = os.path.abspath(sys.argv[0])
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, f'"{script}"', None, 1
        )
        sys.exit()

run_as_admin()

from selections import system_info
from selections import performance
from selections import network
from selections import fixes
from selections import health
from selections import event_logs
from selections import diagnosis

while True:
    print("\n=== IB19 SELF TROUBLESHOOT AND SYSTEM DIAGNOSTIC TOOL ===")
    print("[1] System Information")
    print("[2] Performance Check")
    print("[3] Network Check")
    print("[4] Fixes")
    print("[5] System Health Score")
    print("[6] View Event Logs")
    print("[7] System Diagnosis")
    print("[8] Exit")

    choice = input("Please select an option: ")

    if choice == "1":
        system_info.show_info()

    elif choice == "2":
        performance.show_performance()

    elif choice == "3":
        print("\n=== NETWORK CHECK ===")
        print("[1] Internet Status")
        print("[2] IP Info")
        print("[3] Ping Test")
        sub = input("Please select an option: ")

        if sub == "1":
            network.internet_status()

        elif sub == "2":
            network.show_ip()

        elif sub == "3":
            network.ping_test()

        else:
            print("Invalid option")
            
    elif choice == "4":
        print("\n=== FIXES ===")
        print("[1] Flush DNS --- Fixes websites not loading")
        print("[2] Renew IP --- Fixes network issues")
        print("[3] Clear Temp Files --- Frees space and speed up PC")
        print("[4] Run SFC Scan --- Scan and repair corrupted system files")
        print("[5] Check Disk (chkdsk) --- Scan and repair disk")
        print("[6] Reset Winsock --- Fixes network issues")
        print("[7] Reset TCP/IP Stack --- Fixes network issues")
        print("[8] Kill High CPU Process --- Speed up PC")
        fix = input("Please select an option: ")

        if fix == "1":
            fixes.flush_dns()

        elif fix == "2":
            fixes.renew_ip()

        elif fix == "3":
            fixes.clear_temp()

        elif fix == "4":
            fixes.run_sfc()
            
        elif fix == "5":
            fixes.run_chkdsk()

        elif fix == "6":
            fixes.reset_winsock()

        elif fix == "7":
            fixes.reset_tcpip()

        elif fix == "8":
            fixes.kill_highcpu()

        else:
            print("Invalid option")
    
    elif choice == "5":
        health.calc_health()
        
    elif choice == "6":
        event_logs.show_logs()

    elif choice == "7":
        diagnosis.run_diagnosis()

    elif choice == "8":
        break

    else:
        print("Invalid option")
