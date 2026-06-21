from selections import system_info
from selections import performance
from selections import network
from selections import fixes
from selections import health

while True:
    print("\n=== SELF TROUBLESHOOT AND SYSTEM DIAGNOSTIC TOOL ===")
    print("[1] System Information")
    print("[2] Performance Check")
    print("[3] Network Check")
    print("[4] One Click Fixes")
    print("[5] System Health Score")
    print("[6] Exit") 

    choice = input("Please select an option: ")

    if choice == "1":
        system_info.show_system_info()

    elif choice == "2":
        performance.show_performance()

    elif choice == "3":
        print("[1] Internet Check")
        print("[2] IP Info")
        print("[3] Ping Test")
        print("[4] Full Diagnosis")

        sub = input("Please select an option: ")

        if sub == "1":
            network.check_internet()

        elif sub == "2":
            network.show_ip()

        elif sub == "3":
            network.ping_test()

        elif sub == "4":
            network.internet_diagnosis()

        else:
            print("Invalid option")
            
    elif choice == "4":
        print("[1] Flush DNS")
        print("[2] Renew IP")
        print("[3] Clear Temp Files")

        fix = input("Please select an option: ")

        if fix == "1":
            fixes.flush_dns()

        elif fix == "2":
            fixes.renew_ip()

        elif fix == "3":
            fixes.clear_temp_files()

        else:
            print("Invalid option")
    
    elif choice == "5":
        health.calculate_health_score()

    elif choice == "6":
        break

    else:
        print("Invalid option")
