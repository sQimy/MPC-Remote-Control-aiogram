import socket, pyautogui as pg
import mediaControl as mc

LOCALHOST = "192.168.0.110"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)

print("Server started")
print("Waiting for client request..")

while True:
    clientConnection, clientAddress = server.accept()
    print("Connected clinet :" , clientAddress)
    data = clientConnection.recv(1024)
    print("Client request for:", data.decode())
    message = data.decode()
    if message == "1":
        mc.playPause()
        print(f'Play/Pause recived, message: {message}')
    elif message == '2':
        mc.Next()
        print(f'Next recived, message: {message}')
    elif message == '3':
        mc.Previous()
        print(f'Previous recived, message: {message}')
    elif message == '4':
        mc.VolumeUp()
        print(f'VolumeUp recived, message: {message}')
    elif message == '5':
        mc.VolumeDown()
        print(f'VolumeDown recived, message: {message}')
    elif message == '6':
        mc.Fullscreen()
        print(f'Fullscreen recived, message: {message}')
    else:
        print(f'undifined message recived {message}')
    clientConnection.send(bytes("Successfully Connected to Server!!",'UTF-8'))
    clientConnection.close()