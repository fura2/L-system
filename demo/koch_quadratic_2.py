from l_system import LSystem, Turtle

l_system = LSystem(
    variables='F',
    constants='+-',
    axiom='F',
    rules={'F': 'F+F-F-FF+F+F-F'},
)

s = l_system.axiom
for n in range(5):
    width = 2 if n < 3 else 1 if n < 4 else 0.5
    turtle = Turtle(
        direction=0.0,
        move_rules={
            'F': Turtle.get_go_forward('blue', width),
            '+': Turtle.get_turn(90.0),
            '-': Turtle.get_turn(-90.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/koch_quadratic_2_{n}.svg')
    s = l_system.step(s)
