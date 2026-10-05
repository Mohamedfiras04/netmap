import socket 

def port_scan (ip):
    for port in range (1,1400):

        sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.5)
        if sock.connect_ex( (str(ip),port) )==0 :
            try:
                name=socket.getservbyport(port)
            except:
                name ="Unknown"
            
            print(f"Port : {port} is open  ----> {name}")
        sock.close()
