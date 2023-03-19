from l_system import LSystem, Turtle

l_system = LSystem(
    variables='16789',
    constants='+-[]',
    axiom='[7]++[7]++[7]++[7]++[7]',
    rules={
        '1': '',
        '6': '81++91----71[-81----61]++',
        '7': '+81--91[---61--71]+',
        '8': '-61++71[+++81++91]-',
        '9': '--81++++61[+91++++71]--71',
    },
)

s = l_system.axiom
for n in range(7):
    width = 2 if n < 4 else 1 if n < 6 else 0.5
    turtle = Turtle(
        direction=0.0,
        move_rules={
            '1': Turtle.get_go_forward('Olive', width),
            '6': Turtle.get_do_nothing(),
            '7': Turtle.get_do_nothing(),
            '8': Turtle.get_do_nothing(),
            '9': Turtle.get_do_nothing(),
            '+': Turtle.get_turn(36.0),
            '-': Turtle.get_turn(-36.0),
            '[': Turtle.get_push(),
            ']': Turtle.get_pop(),
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/penrose_tiling_P3_{n}.svg')
    s = l_system.step(s)
