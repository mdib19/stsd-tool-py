import psutil

def show_performance():
    print("\n=== SYSTEM PERFORMANCE ===")

    #CPU
    cpu = psutil.cpu_percent(interval=1)
    print("CPU Usage:", cpu, "%")

    #RAM
    ram = psutil.virtual_memory()
    print("RAM Usage:", ram.percent, "%")

    #DISK
    disk = psutil.disk_usage('/')
    print("Disk Usage:", disk.percent, "%")

    #TOP PROCESS
    print("\nTop CPU Processes:")
    processes = psutil.process_iter(['pid', 'name', 'cpu_percent'])

    sorted_processes = sorted(
        processes,
        key=lambda p: p.info['cpu_percent'] or 0,
        reverse=True
    )

    for proc in sorted_processes[:5]:
        print(proc.info['name'], "-", proc.info['cpu_percent'], "%")