# Day 1: Python Basics

Welcome to **Day 1** of the 30 Days of Python Challenge! Today, we explored some fundamental concepts in Python, including basic syntax, arithmetic operations, data types, and string manipulation.

## Topics Covered

### 1. Printing in Python

To output text or variables in Python, we use the `print()` function:
```python
print("Hello, World!")
```

### 2. Arithmetic Operations

Python supports several arithmetic operations, listed below in their order of precedence:

| Operation         | Symbol  | Example               | Explanation                              |
|-------------------|---------|-----------------------|------------------------------------------|
| Parentheses       | `()`    | `(3 + 2) * 4`         | Operations inside parentheses are done first |
| Exponentiation    | `**`    | `2 ** 3`              | Raises a number to the power of another  |
| Multiplication    | `*`     | `3 * 4`               | Multiplies two numbers                   |
| Floor Division    | `//`    | `10 // 3`             | Division without remainder (integer division) |
| Division          | `/`     | `10 / 2`              | Regular division                         |
| Addition          | `+`     | `3 + 2`               | Adds two numbers                         |
| Subtraction       | `-`     | `5 - 3`               | Subtracts one number from another        |
| Modulus           | `%`     | `10 % 3`              | Gives the remainder of division          |

### 3. Variables and Data Types

#### Basic Data Types:
- **String**: Text data, created using either single (`'`) or double (`"`) quotes.
  ```python
  x = "Hello, World!"  # str type
  ```
- **Integer**: Whole numbers, can be converted with `int()`.
  ```python
  y = 834  # int type
  ```
- **Float**: Numbers with decimal points.
  ```python
  z = 38.93  # float type
  ```
- **Boolean**: Represents `True` or `False`.
  ```python
  is_active = True  # bool type
  ```

#### Type Function:
To check the type of a variable, use the `type()` function:
```python
x = 20.5
print(type(x))  # Output: <class 'float'>
```

#### Example of Various Data Types:
```python
x = ["apple", "banana", "cherry"]  # list
x = {"name": "John", "age": 36}    # dict
x = frozenset(["apple", "banana"]) # frozenset
x = b"Hello"                       # bytes
```

### 4. Type Conversion

Python allows you to convert between data types using functions like `int()`, `float()`, and `str()`:
```python
x = float(1)     # Converts 1 to 1.0
y = int(2.8)     # Converts 2.8 to 2
z = complex(1)   # Converts 1 to (1+0j)
```

### 5. Reserved Keywords

These are words that Python has reserved for specific purposes. They cannot be used as variable names:
```
False, None, True, and, as, assert, break, class, def, del, elif, else, except, return, etc.
```

### 6. Comments

Comments in Python can be added using `#` for single-line comments, or `''' ... '''` for multi-line comments.

### 7. Random Numbers

You can generate random numbers in Python using the `random` module:
```python
import random
print(random.randrange(1, 10))  # Random number between 1 and 9
```

### 8. Strings in Python

- **String Slicing**: Extract a portion of a string.
  ```python
  a = "Hello, World!"
  print(a[2:5])  # Outputs: "llo"
  ```
  
- **String Methods**:
  - `upper()`: Converts string to uppercase.
    ```python
    print(a.upper())  # Output: "HELLO, WORLD!"
    ```
  - `lower()`: Converts string to lowercase.
    ```python
    print(a.lower())  # Output: "hello, world!"
    ```
  - `strip()`: Removes whitespace from the beginning and end of a string.
    ```python
    print(a.strip())  # Output: "Hello, World!"
    ```
  - `replace()`: Replaces part of the string with another.
    ```python
    print(a.replace("H", "J"))  # Output: "Jello, World!"
    ```
  - `split()`: Splits a string into a list.
    ```python
    print(a.split(","))  # Output: ['Hello', ' World!']
    ```

- **String Concatenation**:
  Combine two or more strings:
  ```python
  a = "Hello"
  b = "World"
  print(a + " " + b)  # Output: "Hello World"
  ```

- **String Formatting**:
  - Using f-strings:
    ```python
    age = 36
    print(f"My name is John, I am {age} years old.")  # Output: My name is John, I am 36 years old.
    ```

  - Limiting decimals:
    ```python
    price = 59.99
    print(f"The price is {price:.2f} dollars")  # Output: The price is 59.99 dollars
    ```

## Helpful Resources

Here are some resources that helped me during Day 1:
- [Learn Python in Y Minutes](https://learnxinyminutes.com/docs/python/)
- [TutorialsPoint Python Guide](https://www.tutorialspoint.com/python/index.htm)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/default.asp)
- [FreeCodeCamp - String Manipulation](https://www.freecodecamp.org/learn/scientific-computing-with-python/learn-string-manipulation-by-building-a-cipher/step-5)


---

### Exercice 1 : Afficher un message (Facile)  
Demandez à l'utilisateur de saisir son nom et son âge, puis affichez un message de bienvenue.

**Exemple de sortie :**  
```
Entrez votre nom: Ali
Entrez votre âge: 25
Bienvenue Ali, vous avez 25 ans!
```

---

### Exercice 2 : Calcul d'une opération arithmétique (Facile)  
Demandez à l'utilisateur de saisir deux nombres, puis affichez leur somme, différence, produit, division et reste (modulo).

**Exemple de sortie :**  
```
Entrez le premier nombre: 15
Entrez le deuxième nombre: 4
Somme: 19
Différence: 11
Produit: 60
Division: 3.75
Modulo: 3
```

---

### Exercice 3 : Générer un nombre aléatoire (Intermédiaire)  
Demandez à l'utilisateur d'entrer un nombre entre 1 et 100, puis affichez un nombre aléatoire entre 1 et 100.

**Exemple de sortie :**  
```
Entrez un nombre entre 1 et 100: 50
Nombre généré aléatoirement: 73
```

---

### Exercice 4 : Afficher le type d'une variable (Intermédiaire)  
Demandez à l'utilisateur de saisir une valeur, puis affichez le type de la valeur saisie.

**Exemple de sortie :**  
```
Entrez une valeur: 25
Le type de la variable est: <class 'int'>
```

---

### Exercice 5 : Manipuler les chaînes de caractères (Difficile)  
Demandez à l'utilisateur de saisir une phrase, puis :
1. Remplacez tous les espaces par des tirets.
2. Convertissez la chaîne en majuscules.

**Exemple de sortie :**  
```
Entrez une phrase: Bonjour tout le monde
Résultat: BONJOUR-TOUT-LE-MONDE
```
---

This concludes **Day 1** of my 30-day challenge. Stay tuned for more updates!