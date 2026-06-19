import subprocess
import os

def flush_dns():
    print("\nFlushing DNS cache...")
    subprocess.run("ipconfig /flushdns", shell=True)
    print("Done.")

def renew_ip():
    print("\nRenewing IP address...")
    subprocess.run("ipconfig /release", shell=True)
    subprocess.run("ipconfig /renew", shell=True)
    print("Done.")

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