import socket
from concurrent.futures import ThreadPoolExecutor


def check_port(ip, port):
    # Prüft einen einzelnen Port und zeigt ihn an, falls er offen ist.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.2)
    if sock.connect_ex((ip, port)) == 0:
        try:
            name = socket.getservbyport(port)
        except OSError:
            name = "Unknown"
        print(f"{ip} - Port : {port} is open ----> {name}")
    sock.close()


def port_scan(ip):
    #Scannt die ersten 1400 Ports eines Geräts gleichzeitig mit Threads.
    ip = str(ip)
    with ThreadPoolExecutor(max_workers=100) as pool:
        for port in range(1, 1400):
            pool.submit(check_port, ip, port)