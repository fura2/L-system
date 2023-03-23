from l_system import LSystem, Turtle

l_system = LSystem(
    variables='XY',
    constants='F+-',
    axiom='X',
    rules={'X': '+YF-XFX-FY+', 'Y': '-XF+YFY+FX-'},
)

s = l_system.axiom
for n in range(8):
    width = 2 if n < 6 else 1 if n < 7 else 0.5
    turtle = Turtle(
        direction=0.0,
        move_rules={
            'F': Turtle.get_go_forward('navy', width),
            'X': Turtle.get_do_nothing(),
            'Y': Turtle.get_do_nothing(),
            '+': Turtle.get_turn(90.0),
            '-': Turtle.get_turn(-90.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/hilbert_curve_{n}.svg')
    s = l_system.step(s)
