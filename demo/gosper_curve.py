from l_system import LSystem, Turtle

l_system = LSystem(
    variables='AB',
    constants='+-',
    axiom='A',
    rules={'A': 'A-B--B+A++AA+B-', 'B': '+A-BB--B-A++A+B'},
)

s = l_system.axiom
for n in range(6):
    turtle = Turtle(
        direction=90.0,
        move_rules={
            'A': Turtle.get_go_forward('limegreen'),
            'B': Turtle.get_go_forward('blue'),
            '+': Turtle.get_turn(60.0),
            '-': Turtle.get_turn(-60.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/gosper_curve_{n}.png')
    s = l_system.step(s)
