from l_system import LSystem, Turtle

l_system = LSystem(
    variables='FGXY',
    constants='+-',
    axiom='F+G+X+Y',
    rules={'F': 'F+G', 'G': 'F-G', 'X': 'X+Y', 'Y': 'X-Y'},
)

s = l_system.axiom
for n in range(13):
    width = 2 if n < 9 else 1 if n < 12 else 0.5
    turtle = Turtle(
        direction=0.0,
        move_rules={
            'F': Turtle.get_go_forward('red', width),
            'G': Turtle.get_go_forward('red', width),
            'X': Turtle.get_go_forward('blue', width),
            'Y': Turtle.get_go_forward('blue', width),
            '+': Turtle.get_turn(90.0),
            '-': Turtle.get_turn(-90.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/twin_dragon_{n}.svg')
    s = l_system.step(s)
