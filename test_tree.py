"""
Fichier test_init_tree.py

Test de l'ensemble des méthodes de la classe Tree et de ses dépendances
"""


import sys
import os.path
from functions import clear
from tree import Tree
from menu import Menu


clear()

# Arbre vide
t = Tree()

# L'utilisateur a le choix entre créer un nouvel arbre et charger un fichier JSON existant

print("Create a new tree: type N or n")
print("Load a JSON file: type L or l\n")

choice = input("Choice: ")

# Création d'un nouvel arbre
if choice == "N" or choice == "n":
    clear()
    t.init_tree()
# Chargement d'un fichier JSON
elif choice == "L" or choice == "l":
    print()

    # Saisie du nom du fichier
    name_file = input("Enter the JSON file name: ")

    # Erreur si le fichier n'existe pas
    if not (os.path.isfile(name_file)):
        print("\nError \"test_tree.py\"")
        print("The file '", name_file, "' does not exist", sep="")

        sys.exit()

    t.from_json_to_tree(name_file)
else:
    clear()
    sys.exit()

clear()

# Menu et modifications de l'arbre

m = Menu(t)
m.menu_tree()
