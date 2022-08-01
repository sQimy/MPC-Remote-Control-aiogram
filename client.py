import socket

SERVER = "192.168.0.110"
PORT = 8080

while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))

    mediaControl = input('task?: ')
    client.sendall(bytes(mediaControl,'UTF-8'))
    data = client.recv(1024)
    print(data.decode())
    client.close()