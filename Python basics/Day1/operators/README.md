#  Python Operators

Python provides a variety of operators to perform operations on variables and values. They are grouped into several categories:

---

## Arithmetic Operators

Used to perform basic mathematical operations:

| Operator | Description            | Example   | Output |
|----------|------------------------|-----------|--------|
| `+`      | Addition               | `5 + 3`   | `8`    |
| `-`      | Subtraction            | `5 - 3`   | `2`    |
| `*`      | Multiplication         | `5 * 3`   | `15`   |
| `/`      | Division               | `5 / 2`   | `2.5`  |
| `//`     | Floor Division         | `5 // 2`  | `2`    |
| `%`      | Modulus (Remainder)    | `5 % 2`   | `1`    |
| `**`     | Exponentiation         | `2 ** 3`  | `8`    |

---

## Comparison Operators

Used to compare values:

| Operator | Description            | Example     | Output  |
|----------|------------------------|-------------|---------|
| `==`     | Equal to               | `5 == 3`    | `False` |
| `!=`     | Not equal to           | `5 != 3`    | `True`  |
| `>`      | Greater than           | `5 > 3`     | `True`  |
| `<`      | Less than              | `5 < 3`     | `False` |
| `>=`     | Greater than or equal  | `5 >= 5`    | `True`  |
| `<=`     | Less than or equal     | `5 <= 3`    | `False` |

---

## Logical Operators

Used to combine conditional statements:

| Operator | Description              | Example           | Output  |
|----------|--------------------------|-------------------|---------|
| `and`    | True if both are true    | `True and False`  | `False` |
| `or`     | True if one is true      | `True or False`   | `True`  |
| `not`    | Reverses the result      | `not True`        | `False` |

---

## Assignment Operators

Used to assign and modify variable values:

| Operator | Description              | Example     |
|----------|--------------------------|-------------|
| `=`      | Assign                   | `x = 5`     |
| `+=`     | Add and assign           | `x += 3`    |
| `-=`     | Subtract and assign      | `x -= 2`    |
| `*=`     | Multiply and assign      | `x *= 4`    |
| `/=`     | Divide and assign        | `x /= 2`    |
| `//=`    | Floor divide and assign  | `x //= 2`   |
| `%=`     | Modulus and assign       | `x %= 2`    |
| `**=`    | Power and assign         | `x **= 2`   |

---

## Bitwise Operators

Used for bit-level operations:

| Operator | Description       | Example   | Output |
|----------|-------------------|-----------|--------|
| `&`      | AND                | `5 & 3`   | `1`    |
| `|`      | OR                 | `5 | 3`   | `7`    |
| `^`      | XOR                | `5 ^ 3`   | `6`    |
| `~`      | NOT (invert bits)  | `~5`      | `-6`   |
| `<<`     | Left shift         | `5 << 1`  | `10`   |
| `>>`     | Right shift        | `5 >> 1`  | `2`    |

---

## Membership Operators

Used to test if a value is part of a sequence:

| Operator  | Description              | Example              | Output |
|-----------|--------------------------|----------------------|--------|
| `in`      | True if value is present | `'a' in 'apple'`     | `True` |
| `not in`  | True if value not present| `'x' not in 'apple'` | `True` |

---

## Identity Operators

Used to compare memory locations:

| Operator  | Description             | Example         | Output      |
|-----------|-------------------------|------------------|-------------|
| `is`      | True if same object     | `x is y`         | `True/False`|
| `is not`  | True if different object| `x is not y`     | `True/False`|

---

