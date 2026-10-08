
# netmap

A simple network and port scanning tool written in Python.  
netmap discovers active devices in a network and scans their open ports, using multithreading for fast results.


## Features

- Scan a whole network to find active devices (via ping)
- Resolve device hostnames
- Scan the first 1400 ports of a device
- Identify common services on open ports
- Fast scanning using multithreading (ThreadPoolExecutor)

## Requirements

- Python 3.x

No external libraries are required (only Python's standard library).

## Usage
Network scan only (find active devices)
py netmap.py -n 192.168.0.0/24

Port scan only (scan ports of one device)
py netmap.py -p 192.168.0.1

Network + port scan (find devices and scan their ports)
py netmap.py -np 192.168.0.0/24


Show the help message:
py netmap.py -h


## Example output
192.168.0.1 is active ----> kabelbox.local
192.168.0.1 - Port : 53 is open ----> domain
192.168.0.1 - Port : 80 is open ----> http


## Project structure

- `netmap.py` – main program, handles arguments and starts the scans
- `networkscann.py` – network scanning (ping, host discovery)
- `portscann.py` – port scanning
- `networkportscann.py` – combined network and port scanning

## Disclaimer

This tool is for educational purposes only.  
Only scan networks that you own or have permission to test.  
Unauthorized scanning of networks may be illegal.

## Author

Made by Mohamedfiras04
