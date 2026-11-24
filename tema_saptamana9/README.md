# Tema 7 – Laboratorul 8: Inferență Bayesiană cu PyMC

Setări MCMC în PyMC: Ex1 și Ex2: 4 lanțuri × 5000 eșantioane. Ex3: 4 lanțuri × 5000 eșantioane (tune = 2000).
Valorile numerice de mai jos sunt calculate exact / numeric; rezultatele din PyMC vor fi foarte apropiate (diferențe mici datorate zgomotului MCMC). Completează-le cu ce afișează scripturile tale.

---

## Exercițiul 1

**Calcul exact.**  Formula hipergeometrică:  P(Y=y | N) = C(M,y) · C(N−M, n−y) / C(N,n)

Cu M=20, n=15, y=4:

P(Y=4 | N) = C(20,4) · C(N−20, 11) / C(N,15),   C(20,4) = 4845

Prior uniform: P(N) = 1/181 pentru N = 20,…,200 (constantă, se simplifică).

Posterior (Bayes):

P(N | Y=4) = P(Y=4 | N) · P(N) / Σ_N' P(Y=4 | N') · P(N')  ∝  C(N−20, 11) / C(N,15)

Se anulează pentru N < 31 (nu se pot extrage 11 nemarcate din N−20 < 11). Deci N ∈ {31,…,200}.

**b)** Formula mediei: E[N | Y] = Σ N · P(N | Y)

- media a posteriori ≈ **102.6**
- mediana = **95**
- HDI 95% = **[44, 180]**
- estimarea clasică: M·n/Y = 20·15/4 = **75** (aceasta e și modul posteriorului, 74).

Media posterioară (102.6) e mai mare decât 75, deoarece posteriorul este asimetric la dreapta (coadă lungă spre N mare).

**c)** Formula: P(N > 100 | Y) = Σ_{N=101}^{200} P(N | Y)  ≈ **0.449**

**d)** Formula predictivă: P(Y' = k | Y) = Σ_N P(Y'=k | N) · P(N | Y), unde Y' | N ~ Hypergeometric(N, 20, 15).

| k | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| P(Y'=k) | 0.042 | 0.127 | 0.194 | 0.207 | 0.173 | 0.122 | 0.073 | 0.038 |

E[Y'] ≈ 3.34.

Diferența: posteriorul lui N descrie incertitudinea despre un **parametru** (mărimea populației, valori 31–200), iar distribuția predictivă descrie un **număr observabil viitor** (0–15 animale marcate), care mai include și variabilitatea de eșantionare a capturii.

Grafice: `ex1_posterior_N.png`, `ex1_predictiv.png`

---

## Exercițiul 2

**Posterior (conjugare Gamma–Exponențial).**

Verosimilitatea (n observații): L(λ) = Π λ e^{−λ x_i} = λ^n · e^{−λ S},  S = Σ x_i

Priorul Gamma(α, β) (formă–rată): p(λ) ∝ λ^{α−1} e^{−βλ}

Posterior: p(λ | x) ∝ λ^{n+α−1} · e^{−(β+S)λ}  →  **λ | x ~ Gamma(α + n, β + S)**

Date:
- A: n = 8, S_A = 3.2+4.1+2.8+5.0+3.7+4.5+3.0+3.9 = **30.2**
- B: n = 8, S_B = 2.1+2.8+3.4+2.5+3.0+2.2+3.6+2.7 = **22.3**

Posteriori:
- λ_A | A ~ Gamma(2+8, 4+30.2) = **Gamma(10, 34.2)**
- λ_B | B ~ Gamma(2+8, 4+22.3) = **Gamma(10, 26.3)**

**b)** Pentru λ ~ Gamma(α, β), media lui 1/λ este β/(α−1):

- E[1/λ_A] = 34.2 / 9 = **3.80** zile, HDI 95% ≈ **[1.74, 6.45]**
- E[1/λ_B] = 26.3 / 9 = **2.92** zile, HDI 95% ≈ **[1.32, 4.95]**

**c)** Scriem λ_A = G_A / 34.2, λ_B = G_B / 26.3, cu G_A, G_B ~ Gamma(10, 1) independente.

λ_B > λ_A  ⇔  G_B / G_A > 26.3 / 34.2 = 0.769

G_B/G_A ~ F(20, 20) (Gamma(10,1) = χ²(20)/2, ratio de χ² cu 20 grade de libertate), deci

P(1/λ_B < 1/λ_A) = P(λ_B > λ_A) = P(F(20,20) > 0.769) ≈ **0.719**

**d)** Predictiv pentru un pacient nou: X_nou | date ~ Lomax (exponențială cu rată Gamma). Formula:

P(X_B < X_A) = E[ λ_B / (λ_A + λ_B) ]  (integrată peste posteriori)

Estimare: ≈ **0.562**.

Explicație: la c) se compară **parametrii** (mediile), iar posteriorii sunt concentrați → probabilitate mare (0.72). La d) se compară **doi timpi individuali**, fiecare cu variabilitatea mare a unei exponențiale (abatere standard = medie), deci suprapunerea este mare și probabilitatea scade spre 0.5 (0.56). Chiar dacă știm sigur că B e mai rapid în medie, un pacient individual cu B poate fi mai lent decât unul cu A.

Grafic: `ex2_timpi_medii.png`

---

## Exercițiul 3

Modelul: Y_t ~ Poisson(λ_t), cu λ_t = λ1 + (λ2 − λ1) · sigmoid(k (t − τ)).

Semnificația parametrilor:
- λ1 = nivelul inițial al ratei (solicitări/zi, la începutul perioadei),
- λ2 = nivelul final al ratei,
- τ = ziua centrală a tranziției (când λ_t = (λ1+λ2)/2),
- k = rapiditatea schimbării (k mare → salt brusc, k mic → tranziție lentă/graduală).

Rezultate (calculate cu un MCMC Metropolis de verificare; PyMC dă valori apropiate):

| parametru | medie posterioară | HDI 95% |
|---|---|---|
| λ1 | ≈ 2.9 | ≈ [0.6, 4.7] |
| λ2 | ≈ 9.8 | ≈ [7.0, 13.9] |
| τ | ≈ 16.0 | ≈ [9.4, 23.5] |
| k | ≈ 0.51 | ≈ [0.05, 1.47] |

**c)** P(λ2 > λ1 | Y) ≈ **1.0** (practic toate eșantioanele). Rata crește clar de la ~3 la ~10 solicitări pe zi.

**d)** Predictiv: pentru fiecare eșantion posterior se calculează λ_t și se simulează Y_t ~ Poisson(λ_t). Interpretare: modelul reproduce creșterea graduală (trend de la ~3 la ~10), iar datele observate se încadrează în mare parte în intervalul predictiv de 95%. HDI-ul larg pentru τ și k arată că datele nu fixează precis momentul și rapiditatea tranziției (k mic ⇒ schimbare graduală, nu salt).

Grafice: `ex3_tau.png`, `ex3_k.png`, `ex3_lambda_t.png`, `ex3_predictiv.png`
