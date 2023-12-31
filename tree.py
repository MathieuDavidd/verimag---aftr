"""
Fichier tree.py

Classe Tree : arbre

Un arbre est un ensemble de noeuds dont les propriétés reposent sur ses paramètres et ses règles de calcul et
d'optimisation
"""


import copy
import time
import sympy as sy
import json
from functions import *
from node import Node
from parameters import Parameters


class Tree:
    """
    Constructeur

    Attributs de la classe :
        - pro (objet Parameter) : ensemble des paramètres et des règles de calcul et d'optimisation de l'arbre
        - nodes (liste d'objets Node) : liste des noeuds de l'arbre
    """
    def __init__(self):
        self.pro = Parameters()
        self.nodes = []

    """
    Entrée : aucune
    Sortie : objet Parameters
    
    Getter : renvoie l'ensemble des paramètres et des règles de calcul et d'optimisation de l'arbre
    """
    def get_pro(self):
        return self.pro

    """
    Entrée : aucune
    Sortie : liste d'objets Node
    
    Getter : renvoie la liste des noeuds de l'arbre
    """
    def get_nodes(self):
        return self.nodes

    """
    Entrée :
        id (entier) : identifiant d'un noeud
    Sortie : objet Node
    
    Getter : renvoie le noeud dont l'identifiant est id
    """
    def get_node(self, id):
        for node in self.nodes:
            id_node = node.get_id()

            if id_node == id:
                return node

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : liste d'objets Node
    
    Getter : renvoie la liste des parents du noeud node
    """
    def get_node_parents(self, node):
        node_parents = []

        # Liste des identifiants des parents du noeud node
        parents = node.get_parents()

        for parent in parents:
            # Noeud d'identifiant parent
            node_parent = self.get_node(parent)
            node_parents.append(node_parent)

        return node_parents

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : liste de chaine de caractères
    
    Getter : renvoie la liste des portes logiques des parents du noeud node
    """
    def get_node_parents_gates(self, node):
        node_parents_gates = []

        # Liste des parents du noeud node
        node_parents = self.get_node_parents(node)

        for node_parent in node_parents:
            # Porte logique du parent
            node_parent_gate = node_parent.get_gate()
            node_parents_gates.append(node_parent_gate)

        return node_parents_gates

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : liste d'objets Node
    
    Getter : renvoie la liste des fils noeud node
    """
    def get_node_children(self, node):
        node_children = []

        # Liste des identifiantsdes fils du noeud node
        children = node.get_children()

        for child in children:
            # Noeud d'identifiant child
            node_child = self.get_node(child)
            node_children.append(node_child)

        return node_children

    """
    Entrée :
        pro (objet Parameters) : paramètres et règles de calcul et d'optimisation de l'arbre
    Sortie : aucune
    
    Setter : modifie l'ensemble des paramètres et des règles de calcul et d'optimisation de l'arbre
    """
    def set_pro(self, pro):
        self.pro = pro

    """
    Entrée :
        nodes (liste d'objets Node) : liste de noeuds
    Sortie : aucune
    
    Setter : modifie la liste des noeuds de l'arbre
    """
    def set_nodes(self, nodes):
        self.nodes = nodes

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : aucune
    
    Setter : modifie le noeud ayant le même identifiant que node
    """
    def set_node(self, node):
        # Identifiant du noeud node
        id = node.get_id()
        # Noeud à modifier : d'identifiant id
        mod_node = self.get_node(id)
        # Indice du noeud à modifier
        ind_mod_node = self.nodes.index(mod_node)

        self.nodes[ind_mod_node] = node

    """
    Entrée :
        - node (objet Node) : noeud
        - root (booléen, par défaut False) : indique si le noeud node est une nouvelle racine ou non
    Sortie : aucune
    
    Ajoute le noeud node à la liste de noeuds de l'arbre
    """
    def add_node(self, node, root=False):
        # Le noeud node n'est pas une nouvelle racine : ajout en fin de liste
        if not (root):
            self.nodes.append(node)
        # Le noeud node est une nouvelle racine : insertion en début de liste
        else:
            self.nodes.insert(0, node)

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : aucune
    
    Supprime le noeud node de la liste des noeuds de l'arbre
    """
    def delete_node(self, node):
        self.nodes.remove(node)

    """
    Entrée :
        nodes (liste d'objets Node) : liste de noeuds
    Sortie : aucune
    
    Supprime l'ensemble des noeuds nodes la liste des noeuds de l'arbre
    """
    def delete_nodes(self, nodes):
        for node in nodes:
            self.delete_node(node)

    """
    Entrée : aucune
    Sortie : objet Node
    
    Renvoie la racine de l'arbre
    """
    def get_root(self):
        for node in self.nodes:
            if node.is_root():
                return node

    """
    Entrée : aucune
    Sortie : liste d'objets Node
    
    Renvoie la liste des feuilles de l'arbre
    """
    def get_leaves(self):
        leaves = []

        for node in self.nodes:
            if (node.is_leaf()):
                leaves.append(node)

        return leaves

    """
    Entrée : aucune
    Sortie : objet Tree
    
    Copie profonde de l'objet courant
    """
    def deepcopy(self):
        t = copy.deepcopy(self)
        return t

    """
    Entrée : aucune
    Sortie : entier

    Renvoie le nombre de noeuds de l'arbre
    """
    def number_nodes(self):
        return len(self.nodes)

    """
    Entrée :
        node_children (liste d'objets Node) : liste de fils d'un noeud
    Sortie : liste d'objets Node
    
    Parcourt les fils noeud courant en largeur et renvoie ses petits-fils
    """
    def breadth_path(self, node_children):
        # Liste des petits-fils du noeud courant
        node_grand_children = []

        # Parcours des fils du noeud courant
        for node_child in node_children:
            if node_child != None:
                # Petit-fils du noeud courant
                node_children_child = self.get_node_children(node_child)
                node_grand_children.extend(node_children_child)

        return node_grand_children

    """
    Entrée : aucune
    Sortie : aucune
    
    Trie la liste de noeuds de l'arbre de sorte que l'on puisse le parcourir en largeur
    
    Exemple :
        On a la liste de noeuds [noeud1, noeud2, noeud3, noeud4], où noeud3 est la racine de l'arbre
        Les liens de parenté sont : noeud3 père de noeud2 et noeud4, noeud4 père de noeud1 (noeud1 et noeud2 sont
        des feuilles)
        Liste triée : [noeud3, noeud2, noeud4, noeud1]
    """
    def sort_nodes_root_leaves(self):
        # Liste de noeuds triée
        sort_nodes = []
        nmb_nodes = self.number_nodes()

        # Racine de l'arbre
        root = self.get_root()
        # Ajout de la racine à la liste sort_nodes
        sort_nodes.append(root)

        # Fils de la racine
        node_children = self.get_node_children(root)

        # À partir des fils de la racine, on remplit la liste sort_nodes
        while len(sort_nodes) != nmb_nodes:
            # Petits-fils du noeud courant
            node_grand_children = self.breadth_path(node_children)

            # Tri des noeuds
            sort_nodes.extend(node_children)
            # Descente dans l'arbre
            node_children = node_grand_children

        self.set_nodes(sort_nodes)

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : liste d'objets Node
    
    Renvoie l'ensemble des noeuds du sous-arbre engendré par le noeud node
    """
    def sub_tree_from_node(self, node):
        # Sous-arbre
        nodes_sub_tree = []

        # Le noeud node est dans le sous-arbre renvoyé
        nodes_sub_tree.append(node)

        # Fils du noeud node
        node_children = self.get_node_children(node)

        while node_children != []:
            node_grand_children = self.breadth_path(node_children)

            nodes_sub_tree.extend(node_children)
            node_children = node_grand_children

        return nodes_sub_tree

    """
    Entrée :
        leaves_values (liste de réels flottants, d'entiers et/ou de chaine de caractères) :
        liste des valeurs des feuilles de l'arbre
    Sortie : aucune
    
    Ajoute aux feuilles de l'arbre les valeurs contenues dans la liste leaves_values
    """
    def add_leaves_values(self, leaves_values):
        for (leaf, value) in leaves_values:
            leaf.add_value(value)
            self.set_node(leaf)

    """
    Entrée :
        ind_par (entier) : indice d'un paramètre
    Sortie : aucune
    
    Supprime des feuilles de l'arbre la (ind_par+1)-ème valeur
    """
    def delete_leaves_values(self, ind_par):
        leaves = self.get_leaves()

        for leaf in leaves:
            values = leaf.get_values()
            values.pop(ind_par)

    """
    Entrée :
        id (entier) : identifiant d'un noeud
    Sortie : booléen
    
    Renvoie vrai ssi le noeud d'identifiant id existe
    """
    def node_exists(self, id):
        for node in self.nodes:
            id_node = node.get_id()

            if id_node == id:
                return True

        return False

    """
    Entrée :
        name (chaine de caractères) : nom d'un noeud
    Sortie : booléen
    
    Renvoie vrai ssi le nom name est attribué à un noeud de l'arbre
    """
    def name_node_exists(self, name):
        for node in self.nodes:
            name_node = node.get_name()

            if name_node == name:
                return True

        return False

    """
    Entrée : aucune
    Sortie : entier
    
    Renvoie l'identifiant minimum d'un noeud tel que son ajout à l'arbre soit valide

    Exemple :
        Des noeuds dans un arbre sont identifiés par 1, 2, 5, 7
        Alors l'identifiant renvoyé est 3
    """
    def generate_id_add_node(self):
        id = 1

        # On cherche le plus petit identifiant qui n'existe pas
        while self.node_exists(id):
            id += 1

        return id

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : aucune
    
    Ajoute la nouvelle racine node à l'arbre
    """
    def add_root(self, node):
        # Ajout du noeud node à la liste des noeuds de l'arbre
        self.add_node(node, root=True)

        id = node.get_id()
        # Fils de la nouvelle racine
        node_children = self.get_node_children(node)

        # Chaque fils du noeud node doit l'avoir comme nouveau parent
        for node_child in node_children:
            node_child.add_parent(id)
            self.set_node(node_child)

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : aucune
    
    Ajoute la nouvelle feuille node à l'arbre
    """
    def add_leaf(self, node):
        # Ajout du noeud node à la liste des noeuds de l'arbre
        self.add_node(node)

        id = node.get_id()
        # Parents de la nouvelle feuille
        node_parents = self.get_node_parents(node)

        # Chaque parent du noeud node doit l'avoir comme nouveau fils
        for node_parent in node_parents:
            # Cas particulier : un parent du noeud node peut être au préalble une feuille
            if node_parent.is_leaf():
                # Dans ce cas, on supprime toutes ses valeurs
                node_parent.clear_values()
            else:
                parent_gate = node_parent.get_gate()

                if "/" in parent_gate:
                    gate = set_gate_comb(parent_gate, 1)
                    node_parent.set_gate(gate)

            node_parent.add_child(id)
            self.set_node(node_parent)

        # Tri de la liste des noeuds de l'arbre
        self.sort_nodes_root_leaves()

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : aucune
    
    Insère le noeud node à l'arbre
    """
    def insert_node(self, node):
        # Ajout du noeud node à la liste des noeuds de l'arbre
        self.add_node(node)

        # Identifiant du noeud node
        id = node.get_id()
        # Parents du noeud node
        node_parents = self.get_node_parents(node)
        # Fils du noeud node
        node_children = self.get_node_children(node)

        # On supprime les liens de parentés en commun entre les parents et les fils du noeud node
        for node_parent in node_parents:
            # Fils du noeud node_parent
            node_children_parent = self.get_node_children(node_parent)

            for node_child_parent in node_children_parent:
                # node_child_parent fils de node et d'un parent : suppression du lien avec le parent
                if node_child_parent in node_children:
                    # Identifiant du noeud node_child_parent
                    child_parent = node_child_parent.get_id()
                    # Identifiant du noeud node_parent
                    parent = node_parent.get_id()

                    # Suppression réciproque

                    node_parent.delete_child(child_parent)
                    node_child_parent.delete_parent(parent)

                    self.set_node(node_parent)
                    self.set_node(node_child_parent)

            # node_parent a comme nouveau fils le noeud node
            node_parent.add_child(id)
            self.set_node(node_parent)

        # Chaque fils du noeud node doit l'avoir comme nouveau parent
        for node_child in node_children:
            node_child.add_parent(id)
            self.set_node(node_child)

        self.sort_nodes_root_leaves()

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : aucune
    
    Ajoute le noeud node à l'arbre en distinguant 3 cas :
        - 1 : le noeud node n'a pas de parent : ajout d'une nouvelle racine
        - 2 : le noeud node n'a pas de fils : ajout d'une nouvelle feuille
        - 3 : le noeud node a au moins un parent et au moins un fils : insertion du noeud
    """
    def add_node_tree(self, node):
        # Cas 1
        if node.is_root():
            self.add_root(node)
        # Cas 2
        elif node.is_leaf():
            self.add_leaf(node)
        # Cas 3
        else:
            self.insert_node(node)

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : aucune
    
    Supprime les parents du noeud node
    """
    def delete_node_parents(self, node):
        id = node.get_id()
        node_parents = self.get_node_parents(node)

        for node_parent in node_parents:
            id_node_parent = node_parent.get_id()

            # node_parent est un parent de node : on le supprime
            node.delete_parent(id_node_parent)
            # Réciproquement, node est un fils de node_parent : on le supprime
            node_parent.delete_child(id)

            self.set_node(node)
            self.set_node(node_parent)

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : aucune
    
    Supprime les fils du noeud node
    """
    def delete_node_children(self, node):
        id = node.get_id()
        node_children = self.get_node_children(node)

        for node_child in node_children:
            id_node_child = node_child.get_id()

            # node_child est un fils de node : on le supprime
            node.delete_child(id_node_child)
            # Réciproquement, node est un parent de node_child : on le supprime
            node_child.delete_parent(id)

            self.set_node(node)
            self.set_node(node_child)

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : liste d'objets Node
    
    Supprime le noeud node de l'arbre
    Renvoie la liste des parents du noeud node
    """
    def delete_node_tree(self, node):
        node_parents = self.get_node_parents(node)
        node_children = self.get_node_children(node)

        # Suppression des parents du noeud node
        self.delete_node_parents(node)
        # Suppression des fils du noeud node
        self.delete_node_children(node)

        # On ajoute les fils du noeud node à ses parents
        for node_parent in node_parents:
            parent_gate = node_parent.get_gate()

            if "/" in parent_gate:
                nmb_children = len(node_children)

                gate = set_gate_comb(parent_gate, nmb_children-1)
                node_parent.set_gate(gate)

                self.set_node(node_parent)

            id_node_parent = node_parent.get_id()

            for node_child in node_children:
                id_node_child = node_child.get_id()

                node_child.add_parent(id_node_parent)
                node_parent.add_child(id_node_child)

                self.set_node(node_child)
                self.set_node(node_parent)

            ind_parent = node_parents.index(node_parent)
            node_parents[ind_parent] = node_parent

        # Suppression du noeud node
        self.delete_node(node)

        self.sort_nodes_root_leaves()

        return node_parents

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : liste d'objets Node
    
    Suprrime le noeud node et le sous-arbre engendré
    Renvoie la liste des parents du noeud node
    """
    def delete_sub_tree_from_node(self, node):
        # Parents du noeud node
        node_parents = self.get_node_parents(node)

        for node_parent in node_parents:
            parent_gate = node_parent.get_gate()

            if "/" in parent_gate:
                gate = set_gate_comb(parent_gate, -1)

                node_parent.set_gate(gate)

                self.set_node(node_parent)

        # Sous-arbre engendré par le noeud node
        sub_tree = self.sub_tree_from_node(node)

        # Suppression des liens de parenté entre chaque noeud du sous-arbre
        for node_sub_tree in sub_tree:
            self.delete_node_parents(node_sub_tree)

        # Suppression du sous-arbre
        self.delete_nodes(sub_tree)

        self.sort_nodes_root_leaves()

        return node_parents

    """
    Entrée : aucune
    Sortie : liste de réels flottants, d'entiers et/ou de chaines de caractères

    Saisie pour ajouter des valeurs associées à un nouveau paramètre aux feuilles de l'arbre
    Renvoie la liste des valeurs saisies
    """
    def input_add_leaves_values(self):
        print("Adding values\n")

        # Feuilles de l'arbre
        leaves = self.get_leaves()
        leaves_values = []

        for leaf in leaves:
            # Identifiant de la feuille leaf
            id_leaf = leaf.get_id()
            # Nom de la feuille leaf
            name_leaf = leaf.get_name()

            print("Node ", id_leaf, ": ", name_leaf, sep="")

            # Saisie d'une nouvelle valeur
            add_value = generic_type_input("Added value: ", float)

            # L'utilisateur doit ressaisir une valeur tant qu'elle n'est pas valide
            while add_value == "\0":
                print("\nError input: enter a real number or a symbolic formula")
                add_value = generic_type_input("Added value: ")

                if add_value != "\0":
                    print()

            if type(add_value) != str:
                # On privilégiera une valeur entière dans la mesure du possibe
                if add_value - int(add_value) == 0.0:
                    add_value = int(add_value)

            leaves_values.append((leaf, add_value))

            print()

        return leaves_values

    """
    Entrée : aucune
    Sortie : liste de réels flottants, d'entiers et/ou de chaines de caractères
    
    Saisie des valeurs d'une feuille pour tous les paramètres de l'arbre
    Renvoie la liste des valeurs saisies
    """
    def input_values(self):
        values = []

        # Paramètres de l'arbre
        parameters = self.pro.get_parameters()

        for parameter in parameters:
            print("\nParameter:", parameter)

            # Saisie d'une valeur
            value = generic_type_input("Enter a value: ", float)

            # L'utilisateur doit ressaisir une valeur tant qu'elle n'est pas valide
            while value == "\0":
                print("\nError input: enter a real number or a symbolic formula")
                value = generic_type_input("Enter a value: ", float)

                if value != "\0":
                    print()

            if type(value) != str:
                # On privilégiera une valeur entière dans la mesure du possibe
                if value - int(value) == 0.0:
                    value = int(value)

            values.append(value)

        return values

    """
    Entrée : aucune
    Sortie : objet Node
    
    Saisie pour l'ajout d'un noeud
    """
    def input_add_node(self):
        # Noeud renvoyé lors d'une erreur
        node_error = Node()

        nmb_nodes = self.number_nodes()

        print("*\n")

        # Génération de l'identifiant
        id = self.generate_id_add_node()

        print("ID.:", id)

        print("\n*\n")

        # Saisie du nom
        name = input("Name: ")

        while self.name_node_exists(name):
            print("\nThe name '", name, "' is already assigned to a node of the tree", sep="")
            name = input("Name: ")

        print("\n*\n")

        # Saisie du nombre de parents
        nmb_parents = generic_type_input("Number of parents: ", int)

        while nmb_parents == "\0":
            print("\nError input: enter an integer")
            nmb_parents = generic_type_input("Number of parents: ", int)

            if nmb_parents != "\0":
                print()

        # Erreur si le nombre de parents saisi est trop élevé
        if nmb_parents > nmb_nodes:
            print("\nToo much parents")
            time.sleep(2)

            return node_error

        parents = []

        # Le nouveau noeud a des parents
        if nmb_parents != 0:
            add_parent = 1

            # L'utilisateur choisit les parents du nouveau noeud en saisissant leurs identifiants
            while len(parents) != nmb_parents:
                if nmb_parents > 1:
                    print(add_parent, "- ", sep="", end="")

                # Saisie de l'identifiant d'un parent
                parent = generic_type_input("ID.: ", int)

                while parent == "\0":
                    print("\nError input: enter an integer")
                    parent = generic_type_input("ID.: ", int)

                    if parent != "\0":
                        print()

                # L'utilisateur doit saisir un nouvel identifiant d'un parent si il n'existe pas dans l'arbre
                if not (self.node_exists(parent)):
                    print("\nError input: the node", parent, "does not exist\n")
                # Identifiant correct
                else:
                    # Parent du noeud à ajouter
                    node_parent = self.get_node(parent)

                    parents.append(parent)
                    add_parent += 1

                    # Cas particulier : le parent était au préalable une feuille
                    if (node_parent.is_leaf()):
                        children_parent = node_parent.get_children()
                        nmb_children_parent = len(children_parent)

                        # On lui ajoute une porte logique
                        gate_parent = input("Parent's gate: ")

                        # L'utilisateur doit ressaisir une porte logique tant qu'elle n'est pas valide
                        while not (gate_is_valid(gate_parent, nmb_children_parent)):
                            print("\nError input: the gate '", gate_parent, "' is not valid", sep="")
                            gate_parent = input("Parent's gate: ")

                        node_parent.set_gate(gate_parent)

                        # On lui supprime ses valeurs
                        node_parent.clear_values()

                        self.set_node(node_parent)

        print("\n*\n")

        # Saisie du nombre de fils
        nmb_children = generic_type_input("Number of children: ", int)

        while nmb_children == "\0":
            print("\nError input: enter an integer")
            nmb_children = generic_type_input("Number of children: ", int)

            if nmb_children != "\0":
                print()

        # Erreur si le nombre de fils saisi est trop élevé
        if nmb_children > nmb_nodes:
            print("\nToo much children")
            time.sleep(2)

            return node_error

        # Le nouveau noeud n'a pas de fils
        if nmb_children == 0:
            # Erreur si l'utilisateur avait aussi choisi de n'attribuer aucun parent au nouveau noeud
            if parents == []:
                print("\nImpossible to add such a node")
                time.sleep(2)

                return node_error

            # Pas de fils
            children = []

            # Pas de porte logique
            gate = ""

            # Saisie des valeurs pour tous les paramètres de l'arbre
            values = self.input_values()
        # Le nouveau noeud a des fils
        else:
            children = []

            add_child = 1

            # L'utilisateur choisit les fils du nouveau noeud en saisissant leurs identifiants
            while len(children) != nmb_children:
                if nmb_children > 1:
                    print(add_child, "- ", sep="", end="")

                # Saisie de l'identifiant d'un fils
                child = generic_type_input("ID.: ", int)

                while child == "\0":
                    print("\nError input: enter an integer")
                    child = generic_type_input("ID: ", int)

                    if child != "\0":
                        print()

                # L'utilisateur doit saisir un nouvel identifiant d'un parent si il n'existe pas dans l'arbre
                if not (self.node_exists(child)):
                    print("\nError input: the node", child, "does not exist\n")
                # Identifiant correct
                else:
                    children.append(child)
                    add_child += 1

            # On vérifie que si le nouveau noeud est une racine, elle est unique
            if parents == []:
                root = self.get_root()
                id_root = root.get_id()

                # Erreur si l'utilisateur essaye d'ajouter une seconde racine
                if id_root not in children:
                    print("\nImpossible to add a second root")
                    time.sleep(2)

                    return node_error

            print("\n*\n")

            # Saisie de la porte logique
            gate = input("Logical gate: ")

            # L'utilisateur doit ressaisir une porte logique tant qu'elle n'est pas valide
            while not (gate_is_valid(gate, nmb_children)):
                print("\nError input: the gate '", gate, "' is not valid", sep="")
                gate = input("Logical gate: ")

            # Pas de valeurs
            values = []

        # Création du noeud
        node = Node(id, name, parents, children, gate, values)

        return node

    """
    Entrée : aucune
    Sortie : entier
    
    Saisie pour la suppression d'un noeud
    """
    def input_delete_node(self):
        print("*\n")

        # Saisie de l'identifiant de l'arbre
        id = generic_type_input("ID.: ", int)

        # L'utilisateur doit ressaisir un identifiant tant il n'est pas entier
        while id == "\0":
            print("\nError input: enter an integer")
            id = generic_type_input("ID: ", int)

            if id != "\0":
                print()

        # Erreur si le noeud d'identifiant id n'existe pas
        if not (self.node_exists(id)):
            print("\nThe node", id, "does not exist")
            time.sleep(2)

            return 1

        # Noeud à supprimer
        del_node = self.get_node(id)

        # Erreur si l'utilisateur tente de supprimer la racine de l'arbre
        if del_node.is_root():
            print("\nImpossible to delete the root\n")
            time.sleep(2)

            return 1

        print("\n*\n")

        print("Delete the sub-tree from this node?")
        # L'utilisateur peut soit supprimer le noeud uniquement, soit en plus le sous-arbre engendré
        del_choice = input("Type Y or y: ")

        # Suppression du noeud et du sous-arbre engendré
        if del_choice == "Y" or del_choice == "y":
            del_node_parents = self.delete_sub_tree_from_node(del_node)
        # Suppression du noeud uniquement
        else:
            del_node_parents = self.delete_node_tree(del_node)

        for del_node_parent in del_node_parents:
            # Si un parent du noeud supprimé est une feuille, on lui ajoute des valeurs pour chaque paramètre
            if del_node_parent.is_leaf():
                id_del_node_parent = del_node_parent.get_id()

                print("\nNode", id_del_node_parent)

                del_node_parent.clear_gate()

                leaves_values = self.input_values()
                del_node_parent.set_values(leaves_values)

                self.set_node(del_node_parent)

        return 0

    """
    Entrée : aucune
    Sortie : aucune
    
    L'utilisateur initialise l'arbre lui même l'arbre
    """
    def init_tree(self):
        # Initialisation des paramètres et des règles de calcul et d'optimisation de l'arbre
        self.pro.init_parameters_rules()

        clear()

        # Création des noeuds et des valeurs de l'arbre

        print("CREATION OF THE NODES AND THE VALUES OF THE TREE")
        print("================================================\n")

        # Liste des paramètres de l'arbre
        parameters = self.pro.get_parameters()
        # Liste des identifiants de tous les noeuds (initialement, contient celui de la racine, égal à 1)
        ids = [1]
        # Liste de couple d'identifiants (père,fils)
        parents_children = []

        i = 0

        # La boucle s'arrête lorsque l'utilisateur créé la dernière feuille
        while i < len(ids):
            # Identifiant du nouveau noeud à créer
            id = ids[i]

            # Liste des parents du noeud courant
            parents = []

            # Complétion de la liste des parents du noeud courant
            for tuple in parents_children:
                (p, c) = tuple

                if c == id:
                    parents.append(p)

            # Premier noeud : racine de l'arbre
            if i == 0:
                print("Root node\n")
            # Autres types de noeuds (feuilles ou pas)
            else:
                # Affichage de l'identifiant et des parents du noeud

                print("Node", id, "(parent:", end="")

                for parent in parents:
                    node_parent = self.get_node(parent)
                    name_parent = node_parent.get_name()

                    print(" ", parent, " (", name_parent, ")", sep="", end="")

                print(")\n")

            # Saisie du nom
            name = input("Name: ")

            # Saisie du nombre de fils
            nmb_children = generic_type_input("Number of children: ", int)

            while nmb_children == "\0":
                print("\nError input: enter an integer")
                nmb_children = generic_type_input("Number of children: ", int)

                if nmb_children != "\0":
                    print()

            # Nombre de fils nul : l'utilisateur a créé une feuille
            if nmb_children == 0:
                # Pas de fils
                children = []

                # Pas de porte logique
                gate = ""

                # Ajout des valeurs pour tous les paramètres de l'arbre
                values = self.input_values()
            # Nombre de fils non nul : l'utilisateur a créé un parent
            else:
                # Génération de la liste des fils
                children = list(range(len(ids)+1, len(ids)+nmb_children+1))

                # Ajout des couples d'identifiants (noeud courant, fils) à la liste parents_children
                for child in children:
                    parents_children.append((id, child))

                # Ajout des identifiants des fils à la liste ids
                ids.extend(children)

                # Saisie de la porte logique
                gate = input("Logical gate: ")

                # L'utilisateur doit ressaisir une porte logique tant qu'elle n'est pas valide
                while not (gate_is_valid(gate, nmb_children)):
                    print("\nError input: the gate '", gate, "' is not valid", sep="")
                    gate = input("Logical gate: ")

                # Pas de valeurs
                values = []

            # Création du noeud
            node = Node(id, name, parents, children, gate, values)
            self.add_node(node)

            i += 1

            print("\n*\n")

    """
    Entrée : aucune
    Sortie : aucune
    
    Affichage de l'arbre
    """
    def print_tree(self):
        # Affichage des paramètres

        print("PARAMETERS\n")
        self.pro.print_parameters()

        print("\n\n*\n")

        # Affichage des noeuds

        print("NODES\n")

        for node in self.nodes:
            node.print_node()

            # Le noeud node n'est pas une feuille : affichage des règles de calcul associées à sa porte logique
            if not (node.is_leaf()):
                gate = node.get_gate()
                self.pro.print_rules(gate)

            if node != self.nodes[-1]:
                print()

        print("\n*\n")

        # Affichage des règles d'optimisation (scénario)

        print("SCENARIO\n")
        self.pro.print_optimization()

    """
    Entrée :
        node (objet Node) : noeud
    Sortie : liste de listes d'entiers
    
    Renvoie tous les chemins du parcours de l'arbre en partant du noeud node
    """
    def find_path(self, node):
        # Identifiant du noeud node
        id = node.get_id()

        # Cas terminal : node est une feuille
        if node.is_leaf():
            return [id]
        # Tout autre type de noeud
        else:
            # Porte logique du noeud
            gate = node.get_gate()
            # Fils du noeud
            node_children = self.get_node_children(node)

            # Deux cas : gate est une porte logique AND ou OR

            # Porte logique AND
            if gate == "AND":
                # Conservation de tous les fils du noeud : tous les événements associés doivent se réaliser
                return [id, [self.find_path(node_child) for node_child in node_children]]
            # Porte logique OR
            else:
                # Ajout des fils du noeud : au moins un des événements associés doit se réaliser
                return [id] + [self.find_path(node_child) for node_child in node_children]

    """
    Entrée :
        node (objet Node) : noeud
        parameter (chaine de caractères) : paramètre de l'arbre
    Sortie : chaine de caractères
    
    Renvoie l'expression symbolique pour le chemin du parcours de l'arbre issu du noeud node associé au paramètre
    parameter
    """
    def find_symbolic_expression(self, node, parameter):
        # Indice du paramètre parameter
        ind_par = self.pro.get_index_parameter(parameter)

        # Cas terminal : node est une feuille
        if node.is_leaf():
            # Valeurs du noeud node
            values = node.get_values()
            # Valeur associée au paramètre parameter
            value_par = values[ind_par]

            return str(value_par)
        else:
            symb_expr = ""

            # Porte logique du noeud
            gate = node.get_gate()
            # Fils du noeud
            node_children = self.get_node_children(node)
            # Règle de calcul associée à la porte logique gate pour le paramètre parameter
            rule_gate = self.pro.get_rule_gate_ind(gate, ind_par)

            # Deux cas : gate est une porte logique AND ou OR

            # Porte logique AND
            if gate == "AND":
                # Nombre de fils
                nmb_children = len(node_children)

                # Au moins trois fils
                if nmb_children >= 3:
                    for node_child in node_children:
                        # node_child est le dernier fils
                        if node_child == node_children[-1]:
                            symb_expr += self.find_symbolic_expression(node_child, parameter) + ")"
                        # Tout autre fils
                        else:
                            symb_expr += self.find_symbolic_expression(node_child, parameter) + " " + rule_gate + " "

                            if node_child == node_children[0]:
                                symb_expr = "(" + symb_expr
                # Deux fils
                elif nmb_children == 2:
                    # Premier fils
                    first_node_child = node_children[0]
                    # Second fils
                    second_node_child = node_children[1]

                    # Expression symbolique pour le premier fils
                    first_symb_expr = self.find_symbolic_expression(first_node_child, parameter)
                    # Expression symbolique pour le second fils
                    second_symb_expr = self.find_symbolic_expression(second_node_child, parameter)

                    symb_expr = "(" + first_symb_expr + " " + rule_gate + " " + second_symb_expr + ")"
                # Un seul fils
                else:
                    # Seul et unique fils
                    first_node_child = node_children[0]
                    symb_expr = rule_gate + " " + self.find_symbolic_expression(first_node_child, parameter)

                return symb_expr
            # Porte logique OR
            else:
                # Premier fils
                first_node_child = node_children[0]
                return self.find_symbolic_expression(first_node_child, parameter)

    """
    Entrée :
        id (entier) : identifiant d'un noeud
    Sortie : liste d'objets Tree

    Reformate l'arbre en renvoyant la liste des sous-arbres en supprimant les fils du noeud node ssi il est muni
    d'une porte logique OR ou k/n
    """
    def formatting_tree(self, id):
        split_formatting = []

        # Noeud d'identifiant id
        node = self.get_node(id)
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
                tmp_tree = self.deepcopy()

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
                tmp_tree = self.deepcopy()

                # Suprression des noeuds fils et des sous-arbres engendrés
                for tmp_id_child in tmp_children:
                    if tmp_id_child != id_child:
                        node_child = tmp_tree.get_node(tmp_id_child)
                        tmp_tree.delete_sub_tree_from_node(node_child)

                split_formatting.append(tmp_tree)

        return split_formatting

    """
    Entrée : aucune
    Sortie : liste d'objets Tree

    Parcourt l'arbre et renvoie la liste des sous-arbres issus du formatage effectué lors d'un appel de la
    fonction formatting_tree
    """
    def pathway_tree(self):
        nodes = self.get_nodes()
        id_nodes_formatting = []

        # Stockage des noeuds munis d'une porte logique OR ou k/n dans la liste id_nodes_formatting
        for node in nodes:
            gate = node.get_gate()

            if not (node.is_leaf()) and gate != "AND":
                id = node.get_id()
                id_nodes_formatting.append(id)

        list_tree = [self]

        # Création des sous-arbres issus du formatage de l'arbre
        for id_node in id_nodes_formatting:
            tmp = copy.deepcopy(list_tree)

            for tmp_tree in tmp:
                if tmp_tree.node_exists(id_node):
                    list_split_tree = tmp_tree.formatting_tree(id_node)

                    list_tree += list_split_tree
                    list_tree.pop(0)

        return list_tree

    """
    Entrée :aucune
    Sortie : liste de liste d'objets Tree

    Renvoie tous les chemins possibles de l'arbre
    """
    def paths_tree(self):
        # Sous-arbres par formatage de l'arbre
        pathway = self.pathway_tree()
        list_paths = []

        # Parcours de chaque sous-arbre en partant de la racine et stockage du chemin dans la liste list_paths
        for pw in pathway:
            root = pw.get_root()
            paths = pw.find_path(root)

            list_paths.append(paths)

        return list_paths

    """
    Entrée :
        parameters (liste de chaines de caractères) : paramètres de l'arbre
    Sortie : tuple

    Renvoie le 3-uplet de listes (chemins, expressions symboliques développées, expressions symboliques simplifiées)
    """
    def data_tree(self, parameters):
        # Sous-arbres par formatage de l'arbre
        pathway = self.pathway_tree()

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

        return (all_paths, all_dev, all_simp)

    """

    """
    def input_evaluation_variables(self, symb_expr):
        variables = all_var_in_expr(symb_expr)
        evaluations = []

        for variable in variables:
            print("    ", end="")

            inp_str = variable + " := "
            eval_var = generic_type_input(inp_str, int)

            while eval_var == "\0":
                print("\nError input: '", eval_var, "' is not a valid evaluation (enter an integer)")
                eval_var = generic_type_input(inp_str, float)

            str_eval = str(eval_var)
            evaluations.append(eval_var)

        return (variables, evaluations)

    """
    Entrée : aucune
    Sortie : dictionnaire
    
    Converit la liste des noeuds de l'arbre en un dictionnaire
    Le dictionnaire contient une unique clé "Nodes" dont la valeur associée est la liste des noeuds convertis en
    dictionnaires
    """
    def from_nodes_to_dict(self):
        dict = {}
        # Liste associée à la clé Nodes du dictionnaire dict
        list_dict = []

        for node in self.nodes:
            # Conversion du noeud node en un dictionnaire
            dict_node = node.from_node_to_dict()
            list_dict.append(dict_node)

        # Clé pour les noeuds de l'arbre
        dict["Nodes"] = list_dict

        return dict

    """
    Entrée :
        dict (dictionnaire) : noeuds de l'arbre
    Sortie : aucune
    
    Créé la liste des noeuds de l'arbre à partir du dictionnaire dict
    """
    def from_dict_to_nodes(self, dict):
        list_nodes = []

        # Liste des dictionnaires relatifs à chacun des noeuds de l'arbre
        nodes = dict["Nodes"]

        for dict_node in nodes:
            # Noeud vide
            node = Node()
            # Création du noeud node à partir du dictionnaire dict_node
            node.from_dict_to_node(dict_node)

            list_nodes.append(node)

        # Création de la liste des noeuds de l'arbre
        self.set_nodes(list_nodes)

    """
    Entrée : aucune
    Sortie : dictionnaire
    
    Convertit un arbre en un dictionnaire
    Le dictionnaire contient quatre clés :
        - "Parameters" : paramètres de l'arbre (liste de chaine de caractères)
        - "Compute rules" : règles de calcul associée à chaque porte logique pour tous les paramètres de l'arbre
        (dictionnaire)
        - "Optimization rules" : règles d'optimisation associée à tous les paramètres de l'arbre (liste de chaine
        de caractères)
        - "Nodes" : noeuds de l'arbre (liste de dictionnaires)
    """
    def from_tree_to_dict(self):
        dict = {}

        # Dictionnaire pour les paramètres et les règles de calcul et d'optimisation de l'arbre
        dict_pro = self.pro.from_pro_to_dict()
        dict.update(dict_pro)

        # Dictionnaire pour les noeuds de l'arbre
        dict_nodes = self.from_nodes_to_dict()
        dict.update(dict_nodes)

        return dict

    """
    Entrée :
        dict (dictionnaire) : informations relatives à l'arbre
    Sortie : aucune
    
    Créé l'arbre à partir du dictionnaire dict
    """
    def from_dict_to_tree(self, dict):
        # Paramètres et règles de calcul et d'optimisation
        pro = Parameters()
        pro.from_dict_to_pro(dict)

        self.set_pro(pro)

        # Noeuds
        self.from_dict_to_nodes(dict)

    """
    Entrée :
        name_file (chaine de caractères) : nom d'un fichier JSON
    Sortie : aucune
    
    Sauvegarde en local l'arbre sous le format JSON dans un fichier nommé name_file
    """
    def from_tree_to_json(self, name_file):
        # Conversion de l'arbre en dictionnaire
        dict = self.from_tree_to_dict()

        with open(name_file, "w") as f:
            json.dump(dict, f, indent=2)

    """
    Entrée :
        name_file (chaine de caractères) : nom d'un fichier JSON
    Sortie : aucune
    
    Créé l'arbre à partir du chargement du fichier JSON nommé name_file
    """
    def from_json_to_tree(self, name_file):
        with open(name_file, "r") as f:
            dict = json.load(f)

        # Création de l'arbre à partir du dictionnaire dict
        self.from_dict_to_tree(dict)
