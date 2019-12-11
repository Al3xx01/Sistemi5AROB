def mcd(a, b):  #Massimo comune divisore
    while b:
        a, b = b, a%b
    return a

def mcm(a, b):  #Minimo comune multiplo
    return a // mcd(a, b) * b

#IsPrime ritorna se un numero è primo o no
def isPrime(n):
    if(n<=1):
        return False
    if n <= 3:
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <=n):
        if(n % 2 == 0 or n % (i+2) == 0):
            return False
        i = i+6
    return True

#Trovo c
def findC(m):
    c = 2
    while c<m:
        if (mcd(c,m) != 1):
            c = c+1
        else:
            return c

#Trovo d
def findD(c, m):
    d = 0
    while d<m:
        if ((c*d)%m)!=1:
            d = d+1
        else:
            return d


while True:
    p = int(input("Inserisci p: "))
    q = int(input("Inserisci q: "))

    if(isPrime(p) and isPrime(q)):
        break
    else:
        print("Numeri inseriti non primi")

# Calcolo n
n = p * q
print(f"N: {n}")

#Calcolo minimo comune multiplo
m = mcm(p-1, q-1)
print(f"M: {m}")

#Scegliere un intero 1<c<m tale che mcd(c,m) = 1
c = findC(m)
print(f"C: {c}")

#Trova un intero 0<=d<m tale che (cd) mod m = 1
d = findD(c, m)
print(f"D: {d}")

while True:
    #Criptazione dato in input
    a = int(input("Inserisci un numero: "))

    if (a < n):
        cryptedA = pow(a, c) % n
        print(f"Numero cryptato [{a}]: {cryptedA}")

        #Decriptazione dato
        uncryptedA = pow(cryptedA, d)%n
        print(f"Numero decriptato[{cryptedA}]: {uncryptedA}")
        break
    else:
        print(f"Numero maggiore di {n}")

