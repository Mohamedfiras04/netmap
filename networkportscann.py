from networkscann import is_active
from portscann import port_scan
from concurrent.futures import ThreadPoolExecutor

import ipaddress
import socket
def netwoks_port(ip):
    if is_active(str(ip)):
    
        port_scan(ip)
                           
def network_port_scan(NetworkIp):
     net=ipaddress.ip_network(NetworkIp)
     with ThreadPoolExecutor(max_workers=100) as pool:
            
        for ip in net.hosts():
            pool.submit(netwoks_port,str(ip) )
            