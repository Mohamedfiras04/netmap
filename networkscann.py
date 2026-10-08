import platform
import subprocess
import ipaddress
import socket
from concurrent.futures import ThreadPoolExecutor


def is_active(ip):
        # Prüft per Ping, ob ein Gerät erreichbar ist. Gibt bei Erfolg True zurück, sonst False.
    system = "-n" if platform.system() == "Windows" else "-c"
    test = subprocess.run(["ping", system, "1", ip],
        capture_output=True, text=True,
        encoding="utf-8", errors="ignore")

    if "TTL" in test.stdout:
        try:
            name = socket.gethostbyaddr(str(ip))[0]
        except socket.herror:
            name = "Unknown"
        print(f"{ip} is active ----> {name}")
        return True
    return False


def network_scan(NetworkIp):
    #Scannt ein ganzes Netzwerk und zeigt alle aktiven Geräte an.
    net = ipaddress.ip_network(NetworkIp)
    with ThreadPoolExecutor(max_workers=100) as pool:
        for ip in net.hosts():
            pool.submit(is_active, str(ip))