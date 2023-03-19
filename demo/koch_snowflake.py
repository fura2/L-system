'''Koch snowflake'''
from l_system import LSystem, Turtle

l_system = LSystem(
    variables='F',
    constants='+-',
    axiom='F--F--F',
    rules={'F': 'F+F--F+F'},
)

s = l_system.axiom
for n in range(6):
    width = 2 if n < 4 else 1 if n < 5 else 0.5
    turtle = Turtle(
        direction=60.0,
        move_rules={
            'F': Turtle.get_go_forward('dodgerblue', width),
            '+': Turtle.get_turn(60.0),
            '-': Turtle.get_turn(-60.0),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/koch_snowflake_{n}.svg')
    s = l_system.step(s)
