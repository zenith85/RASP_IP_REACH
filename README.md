# RASP_IP_REACH
control your raspberry pi through the network, (private or public) using Python (CLIENT,SERVER)
Project Remote reach raspberry chip using python:
This is Ver.1.0

The commands on the client should be done on the remote PC or another pi
The commands on the server should be done on a raspberry pi
Run the server to wait for client, run the client on the other side to establish a connection
The client can do couple of commands to the server and the server reply, one such a kind command can be translated by the server as OS commands, such as reboot will be converted into “sudo reboot”

NOTES:
on the server part, "to find the local IP address" section can be removed if any problems appear due to the system destro. 
However, if that so, please remove the "#" from the "#ip='192.168.219.168'" and use your own server IP address. 

RESOLVE:
This server code is have the ability to ignore and avoid the error 98, "socket.error: [Errno 98] Address already in use python", by simply doing a try/except error negation using the command "server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)"

Please remove that command if any problem appears due to the system destro.

Feel free to comment and ask any question,
