from l_system import LSystem

l_system = LSystem(
    variables='01',
    constants='',
    axiom='0',
    rules={'0': '01', '1': '10'},
)

s = l_system.axiom
for n in range(7):
    print(f'n = {n}: {s}')
    s = l_system.step(s)
