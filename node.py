"""
Fichier node.py

Classe Node : noeud d'un arbre

Un noeud est implémenté de telle sorte que l'on connaît ses parents et ses fils, et tout autre type d'informations
aidant à la création d'un arbre
"""


class Node:
    """
    Constructeur

    Attributs de la classe :
        - id (entier) :
            l'identifiant du noeud (unique)
        - name (chaine de caractères) :
            nom du noeud (unique)
        - parents (liste d'entiers) :
            parent(s) du noeud (liste vide ssi le noeud est la racine de l'arbre)
        - children (liste d'entiers) :
            fils du noeud (liste vide ssi le noeud est une feuille de l'arbre)
        - gate (chaine de caractères) :
            porte logique du noeud (AND, OR, NOT, XOR ou SOR, chaine de caractères vide ssi le noeud est une feuille
            de l'arbre)
        - values (liste de réels flottants, d'entiers et/ou de chaines de caractères) :
            valeurs d'une feuille (liste vide ssi le noeud est la racine de l'arbre ou est interne) : réelles,
            entières ou variables
    """
    def __init__(self, id=0, name="", parents=[], children=[], gate="", values=[]):
        self.id = id
        self.name = name
        self.parents = parents
        self.children = children
        self.gate = gate
        self.values = values

    """
    Entrée : aucune
    Sortie : entier
    
    Getter : renvoie l'identifiant du noeud
    """
    def get_id(self):
        return self.id

    """
    Entrée : aucune
    Sortie : chaine de caractères
    
    Getter : renvoie le nom du noeud
    """
    def get_name(self):
        return self.name

    """
    Entrée : aucune
    Sortie : liste d'entiers
    
    Getter : renvoie la liste des identifiants des parents du noeud
    """
    def get_parents(self):
        return self.parents

    """
    Entrée : aucune
    Sortie : liste d'entiers
    
    Getter : renvoie la liste des identifiants des fils du noeud
    """
    def get_children(self):
        return self.children

    """
    Entrée : aucune
    Sortie : chaine de caractères
    
    Getter : renvoie la porte logique du noeud
    """
    def get_gate(self):
        return self.gate

    """
    Entrée : aucune
    Sortie : liste de réels flottants
    
    Getter : renvoie la liste des valeurs du noeud
    """
    def get_values(self):
        return self.values

    """
    Entrée :
        id (entier) : identifiant du noeud
    Sortie : aucune
    
    Setter : modifie l'identifiant du noeud
    """
    def set_id(self, id):
        self.id = id

    """
    Entrée :
        name (chaine de caractères) : nom du noeud
    Sortie : aucune
    
    Setter : modifie le nom du noeud
    """
    def set_name(self, name):
        self.name = name

    """
    Entrée :
        parents (liste d'entiers) : liste des identifiants des parents du noeud
    Sortie : aucune
    
    Setter : modifie les parents du noeud
    """
    def set_parents(self, parents):
        self.parents = parents

    """
    Entrée :
        children (liste d'entiers) : liste des identifiants des fils du noeud
    Sortie : aucune
    
    Setter : modifie les fils du noeud
    """
    def set_children(self, children):
        self.children = children

    """
    Entrée :
        gate (chaine de caractères) : porte logique du noeud
    Sortie : aucune
    
    Setter : modifie la porte logique du noeud
    """
    def set_gate(self, gate):
        self.gate = gate

    """
    Entrée :
        parents (liste de réels flottants, d'entiers et/ou de chaine de caractères) :
        liste des valeurs du noeud
    Sortie : aucune
    
    Setter : modifie les valeurs du noeud
    """
    def set_values(self, values):
        self.values = values

    """
    Entrée : aucune
    Sortie : aucune
    
    Vide le tableau de valeurs du noeud
    """
    def clear_values(self):
        self.values = []

    """
    Entrée : aucune
    Sortie : booléen
    
    Renvoie vrai ssi le noeud est la racine de l'arbre (i.e. n'a pas de parents)
    """
    def is_root(self):
        return (self.parents == [])

    """
    Entrée : aucune
    Sortie : booléen
    
    Renvoie vrai ssi le noeud est une feuille de l'arbre (i.e. n'a pas de fils)
    """
    def is_leaf(self):
        return (self.children == [])

    """
    Entrée :
        parent (entier) : identifiant du noeud parent
    Sortie : aucune
    
    Ajoute au noeud le parent dont l'identifiant est parent
    """
    def add_parent(self, parent):
        self.parents.append(parent)

    """
    Entrée :
        parent (entier) : identifiant du noeud parent
    Sortie : aucune
    
    Supprime du noeud le parent dont l'identifiant est parent
    """
    def delete_parent(self, parent):
        self.parents.remove(parent)

    """
    Entrée :
        child (entier) : identifiant du noeud fils
    Sortie : aucune
    
    Ajoute au noeud le fils dont l'identifiant est child
    """
    def add_child(self, child):
        self.children.append(child)

    """
    Entrée :
        child (entier) : identifiant du noeud fils
    Sortie : aucune
    
    Supprime du noeud le fils dont l'identifiant est child
    """
    def delete_child(self, child):
        self.children.remove(child)

    """
    Entrée :
        value (réel flottant) : valeur d'une feuille
    Sortie : aucune
    
    Ajoute au noeud la valeur value
    """
    def add_value(self, value):
        self.values.append(value)

    """
    Entrée : aucune
    Sortie : aucune
    
    Affiche le noeud
    """
    def print_node(self):
        # Affichage de l'identifiant du noeud
        print("Node", self.id, end="")

        # Nature du noeud : racine
        if self.is_root():
            print(" (root)")
        # Feuille
        elif self.is_leaf():
            print(" (leaf)")
        # Noeud interne
        else:
            print()

        # Affichage du nom du noeud
        print("  Name:", self.name)

        # Le noeud n'est pas la racine de l'arbre : affichage de son ou ses parent(s)
        if not (self.is_root()):
            if len(self.parents) > 1:
                print("  Parents' id.: ", end="")
            else:
                print("  Parent's id.: ", end="")

            for parent in self.parents:
                print(parent, end=" ")

            print()

        # Le noeud n'est pas une feuille de l'arbre : affichage de son ou ses fils et de sa porte logique
        if not (self.is_leaf()):
            if len(self.children) > 1:
                print("  Children's id.: ", end="")
            else:
                print("  Child's id.: ", end="")

            for child in self.children:
                print(child, end=" ")

            print()
            print("  Logical gate:", self.gate)
        # Le noeud est une feuille : affichage de ses valeurs
        else:
            print("  Values: ", end="")

            for values in self.values:
                print(values, end=" ")

            print()

    """
    Entrée : aucune
    Sortie : dictionnaire
    
    Convertit un noeud en un dictionnaire
    Les clés du dictionnaire sont les attributs du noeud
    """
    def from_node_to_dict(self):
        dict = {}

        # Clé pour l'identifiant
        id = self.get_id()
        dict["ID"] = id

        # Clé pour le nom
        name = self.get_name()
        dict["Name"] = name

        # Clé pour les identifiants des parents
        parents = self.get_parents()
        dict["Parents"] = parents

        # Clé pour les identifiants des fils
        children = self.get_children()
        dict["Children"] = children

        # Clé pour la porte logique
        gate = self.get_gate()
        dict["Gate"] = gate

        # Clé pour les valeurs
        values = self.get_values()
        dict["Values"] = values

        return dict

    """
    Entrée :
        dict (dictionnaire) : informations relatives à un noeud de l'arbre
    Sortie : aucune
    
    Créé un noeud à partir du dictionnaire dict
    """
    def from_dict_to_node(self, dict):
        # Identifiant
        id = dict["ID"]
        self.set_id(id)

        # Nom
        name = dict["Name"]
        self.set_name(name)

        # Parents
        parents = dict["Parents"]
        self.set_parents(parents)

        # Fils
        children = dict["Children"]
        self.set_children(children)

        # Porte logique
        gate = dict["Gate"]
        self.set_gate(gate)

        # Valeurs
        values = dict["Values"]
        self.set_values(values)
