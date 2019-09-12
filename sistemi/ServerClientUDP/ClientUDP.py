import socket as sck 

HOST = "127.0.0.1"
PORT = 22222
s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)

while True:
    testo = input("inserisci il messaggio: ")
    s.sendto(testo.encode(),(HOST,PORT))
    print("\nHai inviato: " + str(testo))

    data,server = s.recvfrom(4096)
    print("\nServer: " + data.decode())

    if(testo == "stop"):
        break

    

s.close()
print("socket chiuso")