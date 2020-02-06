n2l = {0:"A",
       1:"B",
       2:"C",
       3:"D",
       4:"E",
       5:"F",
       6:"G",
       7:"H",
       8:"I",
       9:"L",
       10:"M",
       11:"N",
       12:"O",
       13:"P",
       14:"Q",
       15:"R",
       16:"S",
       17:"T",
       18:"U",
       19:"V",
       20:"Z"}

parola = "ciao"
key = "ITISDELPOZZO"
l2n = {}
for numero, lettera in n2l.items():
    l2n[lettera] = numero

for k in key:
    parola = parola + " " + str(l2n[k]) 

print(parola)