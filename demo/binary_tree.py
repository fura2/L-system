from l_system import Figure, LSystem, Pose, Turtle

l_system = LSystem(
    variables='01',
    constants='[]',
    axiom='0',
    rules={'0': '1[0]0', '1': '11'},
)


def push_and_turn_left(pose: Pose, stack: list[Pose], figures: list[Figure]) -> Pose:
    new_pose = Turtle.get_push()(pose, stack, figures)
    return Turtle.get_turn(45.0)(new_pose, stack, figures)


def pop_and_turn_right(pose: Pose, stack: list[Pose], figures: list[Figure]) -> Pose:
    new_pose = Turtle.get_pop()(pose, stack, figures)
    return Turtle.get_turn(-45.0)(new_pose, stack, figures)


s = l_system.axiom
for n in range(8):
    turtle = Turtle(
        direction=90.0,
        move_rules={
            '0': Turtle.get_go_forward('green', 2),
            '1': Turtle.get_go_forward('brown', 2),
            '[': push_and_turn_left,
            ']': pop_and_turn_right,
        },
    )
    turtle.move(s)
    turtle.show_and_save(f'n = {n}', output_path=f'resource/binary_tree_{n}.svg')
    s = l_system.step(s)
