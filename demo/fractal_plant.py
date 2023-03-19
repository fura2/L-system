from l_system import LSystem, Turtle

l_system = LSystem(
    variables='XF',
    constants='+-[]',
    axiom='X',
    rules={'X': 'F+[[X]-X]-F[-FX]+X', 'F': 'FF'},
)

s = l_system.axiom
for n in range(8):
    width = 2 if n < 4 else 1 if n < 7 else 0.5
    turtle = Turtle(
        direction=90.0,
        move_rules={
            'X': Turtle.get_do_nothing(),
            'F': Turtle.get_go_forward('green', width),
            '+': Turtle.get_turn(25.0),
            '-': Turtle.get_turn(-25.0),
            '[': Turtle.get_push(),
            ']': Turtle.get_pop(),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/fractal_plant_{n}.svg')
    s = l_system.step(s)
