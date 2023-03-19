from l_system import LSystem, Turtle

l_system = LSystem(
    variables='FG',
    constants='+-',
    axiom='G',
    rules={
        'F': 'FF-G-G+F+F-G-GF+G+FFG-F+G+FF+G-FG-G-F+F+GG-',
        'G': '+FF-G-G+F+FG+F-GG-F-G+FGG-F-GF+F+G-G-F+F+GG',
    },
)

s = l_system.axiom
for n in range(4):
    width = 2 if n < 2 else 1 if n < 3 else 0.5
    turtle = Turtle(
        direction=0.0,
        move_rules={
            'F': Turtle.get_go_forward('limegreen', width),
            'G': Turtle.get_go_forward('gold', width),
            '+': Turtle.get_turn(90.0),
            '-': Turtle.get_turn(-90.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/quadratic_gosper_curve_{n}.svg')
    s = l_system.step(s)
