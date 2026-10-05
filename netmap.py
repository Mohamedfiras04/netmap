import argparse
import socket

parser= argparse.ArgumentParser("Netmap: A simpole network mapping tool" )
parser.add_argument("-p","--port",help="port scanning",required=False)
parser.add_argument(-"n","--network",help="network scanning",requird=False)
parser.add_argument(-"np","--networkport",help="network and port scanning ", requird=False)

arg=parser.parse_args()
if arg.port :
    print(f)
