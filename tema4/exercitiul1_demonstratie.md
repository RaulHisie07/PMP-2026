# Exercitiul 1

**a)** $A\perp C\mid B$: daca stim B, cunoasterea lui C nu mai schimba
probabilitatea lui A:

$$P(a\mid b,c)=P(a\mid b).$$

**b)** Din independenta conditionata:

$$P(a,b,c)=P(a,c\mid b)P(b)=P(a\mid b)P(c\mid b)P(b).$$

Alegem:

$$\phi_{AB}(a,b)=P(a\mid b)P(b),\qquad
\phi_{BC}(b,c)=P(c\mid b),\qquad Z=1.$$

Atunci $P(a,b,c)=Z^{-1}\phi_{AB}(a,b)\phi_{BC}(b,c)$.
Potentialele sunt strict pozitive deoarece distributia este strict pozitiva.

**c)** Presupunem factorizarea si notam:

$$U(b)=\sum_a\phi_{AB}(a,b),\qquad
V(b)=\sum_c\phi_{BC}(b,c).$$

Insumand dupa a si c:

$$P(b)=Z^{-1}U(b)V(b).$$

Prin urmare:

$$P(a,c\mid b)=\frac{P(a,b,c)}{P(b)}
=\frac{\phi_{AB}(a,b)}{U(b)}\frac{\phi_{BC}(b,c)}{V(b)}.$$

Insumand dupa c, respectiv dupa a:

$$P(a\mid b)=\frac{\phi_{AB}(a,b)}{U(b)},\qquad
P(c\mid b)=\frac{\phi_{BC}(b,c)}{V(b)}.$$

Rezulta $P(a,c\mid b)=P(a\mid b)P(c\mid b)$, deci $A\perp C\mid B$.
