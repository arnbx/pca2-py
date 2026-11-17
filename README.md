# Python Programs

Eight small Python programs, one file per question. All were run with `.venv/bin/python3` (Python 3.15.2).

---

## 1. File write and read

**Question:** Write a Python program to open a text file `notes.txt` in write mode, write three lines of text into it, close it, and then read and display its contents.

**File:** `q1_file_write_read.py`

```python
f = open("notes.txt", "w")
f.write("Line one\nLine two\nLine three\n")
f.close()

f = open("notes.txt", "r")
print(f.read())
f.close()
```

**Output:**

```
Line one
Line two
Line three

```

---

## 2. Count vowels, consonants and special characters

**Question:** Write a program to count total vowels, consonants, and special characters present in a user-given string.

**File:** `q2_count_chars.py`

```python
s = input("Enter a string: ")
vowels = sum(c.lower() in "aeiou" for c in s)
consonants = sum(c.isalpha() and c.lower() not in "aeiou" for c in s)
special = sum(not c.isalnum() and not c.isspace() for c in s)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Special characters:", special)
```

**Output** (input `Hello, World! 123`):

```
Enter a string: Hello, World! 123
Vowels: 3
Consonants: 7
Special characters: 2
```

**Output** (input `AEIOU bcd!?`):

```
Enter a string: AEIOU bcd!?
Vowels: 5
Consonants: 3
Special characters: 2
```

---

## 3. Swap keys and values in a dictionary

**Question:** Write a Python program to swap keys and values in a dictionary.

**File:** `q3_swap_dict.py`

```python
d = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in d.items()}
print(swapped)
```

**Output:**

```
{1: 'a', 2: 'b', 3: 'c'}
```

---

## 4. Factorial using recursion

**Question:** Write a Python program defining a user function that calculates factorial of a number using recursion.

**File:** `q4_factorial.py`

```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))
```

**Output:**

```
120
```

---

## 5. Key with maximum value

**Question:** Write a Python program to pass a dictionary as an argument to a function that returns the key with the maximum value.

**File:** `q5_max_key.py`

```python
def max_key(d):
    return max(d, key=d.get)

scores = {"Ann": 70, "Bob": 95, "Cy": 88}
print(max_key(scores))
```

**Output:**

```
Bob
```

---

## 6. Rectangle area with default breadth

**Question:** Write a Python program using a function with default parameters to calculate the area of a rectangle, where the breadth defaults to 5 if not provided.

**File:** `q6_rect_area.py`

```python
def rect_area(length, breadth=5):
    return length * breadth

print(rect_area(10))      # breadth defaults to 5
print(rect_area(10, 3))
```

**Output:**

```
50
30
```

---

## 7. Simple interest with default rate

**Question:** Write a Python program using a function with default parameters to calculate the Simple Interest. If the rate of interest is not provided, assume it as 5%.

**File:** `q7_simple_interest.py`

```python
def simple_interest(principal, time, rate=5):
    return principal * rate * time / 100

print(simple_interest(1000, 2))       # rate defaults to 5%
print(simple_interest(1000, 2, 8))
```

**Output:**

```
100.0
160.0
```

---

## 8. Division with exception handling

**Question:** Write a Python program that reads two numbers from the user, divides them, and handles ZeroDivisionError and ValueError using multiple except blocks. Ensure a message is printed in the finally block regardless of the outcome.

**File:** `q8_divide_errors.py`

```python
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: cannot divide by zero")
except ValueError:
    print("Error: please enter valid numbers")
finally:
    print("Program finished.")
```

**Output** (inputs `10` and `4`):

```
Enter first number: 10
Enter second number: 4
Result: 2.5
Program finished.
```

**Output** (inputs `10` and `0`):

```
Enter first number: 10
Enter second number: 0
Error: cannot divide by zero
Program finished.
```

**Output** (inputs `abc` and `4`):

```
Enter first number: abc
Error: please enter valid numbers
Program finished.
```
