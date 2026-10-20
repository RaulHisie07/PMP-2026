from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from math import comb

model = DiscreteBayesianNetwork([
    ('S', 'M'),
    ('N', 'M'),
    ('S', 'W'),
    ('N', 'W'),
    ('M', 'W')
])

cpd_s = TabularCPD('S', 2, [[0.5], [0.5]])

cpd_n = TabularCPD('N', 6, [[1/6]] * 6)

valori_m = []

for m in range(13):
    linie = []

    for s in range(2):
        for n in range(1, 7):

            p = 4/7 if s == 0 else 0.5

            if m <= 2*n:
                prob = comb(2*n, m) * p**m * (1-p)**(2*n-m)
            else:
                prob = 0

            linie.append(prob)

    valori_m.append(linie)

cpd_m = TabularCPD(
    'M', 13, valori_m,
    evidence=['S', 'N'],
    evidence_card=[2, 6]
)

valori_w = [[], []]

for s in range(2):
    for n in range(1, 7):
        for m in range(13):

            castigator = s if n >= m else 1-s

            valori_w[0].append(1 if castigator == 0 else 0)
            valori_w[1].append(1 if castigator == 1 else 0)

cpd_w = TabularCPD(
    'W', 2, valori_w,
    evidence=['S', 'N', 'M'],
    evidence_card=[2, 6, 13]
)

model.add_cpds(cpd_s, cpd_n, cpd_m, cpd_w)

print(model.check_model())

#c

inference = VariableElimination(model)

rezultat = inference.query(
    variables=['S'],
    evidence={'M': 1}
)

print(rezultat)