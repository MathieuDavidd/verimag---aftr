"""
Fichier menu.py

Classe Menu : menu
Modifications de l'arbre
"""


import sys
import time
from functions import clear
from node import Node
from tree import Tree


class Menu:
    """
    Constructeur

    Attribut de la classe :
        tree (objet Tree) : arbre
    """
    def __init__(self, tree):
        self.tree = tree

    """
    Entrée : aucune
    Sortie : entier
    
    Ajout, suppression ou modification d'un paramètre
    Renvoie :
        - 0 ssi tout s'est bien déroulé
        - 1 sinon
    """
    def action_parameter(self):
        print("\n*\n")

        pro = self.tree.get_pro()
        # Paramètres de l'arbre
        parameters = pro.get_parameters()

        # 3 actions possibles : ajout, suppression et modification d'un paramètre

        print("Parameter")
        print("  Adding: type A or a")
        print("  Deleting: type D or d")
        print("  Modifying: type M or m\n")

        # Saisie du choix de l'utilisateur
        action = input("Action: ")

        # Choix : ajout d'un paramètre à l'arbre
        if action == "A" or action == "a":
            # Erreur si l'arbre contient déjà tous les paramètres possibles
            if len(parameters) == 4:
                print("\nImpossible to add a parameter")
                time.sleep(2)

                return 1

            print("\n*\n")

            # Saisie du paramètre à ajouter
            add_par = input("Enter the parameter you want to add: ")

            # CNS pour la génération d'erreur : le paramètre n'est pas valide ou existe déjà
            if not (pro.parameter_is_valid(add_par)) or pro.parameter_exists(add_par):
                print("\nThe parameter '", add_par, "' cannot be added", sep="")
                time.sleep(2)

                return 1

            print("\n*\n")

            # Couple (rules, opt) := (règles de calcul, règles d'optimisation)
            (rules, opt) = pro.input_add_parameter()
            # Ajout du paramètre à l'arbre
            pro.add_parameter_tree(add_par, rules, opt)

            print("\n*\n")

            # Ajout des valeurs associées au nouveau paramètre aux feuilles de l'arbre

            leaves_values = self.tree.input_add_leaves_values()
            self.tree.add_leaves_values(leaves_values)
        # Choix : suppression d'un paramètre de l'arbre
        elif action == "D" or action == "d":
            # Erreur si l'arbre ne contient qu'un seul paramètre
            if len(parameters) == 1:
                print("\nImpossible to delete a parameter")
                time.sleep(2)

                return 1

            print("\n*\n")

            # Saisie du paramètre à supprimer
            del_par = input("Enter the parameter you want to delete: ")

            # CN pour la génération d'erreur : le paramètre n'existe pas
            if not (pro.parameter_exists(del_par)):
                print("\nThe parameter '", del_par, "' does not exist", sep="")
                time.sleep(2)

                return 1

            # Suppression du paramètre et récupération de son indice
            ind_del_par = pro.delete_parameter_tree(del_par)

            # Suppression des valeurs associées au paramètre supprimé des feuilles de l'arbre
            self.tree.delete_leaves_values(ind_del_par)
        # Choix : modification d'un paramètre de l'arbre
        elif action == "M" or action == "m":
            print("\n*\n")

            # Saisie du paramètre à modifier
            mod_par = input("Enter the parameter you want to modify: ")

            # CN pour la génération d'erreur : le paramètre n'existe pas
            if not (pro.parameter_exists(mod_par)):
                print("\nThe parameter '", mod_par, "' does not exist", sep="")
                time.sleep(2)

                return 1

            print("\n*\n")

            # L'utilisateur peut modifier soit les règles de calcul, soit d'optimisation associées au paramètre

            print("Modify rules")
            print("  Compute rules: type C or c")
            print("  Optimization rule: type O or o\n")

            # Saisie du choix de l'utilisateur
            mod_choice = input("Choice: ")

            # Erreur saisie (rien ne se passe)
            if mod_choice not in ["C", "c", "O", "o"]:
                return 1

            print("\n*\n")

            # Choix : modification des règles de calcul
            if mod_choice == "C" or mod_choice == "c":
                print("Compute rules\n")

                new_rules = pro.input_modify_rules(mod_par)
                pro.modify_parameter_tree(mod_par, mod_rules=new_rules)
            # Choix : modification des règles d'optimisation
            else:
                print("Optimization rule\n")

                new_opt = pro.input_modify_optimization(mod_par)
                pro.modify_parameter_tree(mod_par, mod_opt=new_opt)
        # Toute autre saisie
        else:
            return 1

        # Mise à jour de l'arbre
        self.tree.set_pro(pro)

        return 0

    """
    Entrée : aucune
    Sortie : entier
    
    Ajout ou suppression d'un noeud à l'arbre
    Renvoie :
        - 0 ssi tout s'est bien déroulé
        - 1 sinon
    """
    def action_node(self):
        print("\n*\n")

        # 2 actions possibles : ajout et suppression d'un noeud

        print("Node")
        print("  Adding: type A or a")
        print("  Deleting: type D or d\n")

        # Saisie du choix de l'utilisateur
        action = input("Action : ")

        # Choix : ajout d'un noeud à l'arbre
        if action == "A" or action == "a":
            print("\nAdd a node")
            print("  Specify the name")
            print("          the parent(s)")
            print("          the child(ren)\n")

            node_error = Node()

            node = self.tree.input_add_node()

            # Erreur saisie
            if (node == node_error):
                return 1

            # Ajout du noeud
            self.tree.add_node_tree(node)
        # Choix : suppression d'un noeud de l'arbre
        elif action == "D" or action == "d":
            print("\nDelete a node")
            print("  Two deletion modes")
            print("    Removal of the node only")
            print("               the node and the generated sub-tree\n")

            ret = self.tree.input_delete_node()

            # Erreur saisie
            if ret == 1:
                return 1
        # Toute autre saisie
        else:
            return 1

        return 0

    """
    Entrée : aucune
    Sortie : entier
    
    Exécution d'une action sur un paramètre ou un noeud de l'arbre
    Renvoie :
        - 0 ssi tout s'est bien déroulé
        - 1 ssi il y a une erreur
        - 2 ssi l'utilisateur quitte le menu
        - 3 sinon
    """
    def execute_action(self):
        print("\n===============================================================================================\n")

        print("Quit: type Q or q\n")

        print("~\n")

        print("Actions: adding, deleting or modifying\n")

        print("Parameter: enter P or p")
        print("Node: type N or n\n")

        print("~\n")

        # Saisie du choix de l'utilisateur
        choice = input("Choice: ")

        # Action sur un paramètre
        if choice == "P" or choice == "p":
            ret = self.action_parameter()
        # Action sur un noeud
        elif choice == "N" or choice == "n":
            ret = self.action_node()
        # L'utilisateur quitte le menu
        elif choice == "Q" or choice == "q":
            return 2
        # Toute autre saisie
        else:
            return 3

        return ret

    """
    Entrée : aucune
    Sortie : aucune
    
    Modification de l'arbre
    """
    def menu_tree(self):
        ret = 0

        while ret != 2:
            self.tree.print_tree()
            ret = self.execute_action()

            clear()

        # Une fois le menu quitté, l'utilisateur peut sauvegarder l'arbre créé dans un fichier JSON

        save_choice = input("Save the tree? Type Y or y: ")

        # Sauvegarde de l'arbre
        if save_choice == "Y" or save_choice == "y":
            # Saisie du nom du fichier
            name_file = input("Enter the JSON file name: ")

            # Ajout de l'extension .json si elle a été oubliée
            if ".json" not in name_file:
                name_file = name_file + ".json"

            self.tree.from_tree_to_json(name_file)

        clear()

        sys.exit()
