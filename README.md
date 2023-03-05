# L-system

**A simulator of [L-systems](https://en.wikipedia.org/wiki/L-system) written in Python**

Below is a gallery of various mathematical objects that can be described by an L-system.

## 1. Algae
[reference](https://en.wikipedia.org/wiki/L-system#Example_1:_Algae), [code](demo/algae.py)

### L-system
- variables: `A`, `B`
- constants: none
- axiom: `A`
- rules: `A→AB`, `B→A`

### Results
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

## 2. Thue-Morse sequence
[reference](https://en.wikipedia.org/wiki/Thue%E2%80%93Morse_sequence), [code](demo/thue-morse_sequence.py)

### L-system
- variables: `0`, `1`
- constants: none
- axiom: `0`
- rules: `0→01`, `1→10`

### Results
```
n = 0: 0
n = 1: 01
n = 2: 0110
n = 3: 01101001
n = 4: 0110100110010110
n = 5: 01101001100101101001011001101001
n = 6: 0110100110010110100101100110100110010110011010010110100110010110
```

## 3. Fractal binary tree
[reference](https://en.wikipedia.org/wiki/L-system#Example_2:_Fractal_(binary)_tree), [code](demo/binary_tree.py)

### L-system
- variables: `0`, `1`
- constants: `[`, `]`
- axiom: `0`
- rules: `1→11`, `0→1[0]0`

### Drawing rules
- `0`: go forward with drawing a green segment
- `1`: go forward with drawing a brown segment
- `[`: push the current pose on the stack, turn 45° to the left
- `[`: pop a pose from the stack, turn 45° to the right

### Results
<img src="resource/binary_tree_0.png" width=47%><img src="resource/binary_tree_1.png" width=47%>
<img src="resource/binary_tree_2.png" width=47%><img src="resource/binary_tree_3.png" width=47%>
<img src="resource/binary_tree_4.png" width=47%><img src="resource/binary_tree_5.png" width=47%>

## 4. Cantor set
[reference](https://en.wikipedia.org/wiki/L-system#Example_3:_Cantor_set), [code](demo/cantor_set.py)

### L-system
- variables: `A`, `B`
- constants: none
- axiom: `A`
- rules: `A→ABA`, `B→BBB`

### Drawing rules
- `A`: go forward with drawing a segment
- `B`: go forward without drawing

### Results
<img src="resource/cantor_set_0.png" width=47%>
<img src="resource/cantor_set_1.png" width=47%>
<img src="resource/cantor_set_2.png" width=47%>
<img src="resource/cantor_set_3.png" width=47%>
<img src="resource/cantor_set_4.png" width=47%>
<img src="resource/cantor_set_5.png" width=47%>

## 5. Variants of the Koch curve
[reference1](https://en.wikipedia.org/wiki/L-system#Example_4:_Koch_curve), [reference2](https://en.wikipedia.org/wiki/Koch_snowflake)

### 5-1. Koch snowflake
[code](demo/koch_snowflake.py)
#### L-system
- variables: `F`
- constants: `+`, `-`
- axiom: `F--F--F`
- rules: `F→F+F--F+F`

#### Drawing rules
- `F`: go forward with drawing a segment
- `+`: turn 90° to the left
- `-`: turn 90° to the right

#### Results
<img src="resource/koch_snowflake_0.png" width=47%>
<img src="resource/koch_snowflake_1.png" width=47%>
<img src="resource/koch_snowflake_2.png" width=47%>
<img src="resource/koch_snowflake_3.png" width=47%>
<img src="resource/koch_snowflake_4.png" width=47%>
<img src="resource/koch_snowflake_5.png" width=47%>

### 5-2. Quadratic type 1 curve
#### L-system
- variables: `F`
- constants: `+`, `-`
- axiom: `F`
- rules: `F→F+F-F-F+F`

#### Drawing rules
- `F`: go forward with drawing a segment
- `+`: turn 90° to the left
- `-`: turn 90° to the right

#### Results
<img src="resource/koch_quadratic_1_0.png" width=47%>
<img src="resource/koch_quadratic_1_1.png" width=47%>
<img src="resource/koch_quadratic_1_2.png" width=47%>
<img src="resource/koch_quadratic_1_3.png" width=47%>
<img src="resource/koch_quadratic_1_4.png" width=47%>
<img src="resource/koch_quadratic_1_5.png" width=47%>

### 5-3. Quadratic type 2 curve (Minkowski sausage)
#### L-system
- variables: `F`
- constants: `+`, `-`
- axiom: `F`
- rules: `F→F+F-F-FF+F+F-F`

#### Drawing rules
- `F`: go forward with drawing a segment
- `+`: turn 90° to the left
- `-`: turn 90° to the right

#### Results
<img src="resource/koch_quadratic_2_0.png" width=47%>
<img src="resource/koch_quadratic_2_1.png" width=47%>
<img src="resource/koch_quadratic_2_2.png" width=47%>
<img src="resource/koch_quadratic_2_3.png" width=47%>
<img src="resource/koch_quadratic_2_4.png" width=47%>
<img src="resource/koch_quadratic_2_5.png" width=47%>

## 6. Variants of the Sierpiński triangle
[reference1](https://en.wikipedia.org/wiki/L-system#Example_5:_Sierpinski_triangle), [reference2](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_curve)

### 6-1. Sierpiński triangle
[code](demo/sierpinski_triangle.py)

#### L-system
- variables: `F`, `G`
- constants: `+`, `-`
- axiom: `F-G-G`
- rules: `F→F-G+F+G-F`, `G→GG`

#### Drawing rules
- `F`: go forward with drawing a red segment
- `G`: go forward with drawing a yellow segment
- `+`: turn 120° to the left
- `-`: turn 120° to the right

#### Results
<img src="resource/sierpinski_triangle_0.png" width=47%>
<img src="resource/sierpinski_triangle_1.png" width=47%>
<img src="resource/sierpinski_triangle_2.png" width=47%>
<img src="resource/sierpinski_triangle_3.png" width=47%>
<img src="resource/sierpinski_triangle_4.png" width=47%>
<img src="resource/sierpinski_triangle_5.png" width=47%>

### 6-2. Sierpiński arrowhead curve
[code](demo/sierpinski_arrowhead_curve_1.py)

#### L-system
- variables: `A`, `B`
- constants: `+`, `-`
- axiom: `A`
- rules: `A→B-A-B`, `B→A+B+A`

#### Drawing rules
- `A`: go forward with drawing a red segment
- `B`: go forward with drawing a blue segment
- `+`: turn 60° to the left
- `-`: turn 60° to the right

#### Results
<img src="resource/sierpinski_arrowhead_curve_1_0.png" width=47%>
<img src="resource/sierpinski_arrowhead_curve_1_1.png" width=47%>
<img src="resource/sierpinski_arrowhead_curve_1_2.png" width=47%>
<img src="resource/sierpinski_arrowhead_curve_1_3.png" width=47%>
<img src="resource/sierpinski_arrowhead_curve_1_4.png" width=47%>
<img src="resource/sierpinski_arrowhead_curve_1_5.png" width=47%>

### 6-3. Sierpiński arrowhead curve (alternative construction)
[code](demo/sierpinski_arrowhead_curve_2.py)

#### L-system
- variables: `X`, `Y`
- constants: `F`, `+`, `-`
- axiom: `XF`
- rules: `X→YF+XF+Y`, `Y→XF-YF-X`

#### Drawing rules
- `X`: do nothing
- `Y`: do nothing
- `F`: go forward with drawing a segment
- `+`: turn 60° to the left
- `-`: turn 60° to the right

#### Results
<img src="resource/sierpinski_arrowhead_curve_2_0.png" width=47%>
<img src="resource/sierpinski_arrowhead_curve_2_1.png" width=47%>
<img src="resource/sierpinski_arrowhead_curve_2_2.png" width=47%>
<img src="resource/sierpinski_arrowhead_curve_2_3.png" width=47%>
<img src="resource/sierpinski_arrowhead_curve_2_4.png" width=47%>
<img src="resource/sierpinski_arrowhead_curve_2_5.png" width=47%>

## 7. Variants of the Sierpiński curve
[reference1](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_curve), [reference2](https://math.stackexchange.com/questions/3393187)

### 7-1. Sierpiński curve
[code](demo/sierpinski_curve.py)

#### L-system
- variables: `X`
- constants: `F`, `+`, `-`
- axiom: `F--XF--F--XF`
- rules: `X→XF+G+XF--F--XF+G+X`

#### Drawing rules
- `X`: do nothing
- `F`: go forward with drawing a segment
- `+`: turn 45° to the left
- `-`: turn 45° to the right

#### Results
<img src="resource/sierpinski_curve_0.png" width=47%>
<img src="resource/sierpinski_curve_1.png" width=47%>
<img src="resource/sierpinski_curve_2.png" width=47%>
<img src="resource/sierpinski_curve_3.png" width=47%>
<img src="resource/sierpinski_curve_4.png" width=47%>
<img src="resource/sierpinski_curve_5.png" width=47%>

### 7-2. Sierpiński square curve
[code](demo/sierpinski_square_curve.py)

#### L-system
- variables: `X`
- constants: `F`, `+`, `-`
- axiom: `F+XF+F+XF`
- rules: `X→XF-F+F-XF+F+XF-F+F-X`

#### Drawing rules
- `X`: do nothing
- `F`: go forward with drawing a segment
- `+`: turn 90° to the left
- `-`: turn 90° to the right

#### Results
<img src="resource/sierpinski_square_curve_0.png" width=47%>
<img src="resource/sierpinski_square_curve_1.png" width=47%>
<img src="resource/sierpinski_square_curve_2.png" width=47%>
<img src="resource/sierpinski_square_curve_3.png" width=47%>
<img src="resource/sierpinski_square_curve_4.png" width=47%>
<img src="resource/sierpinski_square_curve_5.png" width=47%>
