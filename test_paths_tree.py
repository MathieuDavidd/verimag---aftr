"""
Fichier test_paths_tree.py

Test des méthodes de la classe Tree pour le parcours d'arbre
"""


import copy
import sys
import os.path
import sympy as sy
from functions import clear
from tree import Tree
from functions import private_from, get_elements_gate_comb, list_gate_comb


########################################################################################################################
#                                                  MÉTHODES DE TEST                                                    #
########################################################################################################################


"""
Entrée :
    tree (objet Tree) : arbre
    id (entier) : identifiant d'un noeud
Sortie : liste d'objets Tree

Reformate l'arbre tree en renvoyant la liste des sous-arbres en supprimant les fils du noeud node ssi il est muni
d'une porte logique OR ou k/n
"""
def formatting_tree(tree, id):
    split_formatting = []

    # Noeud d'identifiant id
    node = tree.get_node(id)
    # Porte logique du noeud
    gate = node.get_gate()
    # Identifiants des fils du noeud
    children = node.get_children()

    # gate est une porte logique k/n
    if "/" in gate:
        # Noeud ayant n fils et muni d'une porte logique k/n = Noeud ayant k fils et muni d'une porte logique AND
        node.set_gate("AND")

        (str_k, str_n) = get_elements_gate_comb(gate)
        k = int(str_k)

        # Copie profonde de la liste children
        tmp_children = copy.deepcopy(children)

        #
        lgc = list_gate_comb(tmp_children, k)

        # Inversion des permutations
        for i in range(len(lgc)):
            diff_list = private_from(tmp_children, lgc[i])
            lgc[i] = diff_list

        # Formatage de l'arbre
        for list in lgc:
            # Copie profonde de l'arbre
            tmp_tree = copy.deepcopy(tree)

            # Suprression des noeuds fils et des sous-arbres engendrés
            for id_child in list:
                node_child = tmp_tree.get_node(id_child)
                tmp_tree.delete_sub_tree_from_node(node_child)

            split_formatting.append(tmp_tree)
    # gate est une porte logique OR
    else:
        # Copie profonde de la liste children
        tmp_children = copy.deepcopy(children)

        # Formatage de l'arbre
        for id_child in tmp_children:
            # Copie profonde de l'arbre
            tmp_tree = copy.deepcopy(tree)

            # Suprression des noeuds fils et des sous-arbres engendrés
            for tmp_id_child in tmp_children:
                if tmp_id_child != id_child:
                    node_child = tmp_tree.get_node(tmp_id_child)
                    tmp_tree.delete_sub_tree_from_node(node_child)

            split_formatting.append(tmp_tree)

    return split_formatting

"""
Entrée :
    tree (objet Tree) : arbre
Sortie : liste d'objets Tree

Parcourt l'arbre tree et renvoie la liste des sous-arbres issus du formatage effectué lors d'un appel de la
fonction formatting_tree
"""
def pathway_tree(tree):
    nodes = tree.get_nodes()
    id_nodes_formatting = []

    # Stockage des noeuds munis d'une porte logique OR ou k/n dans la liste id_nodes_formatting
    for node in nodes:
        gate = node.get_gate()

        if not (node.is_leaf()) and gate != "AND":
            id = node.get_id()
            id_nodes_formatting.append(id)

    list_tree = [tree]

    # Création des sous-arbres issus du formatage de l'arbre
    for id_node in id_nodes_formatting:
        tmp = copy.deepcopy(list_tree)

        for tmp_tree in tmp:
            if tmp_tree.node_exists(id_node):
                list_split_tree = formatting_tree(tmp_tree, id_node)

                list_tree += list_split_tree
                list_tree.pop(0)

    return list_tree

"""
Entrée :
    tree (objet Tree) : arbre
Sortie : liste de liste d'objets Tree

Renvoie tous les chemins possibles de l'arbre tree
"""
def paths_tree(tree):
    # Sous-arbres par formatage de l'arbre
    pathway = pathway_tree(tree)
    list_paths = []

    # Parcours de chaque sous-arbre en partant de la racine et stockage du chemin dans la liste list_paths
    for pw in pathway:
        root = pw.get_root()
        paths = pw.find_path(root)

        list_paths.append(paths)

    return list_paths

"""
Entrée :
    tree (objet Tree) : arbre
    parameters (liste de chaines de caractères) : paramètres de l'arbre
Sortie : tuple

Renvoie le 3-uplet de listes (chemins, expressions symboliques développées, expressions symboliques simplifiées)
"""
def data_tree(tree, parameters):
    # Sous-arbres par formatage de l'arbre
    pathway = pathway_tree(tree)

    all_paths = []
    all_dev = []
    all_simp = []

    for pw in pathway:
        root = pw.get_root()

        # Chemins du sous-arbre en partant de la racine
        paths = pw.find_path(root)
        all_paths.append(paths)

        list_dev = []
        list_simpl = []

        for parameter in parameters:
            # Expression symbolique du sous-arbre pour le paramètre parameter
            symb_expr = pw.find_symbolic_expression(root, parameter)
            list_dev.append(symb_expr)

            # Simplification
            simpl = sy.sympify(symb_expr)

            list_simpl.append(simpl)

        all_dev.append(list_dev)
        all_simp.append(list_simpl)

    return all_paths, all_dev, all_simp


########################################################################################################################
#                                                  PROGRAMME PRINCIPAL                                                 #
########################################################################################################################


clear()

# Arbre vide
t = Tree()

# L'utilisateur doit entrer le nom d'un fichier JSON pour charger son contenu
name_file = input("Enter the JSON file name: ")

# Ajout de l'extension .json si elle a été oubliée
if ".json" not in name_file:
    name_file += ".json"

# Erreur si le fichier n'existe pas
if not (os.path.isfile(name_file)):
    print("\nError \"test_tree.py\"")
    print("The file '", name_file, "' does not exist", sep="")

    sys.exit()

# Chargement du contenu du fichier JSON pour le convertir en arbre
t.from_json_to_tree(name_file)

pro = t.get_pro()
# Paramètres de l'arbre
parameters = pro.get_parameters()

clear()

print("Test:", name_file)
print("\n~\n")

# Tous les chemins possibles et les expressions symboliques associées à chaque paramètre de l'arbre t
(paths, expr_dev, expr_simpl) = data_tree(t, parameters)

# Nombre de chemins
nmb_paths = len(paths)
print(nmb_paths, "pathway\n")

print("Parameters")
pro.print_parameters()

print("\n\n~\n")

# Affichage des chemins et des expressions symboliques associées à chaque paramètre de l'arbre
for i in range(len(paths)):
    print(i+1, ": ", sep="", end="")

    # Chemin de l'arbre
    path = paths[i]
    print(path)

    for j in range(len(parameters)):
        parameter = parameters[j]
        print("  ", parameter, ": ", sep="", end="")

        # Expressions symboliques du chemin sous forme dévelopée
        dev_path = expr_dev[i]
        simpl_path = expr_simpl[i]

        # Expressions symboliques du chemin sous forme simplifiée
        dev_par = dev_path[j]
        simpl_par = simpl_path[j]

        # Affichage de l'expression symbolique

        print(dev_par, " = ", sep="", end="")
        print(simpl_par)

    if i < len(paths)-1:
        print()
