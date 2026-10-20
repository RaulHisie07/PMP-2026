from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('B', 'T'),
    ('B', 'X'),
    ('B', 'D'),
    ('T', 'D')
])

cpd_b = TabularCPD(
    'B', 2,
    [[0.9], [0.1]]
)

cpd_t = TabularCPD(
    'T', 2,
    [[0.7, 0.2],
     [0.3, 0.8]],
    evidence=['B'],
    evidence_card=[2]
)

cpd_x = TabularCPD(
    'X', 2,
    [[0.9, 0.1],
     [0.1, 0.9]],
    evidence=['B'],
    evidence_card=[2]
)

cpd_d = TabularCPD(
    'D', 2,
    [[0.9, 0.5, 0.5, 0.1],
     [0.1, 0.5, 0.5, 0.9]],
    evidence=['B', 'T'],
    evidence_card=[2, 2]
)

model.add_cpds(cpd_b, cpd_t, cpd_x, cpd_d)

print(model.check_model())


# punctul b

inference = VariableElimination(model)

rezultat = inference.query(
    variables=['B'],
    evidence={'T': 1, 'D': 1}
)

print(rezultat)

#punctul c

rezultat = inference.query(
    variables=['X'],
    evidence={'B': 0}
)

print(rezultat)