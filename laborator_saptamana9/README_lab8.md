# Exercițiu laborator 8 – Programare probabilistă cu PyMC

Model: Y | n ~ Binomial(n, θ), n ~ Poisson(10), θ cunoscut.
Combinații: Y ∈ {0, 5, 10}, θ ∈ {0.2, 0.5} (6 cazuri).
Setări MCMC: 4 lanțuri × 5000 eșantioane (draws) pentru fiecare caz.
Grafic: `ex_lab8_posterior.png` (toate cele 6 posteriori într-o singură fereastră, cu `az.plot_posterior`).

## Calcul exact al posteriorului

Formule folosite:
- Binomial: P(Y | n) = C(n, Y) · θ^Y · (1−θ)^(n−Y), pentru n ≥ Y
- Poisson: P(n) = e^(−10) · 10^n / n!
- Bayes: P(n | Y) ∝ P(Y | n) · P(n)
- C(n, Y) = n! / (Y! · (n−Y)!)

Calcul:

P(n | Y) ∝ [ n! / (Y! (n−Y)!) ] · θ^Y · (1−θ)^(n−Y) · e^(−10) · 10^n / n!

n! se simplifică:

P(n | Y) ∝ [ 1 / (Y! (n−Y)!) ] · θ^Y · (1−θ)^(n−Y) · e^(−10) · 10^n

Scriem 10^n = 10^Y · 10^(n−Y). Tot ce nu depinde de n (θ^Y, e^(−10), 10^Y, 1/Y!) este constantă și se absoarbe în normalizare:

P(n | Y) ∝ [ 10 (1−θ) ]^(n−Y) / (n−Y)!,   n = Y, Y+1, Y+2, …

Aceasta este forma unei distribuții Poisson în variabila m = n − Y:

**n − Y | Y ~ Poisson(10 (1−θ))**, adică n = Y + m.

Media și varianța pentru Poisson(λ) sunt amândouă λ, deci:
- E[n | Y] = Y + 10 (1−θ)
- Var[n | Y] = 10 (1−θ)

Valori:

| θ | 10(1−θ) | Y=0 | Y=5 | Y=10 |
|---|---|---|---|---|
| 0.2 | 8 | media 8 | media 13 | media 18 |
| 0.5 | 5 | media 5 | media 10 | media 15 |

Varianța posterioară este 8 pentru θ=0.2 și 5 pentru θ=0.5 (indiferent de Y).
Valorile au fost verificate numeric (normalizare directă pe n = 0…199) și coincid cu formula.

## Efectul lui Y și θ asupra posteriorului

- **Efectul lui Y:** Y deplasează posteriorul. Media crește cu exact Y: la Y mai mare, posteriorul se mută spre dreapta cu aceeași cantitate. Forma (varianța) rămâne neschimbată. Mai mult, n nu poate fi mai mic decât Y (n ≥ Y), deci suportul distribuției începe de la Y.
- **Efectul lui θ:** θ controlează cât de împrăștiat și cât de deplasat este posteriorul peste Y. θ mai mare înseamnă 10(1−θ) mai mic, deci media peste Y este mai mică (5 față de 8) și varianța este mai mică (5 față de 8). Interpretare: dacă probabilitatea de cumpărare este mare, Y cumpărători observați implică un n apropiat de Y, deoarece sunt puțini clienți care nu au cumpărat. Dacă θ este mic, mulți clienți pot să nu cumpere, deci n poate fi cu mult mai mare decât Y.
- **Comparație cu priorul:** priorul Poisson(10) are media 10 și varianța 10. Posteriorul are varianța 10(1−θ) < 10, deci observarea lui Y reduce incertitudinea despre n. Când Y=0, posteriorul este Poisson(10(1−θ)), adică mai concentrat spre valori mici decât priorul.
