from l_system import LSystem, Turtle

l_system = LSystem(
    variables='Ff',
    constants='',
    axiom='F',
    rules={'F': 'FfF', 'f': 'fff'},
)

s = l_system.axiom
for n in range(6):
    turtle = Turtle(
        direction=0.0,
        move_rules={
            'F': Turtle.get_go_forward('blue', 2),
            'f': Turtle.get_go_forward_without_drawing(),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/cantor_set_{n}.svg')
    s = l_system.step(s)
