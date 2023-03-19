from l_system import LSystem, Turtle

l_system = LSystem(
    variables='FG',
    constants='+-',
    axiom='F',
    rules={'F': 'F+G', 'G': 'F-G'},
)

s = l_system.axiom
for n in range(14):
    width = 2 if n < 10 else 1 if n < 13 else 0.5
    turtle = Turtle(
        direction=0.0,
        move_rules={
            'F': Turtle.get_go_forward('red', width),
            'G': Turtle.get_go_forward('limegreen', width),
            '+': Turtle.get_turn(90.0),
            '-': Turtle.get_turn(-90.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/heighway_dragon_{n}.svg')
    s = l_system.step(s)
