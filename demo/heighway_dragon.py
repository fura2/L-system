from l_system import LSystem, Turtle


l_system = LSystem(
    variables='FG',
    constants='+-',
    axiom='F',
    rules={'F': 'F+G', 'G': 'F-G'},
)

s = l_system.axiom
for n in range(15):
    turtle = Turtle(
        direction=0.0,
        move_rules={
            'F': Turtle.get_go_forward('red'),
            'G': Turtle.get_go_forward('forestgreen'),
            '+': Turtle.get_turn(90.0),
            '-': Turtle.get_turn(-90.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/heighway_dragon_{n}.png')
    s = l_system.step(s)
