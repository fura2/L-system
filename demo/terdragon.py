from l_system import LSystem, Turtle


l_system = LSystem(
    variables='FGH',
    constants='+-',
    axiom='F+G-H',
    rules={'F': 'F+F-F', 'G': 'G+G-G', 'H': 'H+H-H'},
)

s = l_system.axiom
for n in range(9):
    turtle = Turtle(
        direction=0.0,
        move_rules={
            'F': Turtle.get_go_forward('red'),
            'G': Turtle.get_go_forward('green'),
            'H': Turtle.get_go_forward('blue'),
            '+': Turtle.get_turn(120.0),
            '-': Turtle.get_turn(-120.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/terdragon_{n}.png')
    s = l_system.step(s)
