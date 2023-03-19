from l_system import LSystem, Turtle

l_system = LSystem(
    variables='FG',
    constants='+-',
    axiom='F',
    rules={'F': 'F-G--G+F++FF+G-', 'G': '+F-GG--G-F++F+G'},
)

s = l_system.axiom
for n in range(6):
    width = 2 if n < 4 else 1 if n < 5 else 0.5
    turtle = Turtle(
        direction=90.0,
        move_rules={
            'F': Turtle.get_go_forward('limegreen', width),
            'G': Turtle.get_go_forward('blue', width),
            '+': Turtle.get_turn(60.0),
            '-': Turtle.get_turn(-60.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/hexagonal_gosper_curve_{n}.svg')
    s = l_system.step(s)
