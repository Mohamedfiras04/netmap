import platform 
import subprocess
import ipaddress
import socket
from concurrent.futures import ThreadPoolExecutor

def is_active(ip):
    system = "-n" if platform.system() == "Windows" else "-c"
    test = subprocess.run(["ping", system, "1", ip],
        capture_output=True, text=True,
        encoding="utf-8", errors="ignore")       # ← Encoding + Fehler ignorieren!
  
    if "TTL" in test.stdout :
        try:
            name=socket.gethostbyaddr(str(ip))[0]
        except:
            name="Unknown"
        print(f"{ip} is active ----> {name}")


def network_scan(NetworkIp):
    net=ipaddress.ip_network(NetworkIp)
    with ThreadPoolExecutor(max_workers=100) as pool:
        for ip in net.hosts():
            pool.submit(is_active,str(ip))
            
                