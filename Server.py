import socket
import os

#-----------------to find the local IP address----------------------
gw = os.popen("ip -4 route show default").read().split()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gw[2], 0))
ip = s.getsockname()[0]
gateway = gw[2]
host = socket.gethostname()
print ("IP:", ip, " GW:", gateway, " Host:", host)
#-------------------------------------------------------------------
#ip='192.168.219.168'
def BINDING(ip,port):
        address=(ip,port)
        server.bind(address)

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

port=1234
BINDING(ip,port)
server.listen(1)
print "[*] started listening on ", ip, ":", port
client,addr=server.accept()
print "[*] Get a connection from ", addr[0], ":", addr[1]
while True:
        data=client.recv(1024)
        print "[*] Received '",data,"' from the client"
        print " Processing data"
        if (data=="Hello server"):
                client.send("Hello client")
                print "         processing done, data was valid.\n[*] Replay se$
        elif (data=="disconnect"):
                client.send("goodbye")
                client.close()
                break;
        elif (data=="reboot"):
                os.system("sudo reboot")
        else:
