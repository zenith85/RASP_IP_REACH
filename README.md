# Remote Raspberry Pi Control using Python (Academic Purposes)
**Project Logo is not available**

## Overview
This project enables you to control your Raspberry Pi over the network, whether it's a private or public connection. The implementation involves Python scripts for both the client and server sides.

## Version
This documentation corresponds to Version 1.0 of the project.

## Usage
### Client Side
Execute the following commands on the remote PC or another Raspberry Pi:

#### **bash**
python client.py
This will establish a connection with the server.

### Server Side
Run the server script on your Raspberry Pi:

#### **bash**
python server.py
The server will wait for a client to connect.

## Command Execution
The client can send various commands to the server, and the server will respond accordingly. For instance, a command like "reboot" will be translated on the server as "sudo reboot". Feel free to create your own set of commands.

## Configuration Notes
On the server side, the "Find Local IP Address" section can be omitted if any issues arise from system changes. In such cases, remove the "#" from the "#ip='192.168.219.168'" line and use your own server IP address.

## Troubleshooting
Address Already in Use Error
The server code is designed to handle the "Address already in use" error (socket.error: [Errno 98]) by employing a try/except block. If you encounter any problems related to system changes, consider removing the following line:

## python
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Feel free to comment and ask any questions. Contributions are welcome—fork the project and showcase its full potential!
