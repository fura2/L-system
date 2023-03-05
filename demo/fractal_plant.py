from l_system import LSystem, Turtle

l_system = LSystem(
    variables='XF',
    constants='+-[]',
    axiom='X',
    rules={'X': 'F+[[X]-X]-F[-FX]+X', 'F': 'FF'},
)

s = l_system.axiom
for n in range(9):
    turtle = Turtle(
        direction=90.0,
        move_rules={
            'X': Turtle.get_do_nothing(),
            'F': Turtle.get_go_forward('green'),
            '+': Turtle.get_turn(25.0),
            '-': Turtle.get_turn(-25.0),
            '[': Turtle.get_push(),
            ']': Turtle.get_pop(),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/fractal_plant_{n}.png')
    s = l_system.step(s)
