import numpy as np
n = 4647233
isprime = True
for p in range(2, (n//2)+1):
    if (n % p == 0):
        print(f"Trovato fattore {p}")
        isprime = False
if isprime:
    print(f"Il numero {n} è primo")