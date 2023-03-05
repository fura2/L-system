from l_system import LSystem, Turtle


l_system = LSystem(
    variables='AB',
    constants='',
    axiom='A',
    rules={'A': 'ABA', 'B': 'BBB'},
)

s = l_system.axiom
for n in range(6):
    turtle = Turtle(
        direction=0.0,
        move_rules={
            'A': Turtle.get_go_forward('blue'),
            'B': Turtle.get_go_forward_without_drawing(),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/cantor_set_{n}.png')
    s = l_system.step(s)
