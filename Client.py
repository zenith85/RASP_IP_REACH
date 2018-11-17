import socket

SERVER_REPLY = "Server ?"
host = '192.168.219.168'  # ip of raspberry pi
port = 1234
client = socket.socket()
client.connect(('192.168.219.168', 1234))


def communicate(data):
    global SERVER_REPLY
    client.send(data.encode())
    SERVER_REPLY = client.recv(1024).decode()
    return


while True:

    if (SERVER_REPLY == "goodbye"):
        client.close()
        print("oh the server saying ",SERVER_REPLY)
        break
    else:
        print(SERVER_REPLY)
        Command = input("your command: ")
        communicate(Command)
