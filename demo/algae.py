from l_system import LSystem

l_system = LSystem(
    variables='AB',
    constants='',
    axiom='A',
    rules={'A': 'AB', 'B': 'A'},
)

s = l_system.axiom
for n in range(8):
    print(f'n = {n}: {s}')
    s = l_system.step(s)
