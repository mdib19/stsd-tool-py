import subprocess

def show_event_logs():
    print("\n=== EVENT LOGS ===")
    print("[1] System Errors")
    print("[2] Application Errors")
    print("[3] Recent Warnings")

    choice = input("Please select an option: ")

    if choice == "1":
        print("\nFetching System Errors...")
        subprocess.run(
            'wevtutil qe System /c:5 /f:text /q:"*[System[Level=2]]"',
            shell=True
        )

    elif choice == "2":
        print("\nFetching Application Errors...")
        subprocess.run(
            'wevtutil qe Application /c:5 /f:text /q:"*[System[Level=2]]"',
            shell=True
        )

    elif choice == "3":
        print("\nFetching Recent Warnings...")
        subprocess.run(
            'wevtutil qe System /c:5 /f:text /q:"*[System[Level=3]]"',
            shell=True
        )

    else:
        print("Invalid option.")