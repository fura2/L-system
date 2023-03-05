from l_system import LSystem, Turtle


l_system = LSystem(
    variables='XY',
    constants='F+-',
    axiom='XF',
    rules={'X': 'YF+XF+Y', 'Y': 'XF-YF-X'},
)

s = l_system.axiom
for n in range(6):
    turtle = Turtle(
        direction=0.0,
        move_rules={
            'X': Turtle.get_do_nothing(),
            'Y': Turtle.get_do_nothing(),
            'F': Turtle.get_go_forward('green'),
            '+': Turtle.get_turn(60.0),
            '-': Turtle.get_turn(-60.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/sierpinski_arrowhead_curve_2_{n}.png')
    s = l_system.step(s)
