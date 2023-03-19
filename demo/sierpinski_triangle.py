from l_system import LSystem, Turtle

l_system = LSystem(
    variables='FG',
    constants='+-',
    axiom='F-G-G',
    rules={'F': 'F-G+F+G-F', 'G': 'GG'},
)

s = l_system.axiom
for n in range(6):
    width = 2 if n < 3 else 1 if n < 5 else 0.5
    turtle = Turtle(
        direction=60.0,
        move_rules={
            'F': Turtle.get_go_forward('red', width),
            'G': Turtle.get_go_forward('gold', width),
            '+': Turtle.get_turn(120.0),
            '-': Turtle.get_turn(-120.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/sierpinski_triangle_{n}.svg')
    s = l_system.step(s)
