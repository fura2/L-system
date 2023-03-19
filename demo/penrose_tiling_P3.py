from l_system import LSystem, Turtle

l_system = LSystem(
    variables='F1234',
    constants='+-[]',
    axiom='[2]++[2]++[2]++[2]++[2]',
    rules={
        'F': '',
        '1': '3F++4F----2F[-3F----1F]++',
        '2': '+3F--4F[---1F--2F]+',
        '3': '-1F++2F[+++3F++4F]-',
        '4': '--3F++++1F[+4F++++2F]--2F',
    },
)


s = l_system.axiom
for n in range(7):
    width = 2 if n < 4 else 1 if n < 6 else 0.5
    turtle = Turtle(
        direction=0.0,
        move_rules={
            'F': Turtle.get_go_forward('darkkhaki', width),
            '1': Turtle.get_do_nothing(),
            '2': Turtle.get_do_nothing(),
            '3': Turtle.get_do_nothing(),
            '4': Turtle.get_do_nothing(),
            '+': Turtle.get_turn(36.0),
            '-': Turtle.get_turn(-36.0),
            '[': Turtle.get_push(),
            ']': Turtle.get_pop(),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/penrose_tiling_P3_{n}.svg')
    s = l_system.step(s)
