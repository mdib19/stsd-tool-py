import psutil

def calculate_health_score():
    print("\n=== SYSTEM HEALTH SCORE ===")

    score = 100

    #CPU USAGE
    cpu = psutil.cpu_percent(interval=1)
    if cpu > 80:
        score -= 25
    elif cpu > 50:
        score -= 10

    #RAM USAGE
    ram = psutil.virtual_memory().percent
    if ram > 80:
        score -= 25
    elif ram > 50:
        score -= 10

    #DISK USAGE
    disk = psutil.disk_usage('/').percent
    if disk > 85:
        score -= 25
    elif disk > 60:
        score -= 10


    print(f"CPU Usage: {cpu}%")
    print(f"RAM Usage: {ram}%")
    print(f"Disk Usage: {disk}%")


    print(f"System Health Score: {score}/100")

    if score >= 80:
        print("Status: GOOD")
    elif score >= 50:
        print("Status: MODERATE")
    else:
        print("Status: POOR")
