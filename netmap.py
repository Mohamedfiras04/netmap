import argparse
from portscann import port_scan
from networkscann import network_scan
from networkportscann import network_port_scan


parser= argparse.ArgumentParser("Netmap: A simpole network mapping tool" )
parser.add_argument("-p","--port",help="port scanning first 1400 ports ",required=False)
parser.add_argument("-n","--network",help="network scanning",required=False)
parser.add_argument("-np","--networkport",help="network and port scanning ", required=False)

arg=parser.parse_args()

####

if arg.port :
    print(f"Port scanning on {arg.port }")
    port_scan(arg.port)
if  arg.network :
    print(f"network scanning on {arg.network}")
    network_scan(arg.network)
if arg.networkport:
    print(f"network and port scanning on {arg.networkport}")
    network_port_scan(arg.networkport)
