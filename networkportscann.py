from networkscann import is_active
from portscann import port_scan
from concurrent.futures import ThreadPoolExecutor

import ipaddress


def netwoks_port(ip):
    ##Prüft, ob ein Gerät aktiv ist, und scannt dann seine Ports.
    if is_active(str(ip)):
        port_scan(ip)


def network_port_scan(NetworkIp):
    #Scannt ein ganzes Netzwerk: prüft jedes Gerät und dessen Ports."""
    net = ipaddress.ip_network(NetworkIp)
    with ThreadPoolExecutor(max_workers=60) as pool:
        for ip in net.hosts():
            pool.submit(netwoks_port, str(ip))