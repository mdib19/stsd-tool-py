import subprocess
import os
import psutil


#flush dns
def flush_dns():
    print("\nFlushing DNS cache...")
    subprocess.run("ipconfig /flushdns", shell=True)
    print("Done.")

#renew ip
def renew_ip():
    print("\nRenewing IP address...")
    subprocess.run("ipconfig /release", shell=True)
    subprocess.run("ipconfig /renew", shell=True)
    print("Done.")

#temp files
def clear_temp_files():
    print("\nClearing temporary files...")

    temp_path = os.getenv("TEMP")

    if temp_path:
        try:
            for file in os.listdir(temp_path):
                file_path = os.path.join(temp_path, file)
                try:
                    os.remove(file_path)
                except:
                    pass
            print("Temp files cleared.")
        except:
            print("Could not clear some files.")
    else:
        print("TEMP folder not found.")

#sfc
def run_sfc_scan():
    print("\nRunning SFC Scan (this may take a few minutes)...")
    print("Please do not close the window.")
    subprocess.run("sfc /scannow", shell=True)
    print("SFC Scan complete.")
    
#chkdsk
def run_chkdsk():
    print("\nRunning Check Disk Scan...")
    subprocess.run("chkdsk C: /f /r", shell=True)
    print("Done.")

#winsock
def reset_winsock():
    print("\nResetting Winsock...")
    subprocess.run("netsh winsock reset", shell=True)
    print("Done. Please restart your computer for changes to take effect.")

#tcp ip stack
def reset_tcpip():
    print("\nResetting TCP/IP Stack...")
    subprocess.run("netsh int ip reset", shell=True)
    print("Done. Please restart your computer for changes to take effect.")

#high cpu processes
def kill_high_cpu_process():
    print("\nFinding highest CPU process...")

    PROTECTED = {"system", "svchost.exe", "lsass.exe", "csrss.exe", "winlogon.exe"}

    processes = psutil.process_iter(['pid', 'name', 'cpu_percent'])
    sorted_processes = sorted(
        processes,
        key=lambda p: p.info['cpu_percent'] or 0,
        reverse=True
    )

    for proc in sorted_processes:
        name = proc.info['name'].lower()
        if name not in PROTECTED:
            print(f"Killing: {proc.info['name']} (PID {proc.info['pid']}) - {proc.info['cpu_percent']}%")
            proc.kill()
            print("Done.")
            break
    else:
        print("No killable high-CPU process found.")