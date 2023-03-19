from l_system import LSystem, Turtle

l_system = LSystem(
    variables='12345',
    constants='+-',
    axiom='1+2+3+4+5',
    rules={
        '1': '1+1-1--1+1+1',
        '2': '2+2-2--2+2+2',
        '3': '3+3-3--3+3+3',
        '4': '4+4-4--4+4+4',
        '5': '5+5-5--5+5+5',
    },
)

s = l_system.axiom
for n in range(6):
    width = 2 if n < 3 else 1 if n < 4 else 0.5
    turtle = Turtle(
        direction=0.0,
        move_rules={
            '1': Turtle.get_go_forward('red', width),
            '2': Turtle.get_go_forward('gold', width),
            '3': Turtle.get_go_forward('limegreen', width),
            '4': Turtle.get_go_forward('blue', width),
            '5': Turtle.get_go_forward('darkviolet', width),
            '+': Turtle.get_turn(72.0),
            '-': Turtle.get_turn(-72.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/pentadendrite_{n}.svg')
    s = l_system.step(s)
