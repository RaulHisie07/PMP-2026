from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('C', 'H'),
    ('P', 'H')
])

cpd_c = TabularCPD('C', 3, [[1/3], [1/3], [1/3]])
cpd_p = TabularCPD('P', 3, [[1/3], [1/3], [1/3]])

valori = []

for c in range(3):
    for p in range(3):
        usi = [h for h in range(3) if h != c and h != p]

        for h in range(3):
            if h in usi:
                valori.append(1 / len(usi))
            else:
                valori.append(0)

cpd_h = TabularCPD(
    'H', 3,
    [valori[0::3], valori[1::3], valori[2::3]],
    evidence=['C', 'P'],
    evidence_card=[3, 3]
)

model.add_cpds(cpd_c, cpd_p, cpd_h)

inference = VariableElimination(model)

rezultat = inference.query(
    variables=['C'],
    evidence={'P': 0, 'H': 2}
)

print(rezultat)