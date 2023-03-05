'''Fractional binary tree'''
from l_system import LSystem, Pose, Segment, Turtle


l_system = LSystem(
    variables='01',
    constants='[]',
    axiom='0',
    rules={'0': '1[0]0', '1': '11'},
)

def push_and_turn_left(pose: Pose, stack: list[Pose], trajectory: list[Segment]) -> Pose:
    new_pose = Turtle.get_push()(pose, stack, trajectory)
    return Turtle.get_turn(45.0)(new_pose, stack, trajectory)

def pop_and_turn_right(pose: Pose, stack: list[Pose], trajectory: list[Segment]) -> Pose:
    new_pose = Turtle.get_pop()(pose, stack, trajectory)
    return Turtle.get_turn(-45.0)(new_pose, stack, trajectory)

s = l_system.axiom
for n in range(6):
    turtle = Turtle(
        direction=90.0,
        move_rules={
            '0': Turtle.get_go_forward('green'),
            '1': Turtle.get_go_forward('brown'),
            '[': push_and_turn_left,
            ']': pop_and_turn_right,
        },
    )
    turtle.move(s)
    if 3 <= n <= 5:
        turtle.show_and_save(f'n = {n}', output_path=f'resource/bintree_{n}.png')
    s = l_system.step(s)
