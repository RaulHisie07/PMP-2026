import random

numar_persoane = 100000

numar_pozitive = 0 
numar_bolnavi_pozitivi = 0

for i in range(numar_persoane):
   bolnav = random.random() < 0.01

   if bolnav:
      test_pozitiv = random.random() < 0.95
   else:
      test_pozitiv = random.random() < 0.10
    
   if test_pozitiv:
      numar_pozitive = numar_pozitive + 1

      if bolnav:
        numar_bolnavi_pozitivi = numar_bolnavi_pozitivi + 1


probabilitate_simulata = (numar_bolnavi_pozitivi/numar_pozitive)

probabilitate_teoretica = (
    (0.95 * 0.01) /
    ((0.95 * 0.01) + (0.10 * 0.99))
)

print("Probabilitatea simulata:", probabilitate_simulata)
print("Probabilitatea teoretica:", probabilitate_teoretica)