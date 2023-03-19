from l_system import LSystem, Turtle

l_system = LSystem(
    variables='X',
    constants='F+-',
    axiom='F+XF+F+XF',
    rules={'X': 'XF-F+F-XF+F+XF-F+F-X'},
)

s = l_system.axiom
for n in range(6):
    width = 2 if n < 3 else 1 if n < 5 else 0.5
    turtle = Turtle(
        direction=0.0,
        move_rules={
            'X': Turtle.get_do_nothing(),
            'F': Turtle.get_go_forward('slateblue', width),
            '+': Turtle.get_turn(90.0),
            '-': Turtle.get_turn(-90.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/sierpinski_square_curve_{n}.svg')
    s = l_system.step(s)
