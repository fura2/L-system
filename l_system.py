from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional, TypeAlias, Union

import matplotlib.pyplot as plt  # type: ignore
import numpy as np
from matplotlib.collections import LineCollection, PatchCollection  # type: ignore


class LSystem:
    '''Definition of an L-system'''

    Alphabet: TypeAlias = str
    String: TypeAlias = str  # sequence of Alphabets

    def __init__(self, variables: String, constants: String, axiom: String, rules: dict[Alphabet, String]) -> None:
        self.variables = variables
        self.constants = constants
        self.axiom = axiom
        self.rules = rules

        for c in self.variables:
            assert c in self.rules
        for c in self.constants:
            assert c not in self.rules
            self.rules[c] = c

    def step(self, s: String) -> String:
        return ''.join(self.rules[c] for c in s)


@dataclass(frozen=True)
class Point:
    x: float
    y: float


@dataclass(frozen=True)
class Pose:
    position: Point
    direction: float  # degree


# matplotlib-style color
# https://matplotlib.org/stable/tutorials/colors/colors.html
Color = Union[str, tuple[float, float, float], tuple[float, float, float, float]]


@dataclass(frozen=True)
class Dot:
    point: Point
    color: Color
    radius: float


@dataclass(frozen=True)
class Line:
    from_: Point
    to: Point
    color: Color
    width: float


Figure = Union[Dot, Line]


class Turtle:
    '''A mapping from an L-system string to a 2D graphic'''

    # (pose, stack (updated in-place), set of figures drawn (updated in-place)) -> new pose
    Move: TypeAlias = Callable[[Pose, list[Pose], list[Figure]], Pose]

    def __init__(self, direction: float, move_rules: dict[LSystem.Alphabet, Move]) -> None:
        self.pose = Pose(Point(0.0, 0.0), direction)
        self.move_rules = move_rules
        self.stack = []  # type: list[Pose]
        self.figures = []  # type: list[Figure]

    def move(self, s: LSystem.String) -> None:
        for c in s:
            self.pose = self.move_rules[c](self.pose, self.stack, self.figures)

    def _prepare_image(self, title: Optional[str] = None) -> None:
        dots = [dot for dot in self.figures if isinstance(dot, Dot)]
        lines = [line for line in self.figures if isinstance(line, Line)]

        margin = 3.0
        if len(self.figures) == 0:
            x_min = y_min = -margin
            x_max = y_max = margin
        else:
            x_min = min([dot.point.x for dot in dots] +
                        [line.from_.x for line in lines] +
                        [line.to.x for line in lines]) - margin
            x_max = max([dot.point.x for dot in dots] +
                        [line.from_.x for line in lines] +
                        [line.to.x for line in lines]) + margin
            y_min = min([dot.point.y for dot in dots] +
                        [line.from_.y for line in lines] +
                        [line.to.y for line in lines]) - margin
            y_max = max([dot.point.y for dot in dots] +
                        [line.from_.y for line in lines] +
                        [line.to.y for line in lines]) + margin

        plt.rcParams['svg.fonttype'] = 'none'
        fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
        if title is not None:
            fig.suptitle(title, fontsize=16)
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.add_collection(LineCollection(
            [[[line.from_.x, line.from_.y], [line.to.x, line.to.y]] for line in lines],
            colors=[line.color for line in lines],
            linewidths=[line.width for line in lines],
            zorder=2,
        ))
        ax.add_collection(PatchCollection(
            [plt.Circle([dot.point.x, dot.point.y], dot.radius) for dot in dots],
            facecolors=[dot.color for dot in dots],
            zorder=3,
        ))
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=0.9)

    def show(self, title: Optional[str] = None) -> None:
        self._prepare_image(title)
        plt.show()

    def save(self, title: Optional[str] = None, *, output_path: Path) -> None:
        self._prepare_image(title)
        plt.savefig(output_path)

    def show_and_save(self, title: Optional[str] = None, *, output_path: Path) -> None:
        self._prepare_image(title)
        plt.savefig(output_path)
        plt.show()

    # pre-defined moves
    @classmethod
    def get_go_forward(cls, color: Color, width: float = 1.0) -> Move:
        '''Go forward with drawing'''
        def go_forward(pose: Pose, stack: list[Pose], figures: list[Figure]) -> Pose:
            theta = np.radians(pose.direction)
            new_point = Point(pose.position.x + np.cos(theta), pose.position.y + np.sin(theta))
            figures.append(Line(pose.position, new_point, color, width))
            return Pose(new_point, pose.direction)
        return go_forward

    @classmethod
    def get_go_forward_without_drawing(cls) -> Move:
        '''Go forward without drawing'''
        def go_forward_without_drawing(pose: Pose, stack: list[Pose], figures: list[Figure]) -> Pose:
            theta = np.radians(pose.direction)
            new_point = Point(pose.position.x + np.cos(theta), pose.position.y + np.sin(theta))
            return Pose(new_point, pose.direction)
        return go_forward_without_drawing

    @classmethod
    def get_point_a_dot(cls, color: Color, radius: float = 0.1) -> Move:
        '''Point a dot'''
        def point_a_dot(pose: Pose, stack: list[Pose], figures: list[Figure]) -> Pose:
            figures.append(Dot(pose.position, color, radius))
            return pose
        return point_a_dot

    @classmethod
    def get_turn(cls, angle: float) -> Move:
        '''Turn {angle} degrees to the left'''
        def turn(pose: Pose, stack: list[Pose], figures: list[Figure]) -> Pose:
            return Pose(pose.position, pose.direction + angle)
        return turn

    @classmethod
    def get_do_nothing(cls) -> Move:
        '''Do nothing'''
        def do_nothing(pose: Pose, stack: list[Pose], figures: list[Figure]) -> Pose:
            return pose
        return do_nothing

    @classmethod
    def get_push(cls) -> Move:
        '''Push the current pose on the stack'''
        def push(pose: Pose, stack: list[Pose], figures: list[Figure]) -> Pose:
            stack.append(pose)
            return pose
        return push

    @classmethod
    def get_pop(cls) -> Move:
        '''Pop a pose from the stack'''
        def pop(pose: Pose, stack: list[Pose], figures: list[Figure]) -> Pose:
            return stack.pop()
        return pop
