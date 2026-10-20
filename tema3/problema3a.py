import random

victorii_J0 = 0
victorii_J1 = 0

for i in range(10000):

    primul = random.randint(0, 1)

    n = random.randint(1, 6)

    if primul == 0:
        p = 4/7
    else:
        p = 0.5

    m = 0

    for j in range(2*n):
        if random.random() < p:
            m += 1

    if n >= m:
        castigator = primul
    else:
        castigator = 1 - primul

    if castigator == 0:
        victorii_J0 += 1
    else:
        victorii_J1 += 1

print("J0:", victorii_J0 / 10000)
print("J1:", victorii_J1 / 10000)