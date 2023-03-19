from l_system import LSystem, Turtle

l_system = LSystem(
    variables='FG',
    constants='+-',
    axiom='F',
    rules={'F': 'G-F-G', 'G': 'F+G+F'},
)

s = l_system.axiom
for n in range(9):
    width = 2 if n < 5 else 1 if n < 7 else 0.5
    turtle = Turtle(
        direction=0.0,
        move_rules={
            'F': Turtle.get_go_forward('red', width),
            'G': Turtle.get_go_forward('blue', width),
            '+': Turtle.get_turn(60.0),
            '-': Turtle.get_turn(-60.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/sierpinski_arrowhead_curve_{n}.svg')
    s = l_system.step(s)
