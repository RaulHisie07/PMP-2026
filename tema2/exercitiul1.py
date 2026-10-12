import random

numar_aruncari = 100000

primul_par = 0
suma10_primul_par = 0

cel_putin_unul_par = 0
suma10_cel_putin_unul_par = 0

suma8 = 0
ambele_pare_suma8 = 0

for i in range(numar_aruncari):
    X = random.randint(1,6)
    Y = random.randint(1,6)

    if X % 2 == 0 :
        primul_par = primul_par + 1

        if X+Y >=10:
            suma10_primul_par = suma10_primul_par + 1

    if X%2 == 0 or Y%2==0: 
        cel_putin_unul_par = cel_putin_unul_par + 1

        if X+Y>=10:
            suma10_cel_putin_unul_par = suma10_cel_putin_unul_par + 1

    if X+Y == 8:
        suma8 = suma8+1

        if X%2==0 and Y%2==0:
            ambele_pare_suma8 = ambele_pare_suma8 + 1

p1 = suma10_primul_par / primul_par

p2 = suma10_cel_putin_unul_par / cel_putin_unul_par

p3 = ambele_pare_suma8 / suma8

print("Punctul 1 - simulare : ",p1," exact : ",2/9)
print("Punctul 2 - simulare : ",p2," exact : ",5/27)
print("Punctul 3 - simulare : ",p3," exact : ",3/5)
  