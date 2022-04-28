"""
Fichier aux.py

Fonctions auxiliaires
"""


import os


# Portes logiques
gates = ["AND", "OR", "k/n"]


"""
Efface le terminal
"""
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

"""
Entrée :
    list1 (liste de type générique)
    list2 (liste de type générique)
Sortie : liste de type générique

Applique la différence d_list = list1\list2
"""
def private_from(list1, list2):
    rev_list = []

    for element in list1:
        if not (element in list2):
            rev_list.append(element)

    return rev_list

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

"""
Entrée :
    gate (chaine de caractères) : porte logique
Sortie : tuple

Renvoie le couple (k, n) où k et n sont les éléments de la porte logique gate := k/n
"""
def get_elements_gate_comb(gate):
    elements_split = gate.split("/")

    # Erreur si le format de la porte logique n'est pas valide
    if len(elements_split) != 2:
        return "\0"

    str_k = elements_split[0]
    str_n = elements_split[1]

    return (str_k, str_n)

"""
Entrée :
    gate (chaine de caractères) : porte logique d'un noeud
    children (entier) : nombre de fils d'un noeud
Sortie : booléen

Renvoie vrai ssi la porte logique gate est valide (méthode utile pour la saisie utilisateur)
"""
def gate_is_valid(gate, children):
    # La porte logique gate est répertoriée dans la liste gates : il s'agit soit d'une porte AND, soit d'une porte OR
    if gate in gates:
        return True

    # La porte logique contient le caractère '/' : il s'agit éventuellement d'une porte logique k/n
    if "/" in gate:
        # Vérification de la validité de la porte logique

        split_gate = get_elements_gate_comb(gate)

        if split_gate != "\0":
            str_k = split_gate[0]
            str_n = split_gate[1]

            # Les deux éléments k et n doivent être numériques
            if str_k.isnumeric() and str_n.isnumeric():
                n = int(str_n)

                # n doit être égal au nombre de fils du noeud courant
                if n == children:
                    return True

    return False

"""
Entrée :
    rule (chaine de caractères) : règle de calcul
Sortie : booléen

Renvoie vrai ssi la règle de calcul rule est valide (méthode utile pour la saisie utilisateur)
"""
def rule_is_valid(gate, rule):
    # Règles de calcul valides pour les portes logiques AND et k/n : somme et produit

    if gate == "AND" or gate == "k/n":
        valid_rules_and_comb = ["+", "*"]
        return (rule in valid_rules_and_comb)

    # Règles de calcul valides pour la porte logique OR : maximum et minimum

    valid_rules_or = ["M", "m"]
    return (rule in valid_rules_or)

"""
Entrée :
    optimization (chaine de caractères) : règle d'opitmisation
Sortie : booléen

Renvoie vrai ssi la règle d'optimisation optimization est valide (méthode utile pour la saisie utilisateur)
"""
def optimization_is_valid(optimization):
    # Maximisation ou minimisation

    valid_optimizations = ["M", "m"]
    return (optimization in valid_optimizations)

"""
Entrée :
    gate (chaine de caractères) : porte logique d'un noeud
    set_n (entier) : nouvelle valeur de n pour la combinaison k parmi n
Sortie : chaine de caractères

Modifie et renvoie une porte de type k parmi n
"""
def set_gate_comb(gate, set_n):
    (str_k, str_n) = get_elements_gate_comb(gate)

    n = int(str_n)
    n += set_n
    str_n = str(n)

    gate = str_k + "/" + str_n

    return gate

"""
Entrée :
    list (liste de chaines de caractères)
    k (chaines de caractères)
Sortie : liste de chaines de caractères

Renvoie l'ensemble des combinaisons possibles de k parmi n
"""
def list_gate_comb(list, k):
    lgc = []
    i = 0
    i_max = 2**len(list)-1

    while i <= i_max:
        tmp_list = []
        j = 0
        j_max = len(list)-1

        while j <= j_max:
            if (i >> j) & 1 == 1:
                tmp_list.append(list[j])

            j += 1

        if len(tmp_list) == k:
            lgc.append(tmp_list)

        i += 1

    return lgc

"""
Entrée :
    symb_expr (chaine de caractères) : expression symbolique
Sortie : liste de chaines de caractères

Renvoie la liste des variables se trouvant dans l'expression symbolique symb_expr
"""
def all_var_in_expr(symb_expr):
    str_expr = str(symb_expr)
    variables = []

    for char in str_expr:
        if 97 <= ord(char) <= 122:
            variables.append(char)

    return variables
