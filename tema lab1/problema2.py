import random 

N = 0
S = 0

while True:
    N = N+1
    moneda = random.choice("stema","ban")

    if moneda == "stema":
        z = random.int(1,6)
        S = S + (z-3)
        break
    else:
        S = S - 0.5

print("Numarul de pasi N : ",N)
print("Suma S : ",S)