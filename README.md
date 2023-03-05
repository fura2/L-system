# L-system

A simulator of [L-systems](https://en.wikipedia.org/wiki/L-system) written in Python

## Demo
### 1. Algae <span style="font-size:small">([Wikipedia Example 1](https://en.wikipedia.org/wiki/L-system#Example_1:_Algae))</span>
[code](demo/demo1.py)

#### L-system
- variables: `A`, `B`
- constants: none
- axiom: `A`
- rules: `A→AB`, `B→A`

#### Results
```
n = 0: A
n = 1: AB
n = 2: ABA
n = 3: ABAAB
n = 4: ABAABABA
n = 5: ABAABABAABAAB
n = 6: ABAABABAABAABABAABABA
n = 7: ABAABABAABAABABAABABAABAABABAABAAB
```

### 2. Fractal binary tree <span style="font-size:small">([Wikipedia Example 2](https://en.wikipedia.org/wiki/L-system#Example_2:_Fractal_(binary)_tree))</span>
[code](demo/demo2.py)

#### L-system
- variables: `0`, `1`
- constants: `[`, `]`
- axiom: `0`
- rules: `1→11`, `0→1[0]0`

#### Drawing rules
- `0`: go forward with drawing a green segment
- `1`: go forward with drawing a brown segment
- `[`: push the current pose on the stack, turn 45° to the left
- `[`: pop a pose from the stack, turn 45° to the right

#### Results
<img src="resource/bintree_3.png" width="33%">
<img src="resource/bintree_4.png" width="33%">
<img src="resource/bintree_5.png" width="33%">

### 3. Cantor set <span style="font-size:small">([Wikipedia Example 3](https://en.wikipedia.org/wiki/L-system#Example_3:_Cantor_set))</span>
[code](demo/demo3.py)

#### L-system
- variables: `A`, `B`
- constants: none
- axiom: `A`
- rules: `A→ABA`, `B→BBB`

#### Drawing rules
- `A`: go forward with drawing a segment
- `B`: go forward without drawing

#### Results
<img src="resource/cantor_2.png" width="33%">
<img src="resource/cantor_3.png" width="33%">
<img src="resource/cantor_4.png" width="33%">

### 4. Koch curve <span style="font-size:small">([Wikipedia Example 4](https://en.wikipedia.org/wiki/L-system#Example_4:_Koch_curve))</span>
[code](demo/demo4.py)

#### L-system
- variables: `F`
- constants: `+-`
- axiom: `F`
- rules: `F→F+F-F-F+F`

#### Drawing rules
- `F`: go forward with drawing a segment
- `+`: turn 90° to the left
- `-`: turn 90° to the right

#### Results
<img src="resource/koch_2.png" width="33%">
<img src="resource/koch_3.png" width="33%">
<img src="resource/koch_4.png" width="33%">
