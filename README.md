# L-system

This is a Python implementation of [L-systems](https://en.wikipedia.org/wiki/L-system).

Below is a gallery of various mathematical objects that can be described by an L-system.

## Table of Contents
1. [Algae](#1-algae)
2. [Thue-Morse sequence](#2-thue-morse-sequence)
3. [Fractal binary tree](#3-fractal-binary-tree)
4. [Cantor set](#4-cantor-set)
5. [Variants of the Koch curve](#5-variants-of-the-koch-curve)
   1. [Koch snowflake](#5-1-koch-snowflake)
   2. [Quadratic type 1 curve](#5-2-quadratic-type-1-curve)
   3. [Quadratic type 2 curve (aka Minkowski sausage)](#5-3-quadratic-type-2-curve)
6. [Variants of the Sierpiński triangle](#6-variants-of-the-sierpiński-triangle)
   1. [Sierpiński triangle](#6-1-sierpiński-triangle)
   2. [Sierpiński arrowhead curve](#6-2-sierpiński-arrowhead-curve)
7. [Variants of the Sierpiński curve](#7-variants-of-the-sierpiński-curve)
   1. [Sierpiński curve](#7-1-sierpiński-curve)
   2. [Sierpiński square curve](#7-2-sierpiński-square-curve)
8. [Variants of the dragon curve](#8-variants-of-the-dragon-curve)
   1. [Heighway dragon](#8-1-heighway-dragon)
   2. [Twin dragon](#8-2-twin-dragon)
   3. [Terdragon](#8-3-terdragon)
   4. [Lévy C curve (aka Lévy dragon)](#8-4-lévy-c-curve-aka-lévy-dragon)
9. [Fractal plant](#9-fractal-plant)
10. [Hilbert curve](#10-hilbert-curve)
11. [Peano curve](#11-peano-curve)
12. [Penrose tiling (P3)](#12-penrose-tiling-p3)

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
<img src="resource/binary_tree_0.png" width=33%><img src="resource/binary_tree_1.png" width=33%><img src="resource/binary_tree_2.png" width=33%>
<img src="resource/binary_tree_3.png" width=33%><img src="resource/binary_tree_4.png" width=33%><img src="resource/binary_tree_5.png" width=33%>

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
<img src="resource/cantor_set_0.png" width=33%><img src="resource/cantor_set_1.png" width=33%><img src="resource/cantor_set_2.png" width=33%>
<img src="resource/cantor_set_3.png" width=33%><img src="resource/cantor_set_4.png" width=33%><img src="resource/cantor_set_5.png" width=33%>

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
<img src="resource/koch_snowflake_0.png" width=33%><img src="resource/koch_snowflake_1.png" width=33%><img src="resource/koch_snowflake_2.png" width=33%>
<img src="resource/koch_snowflake_3.png" width=33%><img src="resource/koch_snowflake_4.png" width=33%><img src="resource/koch_snowflake_5.png" width=33%>

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
<img src="resource/koch_quadratic_1_0.png" width=33%><img src="resource/koch_quadratic_1_1.png" width=33%><img src="resource/koch_quadratic_1_2.png" width=33%>
<img src="resource/koch_quadratic_1_3.png" width=33%><img src="resource/koch_quadratic_1_4.png" width=33%><img src="resource/koch_quadratic_1_5.png" width=33%>

### 5-3. Quadratic type 2 curve (aka Minkowski sausage)
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
<img src="resource/koch_quadratic_2_0.png" width=33%><img src="resource/koch_quadratic_2_1.png" width=33%><img src="resource/koch_quadratic_2_2.png" width=33%>
<img src="resource/koch_quadratic_2_3.png" width=33%><img src="resource/koch_quadratic_2_4.png" width=33%><img src="resource/koch_quadratic_2_5.png" width=33%>

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
<img src="resource/sierpinski_triangle_0.png" width=33%><img src="resource/sierpinski_triangle_1.png" width=33%><img src="resource/sierpinski_triangle_2.png" width=33%>
<img src="resource/sierpinski_triangle_3.png" width=33%><img src="resource/sierpinski_triangle_4.png" width=33%><img src="resource/sierpinski_triangle_5.png" width=33%>

### 6-2. Sierpiński arrowhead curve
[code](demo/sierpinski_arrowhead_curve.py)

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
<img src="resource/sierpinski_arrowhead_curve_0.png" width=33%><img src="resource/sierpinski_arrowhead_curve_1.png" width=33%><img src="resource/sierpinski_arrowhead_curve_2.png" width=33%>
<img src="resource/sierpinski_arrowhead_curve_3.png" width=33%><img src="resource/sierpinski_arrowhead_curve_4.png" width=33%><img src="resource/sierpinski_arrowhead_curve_5.png" width=33%>

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
<img src="resource/sierpinski_curve_0.png" width=33%><img src="resource/sierpinski_curve_1.png" width=33%><img src="resource/sierpinski_curve_2.png" width=33%>
<img src="resource/sierpinski_curve_3.png" width=33%><img src="resource/sierpinski_curve_4.png" width=33%><img src="resource/sierpinski_curve_5.png" width=33%>

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
<img src="resource/sierpinski_square_curve_0.png" width=33%><img src="resource/sierpinski_square_curve_1.png" width=33%><img src="resource/sierpinski_square_curve_2.png" width=33%>
<img src="resource/sierpinski_square_curve_3.png" width=33%><img src="resource/sierpinski_square_curve_4.png" width=33%><img src="resource/sierpinski_square_curve_5.png" width=33%>

## 8. Variants of the dragon curve
[reference1](https://en.wikipedia.org/wiki/L-system#Example_6:_Dragon_curve), [reference2](https://en.wikipedia.org/wiki/Dragon_curve), [reference3](https://larryriddle.agnesscott.org/ifs/heighway/heighway.htm)

### 8-1. Heighway dragon
[code](demo/heighway_dragon_1.py)

#### L-system
- variables: `F`, `G`
- constants: `+`, `-`
- axiom: `F`
- rules: `F→F+G`, `G→F-G`

#### Drawing rules
- `F`: go forward with drawing a red segment
- `G`: go forward with drawing a green segment
- `+`: turn 90° to the left
- `-`: turn 90° to the right

#### Results
<img src="resource/heighway_dragon_0.png" width=33%><img src="resource/heighway_dragon_1.png" width=33%><img src="resource/heighway_dragon_2.png" width=33%>
<img src="resource/heighway_dragon_3.png" width=33%><img src="resource/heighway_dragon_4.png" width=33%><img src="resource/heighway_dragon_5.png" width=33%>
<img src="resource/heighway_dragon_6.png" width=33%><img src="resource/heighway_dragon_7.png" width=33%><img src="resource/heighway_dragon_8.png" width=33%>
<img src="resource/heighway_dragon_9.png" width=33%><img src="resource/heighway_dragon_10.png" width=33%><img src="resource/heighway_dragon_11.png" width=33%>
<img src="resource/heighway_dragon_12.png" width=33%><img src="resource/heighway_dragon_13.png" width=33%><img src="resource/heighway_dragon_14.png" width=33%>

### 8-2. Twin dragon
[code](demo/twin_dragon.py)

#### L-system
- variables: `F`, `G`, `X`, `Y`
- constants: `+`, `-`
- axiom: `F+G+X+Y`
- rules: `F→F+G`, `G→F-G`, `X→X+Y`, `Y→X-Y`

#### Drawing rules
- `F`: go forward with drawing a red segment
- `G`: go forward with drawing a red segment
- `X`: go forward with drawing a blue segment
- `Y`: go forward with drawing a blue segment
- `+`: turn 90° to the left
- `-`: turn 90° to the right

#### Results
<img src="resource/twin_dragon_0.png" width=33%><img src="resource/twin_dragon_1.png" width=33%><img src="resource/twin_dragon_2.png" width=33%>
<img src="resource/twin_dragon_3.png" width=33%><img src="resource/twin_dragon_4.png" width=33%><img src="resource/twin_dragon_5.png" width=33%>
<img src="resource/twin_dragon_6.png" width=33%><img src="resource/twin_dragon_7.png" width=33%><img src="resource/twin_dragon_8.png" width=33%>
<img src="resource/twin_dragon_9.png" width=33%><img src="resource/twin_dragon_10.png" width=33%><img src="resource/twin_dragon_11.png" width=33%>
<img src="resource/twin_dragon_12.png" width=33%><img src="resource/twin_dragon_13.png" width=33%><img src="resource/twin_dragon_14.png" width=33%>

### 8-3. Terdragon
[code](demo/terdragon.py)

#### L-system
- variables: `F`, `G`, `H`
- constants: `+`, `-`
- axiom: `F+G-H`
- rules: `F→F+F-F`, `G→G+G-G`, `H→H+H-H`

#### Drawing rules
- `F`: go forward with drawing a red segment
- `G`: go forward with drawing a green segment
- `H`: go forward with drawing a blue segment
- `+`: turn 120° to the left
- `-`: turn 120° to the right

#### Results
<img src="resource/terdragon_0.png" width=33%><img src="resource/terdragon_1.png" width=33%><img src="resource/terdragon_2.png" width=33%>
<img src="resource/terdragon_3.png" width=33%><img src="resource/terdragon_4.png" width=33%><img src="resource/terdragon_5.png" width=33%>
<img src="resource/terdragon_6.png" width=33%><img src="resource/terdragon_7.png" width=33%><img src="resource/terdragon_8.png" width=33%>

### 8-4. Lévy C curve (aka Lévy dragon)
[code](demo/levy_c_curve.py)

#### L-system
- variables: `F`
- constants: `+`, `-`
- axiom: `F`
- rules: `F→+F--F+`

#### Drawing rules
- `F`: go forward with drawing a segment
- `+`: turn 45° to the left
- `-`: turn 45° to the right

#### Results
<img src="resource/levy_c_curve_0.png" width=33%><img src="resource/levy_c_curve_1.png" width=33%><img src="resource/levy_c_curve_2.png" width=33%>
<img src="resource/levy_c_curve_3.png" width=33%><img src="resource/levy_c_curve_4.png" width=33%><img src="resource/levy_c_curve_5.png" width=33%>
<img src="resource/levy_c_curve_6.png" width=33%><img src="resource/levy_c_curve_7.png" width=33%><img src="resource/levy_c_curve_8.png" width=33%>
<img src="resource/levy_c_curve_9.png" width=33%><img src="resource/levy_c_curve_10.png" width=33%><img src="resource/levy_c_curve_11.png" width=33%>
<img src="resource/levy_c_curve_12.png" width=33%><img src="resource/levy_c_curve_13.png" width=33%><img src="resource/levy_c_curve_14.png" width=33%>

## 9. Fractal plant
[reference](https://en.wikipedia.org/wiki/L-system#Example_7:_Fractal_plant), [code](demo/fractal_plant.py)

### L-system
- variables: `X`, `F`
- constants: `+`, `-`, `[`, `]`
- axiom: `X`
- rules: `X→F+[[X]-X]-F[-FX]+X`, `F→FF`

### Drawing rules
- `X`: do nothing
- `F`: go forward with drawing a segment
- `+`: turn 25° to the left
- `-`: turn 25° to the right
- `[`: push the current pose on the stack
- `]`: pop a pose from the stack

### Results
<img src="resource/fractal_plant_0.png" width=33%><img src="resource/fractal_plant_1.png" width=33%><img src="resource/fractal_plant_2.png" width=33%>
<img src="resource/fractal_plant_3.png" width=33%><img src="resource/fractal_plant_4.png" width=33%><img src="resource/fractal_plant_5.png" width=33%>
<img src="resource/fractal_plant_6.png" width=33%><img src="resource/fractal_plant_7.png" width=33%><img src="resource/fractal_plant_8.png" width=33%>

## 10. Hilbert curve
[reference](https://en.wikipedia.org/wiki/Hilbert_curve), [code](demo/hilbert_curve.py)

### L-system
- variables: `A`, `B`
- constants: `F`, `+`, `-`
- axiom: `A`
- rules: `A→+BF-AFA-FB+`, `B→-AF+BFB+FA-`

### Drawing rules
- `A`: do nothing
- `B`: do nothing
- `F`: go forward with drawing a segment
- `+`: turn 90° to the left
- `-`: turn 90° to the right

### Results
<img src="resource/hilbert_curve_0.png" width=33%><img src="resource/hilbert_curve_1.png" width=33%><img src="resource/hilbert_curve_2.png" width=33%>
<img src="resource/hilbert_curve_3.png" width=33%><img src="resource/hilbert_curve_4.png" width=33%><img src="resource/hilbert_curve_5.png" width=33%>
<img src="resource/hilbert_curve_6.png" width=33%><img src="resource/hilbert_curve_7.png" width=33%><img src="resource/hilbert_curve_8.png" width=33%>

## 11. Peano curve
[reference](https://en.wikipedia.org/wiki/Peano_curve), [code](demo/peano_curve.py)

### L-system
- variables: `A`, `B`
- constants: `F`, `+`, `-`
- axiom: `A`
- rules: `A→AFBFA-F-BFAFB+F+AFBFA`, `B→BFAFB+F+AFBFA-F-BFAFB`

### Drawing rules
- `A`: do nothing
- `B`: do nothing
- `F`: go forward with drawing a segment
- `+`: turn 90° to the left
- `-`: turn 90° to the right

### Results
<img src="resource/peano_curve_0.png" width=33%><img src="resource/peano_curve_1.png" width=33%><img src="resource/peano_curve_2.png" width=33%>
<img src="resource/peano_curve_3.png" width=33%><img src="resource/peano_curve_4.png" width=33%><img src="resource/peano_curve_5.png" width=33%>

## 12. Penrose tiling (P3)
[reference](https://es.wikipedia.org/wiki/Teselaci%C3%B3n_de_Penrose#Dibujando_la_teselaci%C3%B3n_de_Penrose_P3), [code](demo/penrose_tiling_P3.py)

### L-system
- variables: `1`, `6`, `7`, `8`, `9`
- constants: `+`, `-`, `[`, `]`
- axiom: `[7]++[7]++[7]++[7]++[7]`
- rules: `1→(empty)`, `6→81++91----71[-81----61]++`, `7→+81--91[---61--71]+`, `8→-61++71[+++81++91]-`, `9→--81++++61[+91++++71]--71`

### Drawing rules
- `1`: go forward with drawing a segment
- `6`: do nothing
- `7`: do nothing
- `8`: do nothing
- `9`: do nothing
- `+`: turn 36° to the left
- `-`: turn 36° to the right
- `[`: push the current pose on the stack
- `]`: pop a pose from the stack

### Results
<img src="resource/penrose_tiling_P3_0.png" width=33%><img src="resource/penrose_tiling_P3_1.png" width=33%><img src="resource/penrose_tiling_P3_2.png" width=33%>
<img src="resource/penrose_tiling_P3_3.png" width=33%><img src="resource/penrose_tiling_P3_4.png" width=33%><img src="resource/penrose_tiling_P3_5.png" width=33%>
<img src="resource/penrose_tiling_P3_6.png" width=33%><img src="resource/penrose_tiling_P3_7.png" width=33%><img src="resource/penrose_tiling_P3_8.png" width=33%>
