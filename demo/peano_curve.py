from l_system import LSystem, Turtle

l_system = LSystem(
    variables='AB',
    constants='F+-',
    axiom='A',
    rules={'A': 'AFBFA-F-BFAFB+F+AFBFA', 'B': 'BFAFB+F+AFBFA-F-BFAFB'},
)

s = l_system.axiom
for n in range(5):
    width = 2 if n < 3 else 1 if n < 4 else 0.5
    turtle = Turtle(
        direction=90.0,
        move_rules={
            'A': Turtle.get_do_nothing(),
            'B': Turtle.get_do_nothing(),
            'F': Turtle.get_go_forward('orchid', width),
            '+': Turtle.get_turn(90.0),
            '-': Turtle.get_turn(-90.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/peano_curve_{n}.svg')
    s = l_system.step(s)
