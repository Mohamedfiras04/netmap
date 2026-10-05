from networkscann import is_active
from portscann import port_scan

import ipaddress
import socket

                           
def network_port_scan(NetworkIp):
     net=ipaddress.ip_network(NetworkIp)
     for ip in net.hosts():
         if is_active(str(ip)):
             try:
                 name=socket.gethostbyaddr(str(ip))[0]
             except:
                 name="Unknown"
             print(f"{ip} is active ----> {name}")
             port_scan(ip)