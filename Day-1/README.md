
# Day-1-of-python:

## `print` fi Python:
- Kan7tajo print bach noutputiw chi 7aja.

## Arithmetic Operators:
- **A9was** | `()` 
- **Exponent** | `**` kanderbo x 2 b7aal ouss.
- **Multiplication** | `*` derb 3adii
- **Floor Division** | `//` qisma ba fasila.
- **Division** | `/` 9isma 3adia
- **Addition** | `+` za2ed
- **Subtraction** | `-` naqes
- **Modulus** | `%` Modulos y3ni ba9i 3la qesma.

## Variables w Data Types:
- **String** (`str()`, `" "` or `''`) | Kan7ewlo ay haja l string.
- **Integer** (`int()`) | Kan7ewlo ra9em mn string l ra9em sahih.
- **Float** | 3la shakl ra9m be fasila (ex: 38.93).
- **Boolean** (`True`, `False`) | Boolean kaykon ya true ya false.

## Data Types fi Python:
- **Text Type**: `str`
- **Numeric Types**: `int`, `float`, `complex`
- **Sequence Types**: `list`, `tuple`, `range`
- **Mapping Type**: `dict`
- **Set Types**: `set`, `frozenset`
- **Boolean Type**: `bool`
- **Binary Types**: `bytes`, `bytearray`, `memoryview`
- **None Type**: `NoneType`

## `type()`:
- `type()` katgolina type dyal variable.

### Examples:
```python
x = "Hello World"   # str
x = 20             # int
x = 20.5           # float
x = 1j             # complex
x = ["apple", "banana", "cherry"]   # list
x = ("apple", "banana", "cherry")   # tuple
x = range(6)       # range
x = {"name" : "John", "age" : 36}   # dict
x = {"apple", "banana", "cherry"}   # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = True           # bool
x = b"Hello"       # bytes
x = bytearray(5)   # bytearray
x = memoryview(bytes(5))   # memoryview
x = None           # NoneType

print(type(x))
```

## Python Numbers w Type Conversion:
- 3la shkel types:
    - `int`
    - `float`
    - `complex`

- Bach nconverti mn type l type akher:
```python
x = float(1)  # mn int l float
y = int(2.8)  # mn float l int
z = complex(1)  # mn int l complex
print(x, y, z)
print(type(x), type(y), type(z))
```

## Reserved Words:
- Mat9derch t3ti reserved words smiyat f variables like:
`False, None, True, and, as, assert, break, class, if, def, return...`

## Comments:
- Kan7etjo `#` bach nektebo comments
```python
# Hadi comment f python
```

## Global Variables:
- Kanjem3o wahed 3adet variables f wahed lline:
```python
x, y, z = "Orange", "Banana", "Cherry"
```

## Random Numbers:
- Python kat generi random numbers:
```python
import random
print(random.randrange(1, 10))
```

## String Handling w Concatenation:
- `str()`, `len()`, `replace()`, `split()`, `upper()`, `lower()`, etc.
```python
txt = "The best things in life are free!"
print("free" in txt)  # True
print("expensive" not in txt)  # True
```
- Concatenation dyal strings:
```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # Hello World
```

## Slicing Strings:
```python
b = "Hello, World!"
print(b[2:5])  # l characters men position 2 l 5
print(b[:5])  # men lbdya l character 5
print(b[2:])  # men character 2 l akher
```

## String Formatting:
- F-Strings bach njib data mn variables w nprintiw f string.
```python
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
```
