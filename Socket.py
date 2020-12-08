import socket
import sys



def checkPortsSocket ():
    print("Revisión de puertos abiertos y cerrados")

    ip= "187.190.178.68"
    portlist= 80,443,21
    print("IP",ip,type(ip))
    try:
        for port in portlist:
            # Crea un socket TCP/IP
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip,port))
            if result == 0:
                print ("Puerto {}: \t Abierto".format(port))
            else:
                print ("Puerto {}: \t Cerrado".format(port))
            sock.close
    except socket.error as error:
        print (str(error))
        print ("Error de conexión")
        sys.exit()