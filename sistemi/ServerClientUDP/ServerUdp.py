import socket as sck 

HOST = "127.0.0.1"
PORT = 22222

s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
s.bind((HOST,PORT))

while True:
    data,address = s.recvfrom(4096)
    print("Client: " + data.decode())

    testo = input("Messaggio: ")
    s.sendto(testo.encode(), address)
    print("\nHai inviato" + str(testo))

    if(data.decode() == "stop"):

        break
    
s.close()
print("chiusura server")