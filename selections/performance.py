import psutil

def show_performance():
    print("\n=== SYSTEM PERFORMANCE ===")

    cpu = psutil.cpu_percent(interval=1)
    print("CPU Usage:", cpu, "%")

    ram = psutil.virtual_memory()
    print("RAM Usage:", ram.percent, "%")

    disk = psutil.disk_usage('/')
    print("Disk Usage:", disk.percent, "%")

    print("\nTop CPU Processes:")
    processes = psutil.process_iter(['pid', 'name', 'cpu_percent'])

    sorted_processes = sorted(
        processes,
        key=lambda p: p.info['cpu_percent'] or 0,
        reverse=True
    )
    for proc in sorted_processes[:5]:
        print(proc.info['name'], "-", proc.info['cpu_percent'], "%")
        
    print("\nTop RAM Processes:")
    processes = psutil.process_iter(['pid', 'name', 'memory_percent'])

    sorted_by_ram = sorted(
        processes,
        key=lambda p: p.info['memory_percent'] or 0,
        reverse=True
    )
    for proc in sorted_by_ram[:5]:
        print(proc.info['name'], "-", round(proc.info['memory_percent'], 2), "%")
