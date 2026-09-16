# Middle-School Python

A collection of my old Python school projects, exercises, tests, and experiments.

Most of these programs were created as part of school assignments, practical exercises, and programming tests while I was learning the fundamentals of programming.

I eventually preferred Java over Python, but Python was where I learned many of the basic programming concepts that I later used in other languages.

> From simple console programs to arrays, algorithms, JSON, and programming tests. Every programmer starts somewhere.

---

## Repository Structure

| Folder                               | Description                                                             |
| ------------------------------------ | ----------------------------------------------------------------------- |
| [`arrays`](arrays)                   | Exercises involving arrays/lists, indexing, searching, and calculations |
| [`json`](json)                       | Experiments with JSON data, configuration files, loading, and saving    |
| [`kontroldarbi`](kontroldarbi)       | Programming tests and larger school exercises                           |
| [`math`](math)                       | Mathematical and calculation-based programs                             |
| [`python strings`](python%20strings) | String manipulation, type conversion, and related exercises             |

---

## Topics Covered

### Functions

Learning how to organize programs into reusable functions.

```python
def function_name(parameter):
    ...
    return result
```

Topics included:

* Function definitions
* Parameters
* Return values
* Calling functions
* Separating a program into multiple logical parts

---

### Loops

Loops were used throughout many of the exercises.

```python
for i in range(N):
    print(i)
```

Topics included:

* `for` loops
* `range()`
* Repeating operations
* Iterating through arrays
* Processing multiple values

---

### Arrays and Lists

Python lists were used to store collections of values.

```python
A = [0] * 10
```

Individual elements could then be accessed using an index:

```python
A[i]
```

Topics included:

* Creating lists
* Initializing arrays
* Array indexing
* Modifying elements
* Iterating through arrays
* Calculating values from array elements
* Searching arrays

---

### Random Number Generation

Some exercises generated random values using Python's `random` module.

```python
from random import randint

number = randint(100, 200)
```

Arrays could also be filled automatically:

```python
for i in range(N):
    A[i] = randint(100, 200)
```

This introduced the idea of generating data programmatically instead of entering every value manually.

---

### Searching

Some programs searched through arrays to determine whether a particular value existed.

```python
for i in range(N):
    if A[i] == B:
        print("Found!")
```

This introduced the basic idea of linear search, where each element is checked one by one.

---

### Calculations and Accumulators

Several exercises involved performing calculations using values stored in arrays.

For example:

```python
sum = 0

for i in range(N):
    sum = sum + A[i]
```

This introduced the accumulator pattern, where a variable stores a running result.

Examples of calculations used in the projects include:

* Sum of array elements
* Powers and cubes
* Geometric calculations
* Volumes
* Mathematical formulas
* Cost calculations

---

### Strings

String manipulation was another part of the coursework.

```python
text = str(number)
length = len(text)
```

Topics included:

* `str()`
* `len()`
* String concatenation
* Building strings
* Accessing string characters
* Formatting console output

One exercise involved constructing a visual pattern using `@` characters.

---

### Type Conversion

The programs frequently converted values between different Python types.

```python
number = int(input())
text = str(number)
```

Common conversions included:

* `int()` — converting input to an integer
* `str()` — converting a value to a string

This was particularly important because values received from `input()` are initially strings.

---

### Binary Representation

Some exercises involved converting decimal numbers into binary representation.

```python
binary_number = bin(N)
```

For example:

```text
10 → 0b1010
```

The exercise also used string operations to determine the length of the resulting representation.

---

### Console Output

A lot of the programs were designed around formatted terminal output.

Examples include:

```python
print("@", end="")
```

and:

```python
print("A[", i, "]=", sep="")
```

Topics included:

* `print()`
* `end`
* `sep`
* Formatting output
* Creating text-based patterns
* Displaying array elements

---

## Mathematics

The repository also contains programs focused on basic mathematical problems.

Examples include:

* Geometry
* Volumes
* Cubes
* Numerical calculations
* Cost calculations
* Formula-based problems

These exercises were useful for learning how to translate a mathematical formula into executable code.

---

## JSON and Configuration

The repository also contains experiments involving JSON.

These programs introduced concepts such as:

* JSON data
* Configuration files
* Loading configuration
* Saving configuration
* Reading structured data
* Writing structured data

This was a step beyond simple console programs and introduced the idea of programs working with external data.

---

## Programming Tests

The `kontroldarbi` directory contains programming tests and larger exercises.

These were not just small examples, but assignments where multiple concepts had to be combined into a complete solution.

Typical requirements included:

* Reading input from the keyboard
* Validating input
* Processing data
* Using functions
* Working with arrays
* Performing calculations
* Printing formatted results

One example involved generating an array of random numbers, displaying the array, and calculating the sum of its elements.

---

## Example: Array Test

One of the programming tests involved creating an array with 10 elements and filling it with random numbers between 100 and 200.

The program then:

1. Generated the array.
2. Printed every element.
3. Calculated the sum of all elements.
4. Displayed the final result.

The general algorithm was:

```text
Create array
    ↓
Fill array with random numbers
    ↓
Print array
    ↓
Calculate sum
    ↓
Print result
```

This exercise combined several fundamental concepts:

* Lists
* Indexing
* Functions
* Loops
* Random numbers
* Accumulators
* Console output

---

## Example: Binary Exercise

Another exercise converted an integer to binary and counted the number of characters in the resulting representation.

```text
Input integer
      ↓
Convert to binary
      ↓
Convert/process as string
      ↓
Count characters
      ↓
Display result
```

This combined:

* Functions
* `bin()`
* `str()`
* `len()`
* Type conversion
* Console input/output

---

## Example: Pattern Exercise

Some exercises focused on producing shapes and patterns in the console.

For example, a program could construct lines using `@` characters and spaces.

The program used:

* `for` loops
* String concatenation
* `end=""`
* Functions
* Input values

These exercises helped develop an understanding of loops and program-controlled output.

---

## Programming Concepts

Overall, the repository contains examples of:

* Variables
* Input and output
* Data types
* Type conversion
* Conditional statements
* `for` loops
* Functions
* Lists and arrays
* Indexing
* Searching
* Random number generation
* Strings
* String manipulation
* Mathematical calculations
* Accumulators
* Binary representation
* JSON
* Configuration files
* Basic algorithms
* Console formatting
* Input validation

---

## What This Repository Represents

This repository is primarily an archive of my early programming work.

The code is not intended to represent modern production-quality Python. Some of the programs use approaches that I would structure differently today.

That is part of the point.

Looking back at old code makes it possible to see how programming skills developed over time, from basic loops and arrays to more advanced programming concepts and different programming languages.

---

## Programming Language Preference

Although this repository is focused on Python, I eventually preferred Java for programming.

Python was still an important part of learning the fundamentals, particularly because it made it easy to experiment with:

* Algorithms
* Data structures
* Functions
* Input/output
* Mathematical problems
* Basic automation

The concepts learned here later carried over into other languages and programming projects.

---

## Archive

This repository is preserved as a snapshot of my early programming education.

Some programs are simple. Some are unfinished. Some are clearly written for a specific school assignment.

They are kept here because they show the progression from learning basic programming syntax to understanding larger programming concepts.

---

## License

These programs are preserved primarily for educational and archival purposes.

Feel free to read, study, or experiment with the code.
