# Hello World

This directory contains introductory Python exercises covering the Python interpreter, expressions, variables, formatted output, and executable Python scripts.

## Tasks

### 0. Interpreter Reasoning

The first task introduces the Python interactive interpreter (REPL).

The exercise explores the difference between expressions and assignment statements.

For example:

```python
>>> 2 + 3
5
>>> x = 10
>>> x
10
>>> print(x)
10
>>> x > 5
True
```

An expression entered directly into the interactive interpreter has its value evaluated and displayed by the REPL.

An assignment such as:

```python
x = 10
```

stores a value in a variable but does not automatically display the value.

The `print()` function explicitly outputs a value.

### 1. Deterministic Script Output

The `structured_output.py` script produces a fixed output without requiring user input.

Expected output:

```text
Language: Python
Version: 3
Pi approx: 3.14
Computation valid: True
```

The script demonstrates:

* Variables
* Integer and floating-point values
* Boolean comparison expressions
* Floating-point formatting
* Formatted string interpolation using f-strings
* Python 3 executable scripts

## Running the Script

From the `hello_world` directory:

```bash
python3 structured_output.py
```

The script can also be executed directly:

```bash
./structured_output.py
```

If necessary, make the file executable with:

```bash
chmod +x structured_output.py
```

## Files

| File                   | Description                                 |
| ---------------------- | ------------------------------------------- |
| `README.md`            | Documentation for the Hello World exercises |
| `structured_output.py` | Produces the required deterministic output  |

## Requirements

The script:

* Uses Python 3
* Does not request user input
* Formats the Pi value to two decimal places
* Generates the Boolean value through a comparison expression
* Uses formatted string interpolation
* Produces the required output exactly

