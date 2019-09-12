import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1025))
while True:
    text = input("Messaggio: ")

    if text == "EXIT":
        s.sendall(text.encode())
        break
        
    else:
        s.sendall(text.encode())
        data = s.recv(4096)
        print("Server: " + data.decode())

conn.close()
s.close()