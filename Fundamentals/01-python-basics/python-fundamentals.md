### 1. Variables and Data Types

- A variable is a name that stores a value.
- Python automatically detects the data type.

| Data Type | Example        | Description          |
| --------- | -------------- | -------------------- |
| int       | `10`           | Whole numbers        |
| float     | `3.14`         | Decimal numbers      |
| str       | `"Satwika"`    | Text                 |
| bool      | `True`/`False` | Logical values       |
| NoneType  | `None`         | Represents “nothing” |


```python
x = 10
pi = 3.14
name = "Satwika"
is_active = True
nothing = None
```


### 2. Type Casting

- Converting one data type to another.

```java
a = "100"
a_int = int(a)   # string → integer
```

- Common conversions:

  - int()
  - float()
  - str()
  - bool()
 
### 3. Input / Output

- Input from user

```python
user_name = input("Enter your name: ")
```

- Output:

```python
print("Hello", user_name)
```


### 4. Strings

- Strings are sequences of characters.
- Common operations:
  - lower() → convert to lowercase
  - upper() → convert to uppercase
  - text[index] → get character at position
  - text[a:b] → slicing from index a to b-1
  - text[::-1] → reverse the string

```python
text = "Python Programming"
text.lower()
text[0:5]
text[::-1]
```

### 5. Arithmetic Operators

- These operators perform mathematical operations.

| Operator | Meaning             | Example |
| -------- | ------------------- | ------- |
| +        | Addition            | 10 + 3  |
| -        | Subtraction         | 10 - 3  |
| *        | Multiplication      | 10 * 3  |
| /        | Division (float)    | 10 / 3  |
| %        | Modulus (remainder) | 10 % 3  |
| //       | Floor division      | 10 // 3 |
| **       | Exponent            | 10 ** 2 |


### 6. Comparison Operators

- Used to compare two values.
- Always return True or False.

##### Examples:

> greater than

== equal to

!= not equal

```python
print(5 > 3)
print(10 == 10)
print(7 != 6)
```

### 7. Logical Operators

- Used to combine conditions.

| Operator | Meaning                                | Example        |
| -------- | -------------------------------------- | -------------- |
| and      | True only if both conditions are True  | True and False |
| or       | True if at least one condition is True | True or False  |
| not      | Reverses True/False                    | not False      |


### 8. Conditionals (if / elif / else)

- Used for decision making — execute different code based on conditions.

##### Example:

```python
num = 10
if num > 0:
    print("positive")
elif num == 0:
    print("zero")
else:
    print("Negative")
```


###  9. Loops

- Loops are used to repeat code.

#### For loop

- Used to run code a fixed number of times.

```python
for i in range(10):
    print(i)
```

#### While loop

- Runs as long as a condition is True.
- Runs once before the condition is checked.


```python
count = 3
while count > 0:
    print(count)
    count -= 1
```

### 10. Functions

- Functions allow reusing a block of code.

#### Syntax:

```python
def function_name(parameters):
    # code
    return value
```

#### Example

```python
def greet(name):
    return f"Hello, {name}"
```

- Functions help make code modular and clean.
