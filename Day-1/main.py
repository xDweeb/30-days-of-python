#Exercice 1

print("Entrez votre nom:")
nom = input()
print("Entrez votre âge:")
age = input()
print(f"Bienvenue {nom}, vous avez {age} ans")

#Exercice 2

print("Entrez le premier nombre:")
a = int(input())  # Convertir en entier
print("Entrez le deuxième nombre:")
b = int(input())  

print("Somme:", a + b)
print("Différence:", a - b)
print("Produit:", a * b)
print("Division:", a / b)
print("Modulo:", a % b)

#Exercice 3
import random

print("Entrez un nombre entre 1 et 100:")
nombre = int(input())  
nombre_aleatoire = random.randint(1, 100)  
print(f"Nombre généré aléatoirement: {nombre_aleatoire}")

#Exercice 4

print("Entrez une valeur:")
valeur = input()
print("Le type de la valeur est:", type(valeur))


'''
https://www.w3schools.com/python/python_exercises.asp
https://www.freecodecamp.org/learn/scientific-computing-with-python/
'''