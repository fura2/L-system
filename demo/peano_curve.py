from l_system import LSystem, Turtle

l_system = LSystem(
    variables='XY',
    constants='F+-',
    axiom='X',
    rules={'X': 'XFYFX-F-YFXFY+F+XFYFX', 'Y': 'YFXFY+F+XFYFX-F-YFXFY'},
)

s = l_system.axiom
for n in range(5):
    width = 2 if n < 3 else 1 if n < 4 else 0.5
    turtle = Turtle(
        direction=90.0,
        move_rules={
            'F': Turtle.get_go_forward('orchid', width),
            'X': Turtle.get_do_nothing(),
            'Y': Turtle.get_do_nothing(),
            '+': Turtle.get_turn(90.0),
            '-': Turtle.get_turn(-90.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/peano_curve_{n}.svg')
    s = l_system.step(s)
