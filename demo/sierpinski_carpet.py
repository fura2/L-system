from l_system import LSystem, Turtle

l_system = LSystem(
    variables='FfX',
    constants='+-',
    axiom='F+F+F+F+X',
    rules={'F': 'FFF', 'f': 'fff', 'X': 'XfXfX+fF++ff-f-fF++ff-f-f-XfFX++ff-f-XfXFX++ff+ff+'},
)

s = l_system.axiom
for n in range(5):
    width = 2 if n < 3 else 1
    turtle = Turtle(
        direction=0.0,
        move_rules={
            'F': Turtle.get_go_forward('deepskyblue', width),
            'f': Turtle.get_go_forward_without_drawing(),
            'X': Turtle.get_point_a_dot('blue'),
            '+': Turtle.get_turn(90.0),
            '-': Turtle.get_turn(-90.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/sierpinski_carpet_{n}.svg')
    s = l_system.step(s)
