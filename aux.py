"""
Fichier aux.py

Fonctions auxiliaires
"""

# blablabla

import os

"""
Efface le terminal
"""
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

"""
Entrée :
    type_input (type) : type de l'élément à saisir
Sortie :
    un entier, un réel flottant ou une chaine de caractères

Saisie et renvoi d'un élément de type type_input
Si une erreur est détectée dans la conversion de l'élément saisi, il y a deux issues possibles :
    - cas où type_input = float : si l'élément saisi est une chaine de caractères alphanumériques, renvoie
    l'élément, sinon, renvoie la chaine de caractères "\0"
    - cas où type_input = int : renvoie la chaine de caractères "\0"
"""
def generic_type_input(message, type_input):
    # Saisie de l'élément
    user_input = input(message)

    try:
        # Conversion
        user_input = type_input(user_input)
    except ValueError:
        # Erreur détectée

        # Le type attendu est int : erreur
        if type_input == int:
            user_input = "\0"
    finally:
        # Renvoi du résultat (erreur ou non)
        return user_input
