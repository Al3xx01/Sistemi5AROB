import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1025))
s.listen()
conn, addr = s.accept()
while True:
    data = conn.recv(4096)  
    print("Client: " + data.decode())
    if data.decode() == "EXIT":
        break
    else:
        text = input("Messaggio: ")
        conn.sendall(text.encode())

conn.close()
s.close()