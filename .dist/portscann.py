import socket
def portscan(ip):
    for port in range (1,1400):
        sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.sendto(0.5)
        if sock.connect_ex((ip,port))==0 :
            name=socket.getservbyport(port)
            print(f"Port {port}is open  ----> {name}")
        sock.close()
                           
        