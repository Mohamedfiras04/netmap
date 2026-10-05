import platform 
import subprocess
import ipaddress
import socket

def is_active(ip):
    system = "-n" if platform.system() == "Windows" else "-c"
    test = subprocess.run(["ping", system, "1", ip],
        capture_output=True, text=True,
        encoding="utf-8", errors="ignore")       # ← Encoding + Fehler ignorieren!
    if test.stdout is None:                        # ← falls leer
        return False
    
    return "TTL" in test.stdout  

def network_scan(NetworkIp):
    net=ipaddress.ip_network(NetworkIp)
    for ip in net.hosts():
        if is_active(str(ip)):
            try:
                name=socket.gethostbyaddr(str(ip))[0]
            except:
                name="Unknown"
            print(f"{ip} is active ----> {name}")