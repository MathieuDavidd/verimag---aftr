"""
Fichier parameters_rules.py

Classe Parameters : paramètres et règles de calcul et d'optimisation de l'arbre

Informations fondatrices de l'arbre : paramètres et règles associées pour effectuer des calculs et optimiser
des scénarios
"""


import sys


# Portes logiques
gates = ["AND", "OR", "NOT", "XOR", "SOR"]

# Paramètres et règles de calcul et d'optimisation valides

valid_parameters = ["Time", "Money", "Damages", "Success probability"]
valid_rules = ["+", "*", "M", "m"]
valid_optimizations = ["M", "m"]


class Parameters:
    """
    Constructeur

    Attributs de la classe :
        - parameters (liste de chaine de caractères) :
            liste des paramètres sur lesquels reposent les calculs (temps, budget pour l'attaquant, dommages
             sur l'infrastructure et probabilité de réussite)
        - rules (dictionnaire) :
            chacune des clés du dictionnaire est une porte logique et la valeur associée est une liste de
            règles de calcul (+, *, M pour maximum ou m pour minimum)
        - optimizations (liste de chaine de caractères) :
            optimisation (maximisation ou minimisation de la valeur) pour chaque paramètre de l'arbre
    """
    def __init__(self):
        self.parameters = []
        self.rules = {"AND": [], "OR": [], "NOT": [], "XOR": [], "SOR": []}
        self.optimizations = []

    """
    Entrée : aucune
    Sortie : liste de chaine de caractères
    
    Getter : renvoie la liste des paramètres de l'arbre
    """
    def get_parameters(self):
        return self.parameters

    """
    Entrée :
        ind (entier) : indice
    Sortie : chaine de caractères
    
    Getter : renvoie le paramètre se trouvant à l'indice ind
    """
    def get_parameter(self, ind):
        return self.parameters[ind]

    """
    Entrée :
        parameter (chaine de caractères) : nom d'un paramètre
    Sortie : chaine de caractères
    
    Getter : renvoie l'indice du paramètre parameter
    """
    def get_index_parameter(self, parameter):
        return self.parameters.index(parameter)

    """
    Entrée : aucune
    Sortie : dictionnaire
    
    Getter : renvoie l'ensemble des règles de calcul associées à chaque porte logique
    """
    def get_rules(self):
        return self.rules

    """
    Entrée :
        gate (chaine de caractères) : porte logique
    Sortie : liste de chaine de caractères
    
    Getter : renvoie la liste des règles de calcul associées à la porte logique gate
    """
    def get_rules_gate(self, gate):
        return self.rules[gate]

    """
    Entrée :
        - gate (chaine de caractères) : porte logique
        - ind (entier) : indice
    Sortie : chaine de caractères
    
    Getter : renvoie la (ind+1)-ième règle de calcul associée à la porte logique gate
    """
    def get_rule_gate_ind(self, gate, ind):
        return self.rules[gate][ind]

    """
    Entrée : aucune
    Sortie : liste de chaine de caractères
    
    Getter : renvoie la liste des règles d'optimisation de l'arbre
    """
    def get_optimizations(self):
        return self.optimizations

    """
    Entrée :
        parameter (chaine de caractères) : nom d'un paramètre
    Sortie : chaine de caractères
    
    Getter : renvoie la règle d'optimisation associée au paramètre parameter
    """
    def get_optimization_par(self, parameter):
        ind_par = self.get_index_parameter(parameter)
        return self.optimizations[ind_par]

    """
    Entrée :
        parameters (chaine de caractères) : paramètres de l'arbre
    Sortie : aucune
    
    Setter : modifie les paramètres de l'arbre
    """
    def set_parameters(self, parameters):
        self.parameters = parameters

    """
    Entrée :
        rules (dictionnaire) : règles de calcul associées à chaque porte logique pour un paramètre
    Sortie : aucune
    
    Setter : modifie les règles de calcul associées à chaque porte logique pour un paramètre
    """
    def set_rules(self, rules):
        self.rules = rules

    """
    Entrée :
        - gate (chaine de caractères) : porte logique
        - rules_gate (liste de chaine de caractères) : nouvelles règles de calcul associées à la porte logique gate
    Sortie : aucune
    
    Setter : modifie les règles de calcul associées à la porte logique gate
    """
    def set_rules_gate(self, gate, rules_gate):
        self.rules[gate] = rules_gate

    """
    Entrée :
        optimizations (chaine de caractères) : règles d'optimisation associées à un paramètre
    Sortie : aucune
    
    Setter : Modifie les règles d'optimisation associées à un paramètre
    """
    def set_optimizations(self, optimizations):
        self.optimizations = optimizations

    """
    Entrée :
        - parameter (chaine de caractères) : nom d'un paramètre
        - optimization (chaine de caractères) : nouvelle règle d'optimisation associée au paramètre parameter
    Sortie : aucune
    
    Setter : modifie la règle d'optimisation associée au paramètre parameter
    """
    def set_optimization_par(self, parameter, optimization):
        ind_par = self.parameters.index(parameter)
        self.optimizations[ind_par] = optimization

    """
    Entrée :
        parameter (chaine de caractères) : nom d'un paramètre
    Sortie : booléen
    
    Renvoie vrai ssi le paramètre parameter existe
    """
    def parameter_exists(self, parameter):
        return (parameter in self.parameters)

    """
    Entrée :
        parameter (chaine de caractères) : nom d'un paramètre
    Sortie : booléen
    
    Renvoie vrai ssi si le paramètre parameter est valide (méthode utile pour la saisie utilisateur)
    """
    def parameter_is_valid(self, parameter):
        return (parameter in valid_parameters)

    """
    Entrée :
        rule (chaine de caractères) : règle de calcul
    Sortie : booléen
    
    Renvoie vrai ssi si la règle de calcul rule est valide (méthode utile pour la saisie utilisateur)
    """
    def rule_is_valid(self, rule):
        return (rule in valid_rules)

    """
    Entrée :
        optimization (chaine de caractères) : règle d'opitmisation
    Sortie : booléen
    
    Renvoie vrai ssi si la règle d'optimisation optimization est valide (méthode utile pour la saisie utilisateur)
    """
    def optimization_is_valid(self, optimization):
        return (optimization in valid_optimizations)

    """
    Entrée :
        parameter (chaine de caractères) : nom d'un paramètre
    Sortie : aucune
    
    Ajoute parameter à la liste des paramètres
    """
    def add_parameter(self, parameter):
        self.parameters.append(parameter)

    """
    Entrée :
        parameter (chaine de caractères) : nom d'un paramètre
    Sortie : aucune
    
    Supprime parameter de la liste des paramètres
    """
    def delete_parameter(self, parameter):
        self.parameters.remove(parameter)

    """
    Entrée :
        - gate (chaine de caractères) : porte logique
        - rule (chaine de caractères) : règle de calcul associée à la porte logique gate
    Sortie : aucune
    
    Ajoute à l'arbre la règle de calcul rule associée à la porte logique gate
    """
    def add_rule_gate(self, gate, rule):
        # Règles de calcul associée à la porte logique gate
        rules_gate = self.get_rules_gate(gate)
        # Ajout de la règle rule
        rules_gate.append(rule)

        self.set_rules_gate(gate, rules_gate)

    """
    Entrée :
        rules (dictionnaire) : chaque clé est une porte logique, et la valeur, la règle de calcul associée
    Sortie : aucune
    
    Ajoute à l'arbre les règles de calcul d'un paramètre associées à chaque porte logique de rules
    """
    def add_rules(self, rules):
        for gate in rules:
            rule = rules[gate]
            self.add_rule_gate(gate, rule)

    """
    Entrée :
        ind_par (entier) : indicie d'un paramètre
    Sortie : aucune
    
    Supprime de l'arbre les règles de calculs du paramètre d'indice ind_par
    """
    def delete_rules(self, ind_par):
        # Règles de calcul associées à toutes les portes logiques
        for gate in gates:
            rules_gate = self.get_rules_gate(gate)

            if rules_gate != []:
                # Suppression de la règle de calcul à l'indice ind_par
                rules_gate.pop(ind_par)
                self.set_rules_gate(gate, rules_gate)

    """
    Entrée :
        optimization (chaine de caractères) : règle d'optimisation
    Sortie : aucune
    
    Ajoute à l'arbre la règle d'optimisation optimization à la liste des règles d'optimisation
    """
    def add_optimization(self, optimization):
        self.optimizations.append(optimization)

    """
    Entrée :
        ind_par (entier) : indice d'un paramètre
    Sortie : aucune
    
    Supprime de l'arbre la règle d'optimisation du paramètre d'indice ind_par
    """
    def delete_optimization(self, ind_par):
        self.optimizations.pop(ind_par)

    """
    Entrée :
        - parameter (chaine de caractères) : nom d'un paramètre
        - rules (dictionnaire) : les clés sont les portes logiques et chaque valeur, une règle de calcul
        - optimization (chaine de caractères) : règle d'optimisation
    Sortie : aucune
    
    Ajoute à l'arbre le paramètre parameter et les règles de calcul et d'optimisation associées (respectivement
    stockées dans rules et optimization)
    """
    def add_parameter_tree(self, parameter, rules, optimization):
        # Ajout du paramètre
        self.add_parameter(parameter)
        # Ajout de ses règles de calcul
        self.add_rules(rules)
        # Ajout de sa règle d'optimisation
        self.add_optimization(optimization)

    """
    Entrée :
        parameter (chaine de caractères) : nom d'un paramètre
    Sortie : entier
    
    Supprime de l'arbre le paramètre parameter et les règles de calcul et d'optimisation associées et renvoie
    l'indice du paramètre supprimé
    """
    def delete_parameter_tree(self, parameter):
        ind_par = self.get_index_parameter(parameter)

        # Suppression du paramètre
        self.delete_parameter(parameter)
        # Suppression de ses règles de calcul
        self.delete_rules(ind_par)
        # Suppression de sa règle d'optimisation
        self.delete_optimization(ind_par)

        return ind_par

    """
    Entrée :
        - parameter (chaine de caractères) : nom d'un paramètre
        - mod_rules (dictionnaire, par défaut vide) : les clés sont les portes logiques et chaque valeur, une nouvelle
        règle de calcul
        - mod_opt (chaine de caractères, par défaut vide) : nouvelle règle d'optimisation
    Sortie : aucune
    
    Modifie le paramètre parameter (règles de calcul ou d'optimisation)
    """
    def modify_parameter_tree(self, parameter, mod_rules={}, mod_opt=""):
        # Argument mod_rules non vide : modification des règles de calcul du paramètre
        if mod_rules != {}:
            ind_par = self.get_index_parameter(parameter)

            for gate in mod_rules:
                rules_gate = self.get_rules_gate(gate)

                rule = mod_rules[gate]
                rules_gate[ind_par] = rule

                self.set_rules_gate(gate, rules_gate)
        # Argument mod_opt non vide : modification des règles d'optimisation du paramètre
        if mod_opt != "":
            self.set_optimization_par(parameter, mod_opt)

    """
    Entrée : aucune
    Sortie : chaine de caractères
    
    Saisie et renvoi d'une règle de calcul associée à un paramètre
    """
    def input_rule_paramater(self):
        # Saisie d'une règle de calcul
        rule = input("Choice: ")

        # L'utilisateur doit ressasir une règle de calcul tant qu'elle n'est pas valide
        while not (self.rule_is_valid(rule)):
            print("\nError input: '", rule, "' is not a valid rule", sep="")
            rule = input("Choice: ")

        return rule

    """
    Entrée : aucune
    Sortie : chaine de caractères
    
    Saisie et renvoi d'une règle d'optimisation associée à un paramètre
    """
    def input_optimization_paramater(self):
        # Saisie d'une règle d'optimisation
        optimization = input("Choice: ")

        # L'utilisateur doit ressaisir une règle d'optimisation tant qu'elle n'est pas valide
        while not (self.optimization_is_valid(optimization)):
            print("\nError input: '", optimization, "' is not a valid rule", sep="")
            optimization = input("Choice: ")

        return optimization

    """
    Entrée :
        gate (chaine de caractères) : porte logique
    Sortie : aucune
    
    Saisie des règles de calcul associées à la porte logique gate pour tous les paramètres de l'arbre
    """
    def input_rule_gate(self, gate):
        print("Gate", gate, end="\n\n")

        for parameter in self.parameters:
            print("Parameter:", parameter)

            # Saisie de la règle de calcul pour le paramètre parameter
            rule = self.input_rule_paramater()
            self.add_rule_gate(gate, rule)

            print()

        if gate != "SOR":
            print("-------\n")

    """
    Entrée : aucune
    Sortie : aucune
    
    Saisie des règles de calcul associées à chacune des portes logiques pour tous les paramètres de l'arbre
    """
    def input_rules(self):
        # Porte logique AND
        self.input_rule_gate("AND")
        # Porte logique OR
        self.input_rule_gate("OR")
        # Porte logique NOT
        self.input_rule_gate("NOT")
        # Porte logique XOR
        self.input_rule_gate("XOR")
        # Porte logique SOR
        self.input_rule_gate("SOR")

    """
    Entrée : aucune
    Sortie : aucune
    
    Saisie des règles d'optimisation pour tous les paramètres de l'arbre
    """
    def input_optimization(self):
        for parameter in self.parameters:
            print("Parameter:", parameter)

            # Saisie de la règle d'optimisation pour le paramètre parameter
            optimization = self.input_optimization_paramater()
            self.add_optimization(optimization)

            print()

    """
    Entrée : aucune
    Sortie : tuple
    
    Saisie pour l'ajout d'un paramètre
    Renvoie le couple (règles de calcul, règle d'optimisation)
    """
    def input_add_parameter(self):
        # Règles de calcul

        print("Compute rules\n")

        rules = {}

        for gate in gates:
            print("Gate", gate)

            # Saisie de la règle de calcul associée à la porte logique gate pour le paramètre à ajouter
            rule = self.input_rule_paramater()
            # Nouvelle clé : nouvelle valeur
            rules[gate] = rule

            if gate != "SOR":
                print("\n---------\n")

        print("\n*\n")

        # Règle d'optimisation

        print("Optimization rule")

        # Saisie de la règle d'optimisation pour le paramètre à ajouter
        optimization = self.input_optimization_paramater()

        return (rules, optimization)

    """
    Entrée :
        parameter (chaine de caractères) : nom d'un paramètre
    Sortie : dictionnaire

    Saisie pour la modification des règles de calcul d'un paramètre
    Renvoie :
        - un dictionnaire vide ssi l'utilisateur choisit de ne modifier aucune règle de calcul
        - le dictionnaire dont les clés sont les portes logiques auxquelles sont associées de nouvelles règles
        de calcul sinon
    """
    def input_modify_rules(self, parameter):
        ind_par = self.get_index_parameter(parameter)

        new_rules = {}

        for gate in gates:
            print("Gate", gate, end="\n\n")

            rules_gate = self.get_rules_gate(gate)
            rule = rules_gate[ind_par]

            print("Actual compute rule:", rule)
            choice = input("Modify this rule? Type Y or y: ")

            # Modification de la règle de calcul
            if choice == "Y" or choice == "y":
                print()

                # Saisie d'une nouvelle règle de calcul
                new_rule = input("New compute rule: ")

                # L'utilisateur doit ressaisir une règle de calcul tant qu'elle n'est pas valide
                while not (self.rule_is_valid(new_rule)):
                    print("\nError input: '", new_rule, "' is not a valid rule", sep="")
                    new_rule = input("New compute rule: ")

                # Nouvelle clé : nouvelle valeur
                new_rules[gate] = new_rule

            print("\n-----------------\n")

        return new_rules

    """
    Entrée :
        parameter (chaine de caractères) : nom d'un paramètre
    Sortie : chaine de caractères

    Saisie pour la modification de la règle d'optimisation d'un paramètre
    Renvoie :
        - une chaine de caractères vide ssi l'utilisateur choisit de ne pas modifier la règle d'optimisation
        - la nouvelle règle d'optimisation sinon
    """
    def input_modify_optimization(self, parameter):
        opt_par = self.get_optimization_par(parameter)

        new_opt = ""

        print("Actual optimization rule:", opt_par)
        choice = input("Modify this rule? Type Y or y: ")

        # Modification de la règle d'optimisation
        if choice == "Y" or choice == "y":
            print()

            # Saisie d'une nouvelle règle d'optimisation
            new_opt = input("New optimization rule: ")

            # Renvoi d'une chaine de caractères vide si l'utilisateur saisit une règle d'optimisation invalide
            if not (self.optimization_is_valid(new_opt)):
                return ""

        return new_opt

    """
    Entrée : aucune
    Sortie : aucune
    
    Saisie pour initialiser les paramètres et les règles de calcul et d'optimisation de l'arbre
    """
    def init_parameters_rules(self):
        print("COMPLETION OF THE TREE PARAMETERS AND RULES")
        print("===========================================\n")

        #################################
        # Initialisation des paramètres #
        #################################

        print("PARAMETERS")
        print("Type Y or y to choose a parameter\n")

        print("*********************************\n")

        # Choix parmi 4 paramètres : 1 au minimum, 4 au maximum

        for i in range(4):
            # Choix 1 : temps
            if i == 0:
                par_choice = input("Time: ")
                parameter = "Time"
            # Choix 2 : coût
            elif i == 1:
                par_choice = input("Money: ")
                parameter = "Money"
            # Choix : dommages sur l'infrastructure
            elif i == 2:
                par_choice = input("Damages: ")
                parameter = "Damages"
            # Choix : probabilité de réussite du scénario
            else:
                par_choice = input("Success probability: ")
                parameter = "Success probability"

            # Ajout d'un paramètre sélectionné
            if par_choice == "Y" or par_choice == "y":
                self.add_parameter(parameter)

        # Erreur si au aucun paramètre n'a été sélectionné
        if len(self.parameters) == 0:
            print("\nError \"parameters_rules.py\"")
            print("init_parameters_rules (class PR): no parameter initialized")

            sys.exit()

        print("\n*\n")

        #######################################
        # Initialisation des règles de calcul #
        #######################################

        print("RULES\n")

        print("Choose the compute rule for each logical gate and parameter")
        print("Choices among the sum (type +), the product (type *), the maximum (type M) and the minimum (type m)\n")

        print("***************************************************************************************************\n")

        self.input_rules()

        print("*\n")

        ############################################
        # Initialisation des règles d'optimisation #
        ############################################

        print("OPTIMIZATION\n")

        print("Choose the optimization rule for each parameter to specify a scenario")
        print("Choices among the maximization (type M) and the minimization (type m)\n")

        print("*********************************************************************\n")

        self.input_optimization()

    """
    Entrée : aucune
    Sortie : aucune
    
    Affichage des paramètres de l'arbre
    """
    def print_parameters(self):
        for parameter in self.parameters:
            print(parameter, end=" ")

    """
    Entrée :
        gate (chaine de caractères) : porte logique
    Sortie : aucune
    
    Affichage des règles de calcul associées à la porte logique gate pour tous les paramètres de l'arbre
    """
    def print_rules(self, gate):
        for i in range(len(self.parameters)):
            parameter = self.get_parameter(i)
            print("    ", parameter, ": ", end="", sep="")

            rule = self.get_rule_gate_ind(gate, i)

            if rule == "+":
                print("sum")
            elif rule == "*":
                print("product")
            elif rule == "M":
                print("maximum")
            else:
                print("minimum")

    """
    Entrée : aucune
    Sortie : aucune
    
    Affichage des règles d'optimisation pour tous les paramètres de l'arbre
    """
    def print_optimization(self):
        for i in range(len(self.parameters)):
            parameter = self.get_parameter(i)
            optimization = self.get_optimization_par(parameter)

            print(parameter, ": ", sep="", end="")

            if (optimization == "M"):
                print("maximum")
            else:
                print("minimum")

    """
    Entrée : aucune
    Sortie : dictionnaire
    
    Convertit l'ensemble des paramètres et des règles de calcul et d'optimisation en un dictionnaire
    Le dictionnaire possède 3 clés : "Parameters" pour les paramètres de l'arbre, "Compute rules" et
    "Optimization rules" pour les règles de calcul et d'optimisation
    """
    def from_pro_to_dict(self):
        dict = {}

        # Clé pour les paramètres
        parameters = self.get_parameters()
        dict["Parameters"] = parameters

        # Clé pour les règles de calcul
        rules = self.get_rules()
        dict["Compute rules"] = rules

        # Clé pour les règles d'optimisation
        optimizations = self.get_optimizations()
        dict["Optimization rules"] = optimizations

        return dict

    """
    Entrée :
        dict (dictionnaire) : informations relatives aux paramètres et des règles de calcul et d'optimisation
    Sortie : aucune
    
    Créé l'ensemble des paramètres et des règles de calcul et d'optimisation de l'arbre à partir du dictionnaire dict
    """
    def from_dict_to_pro(self, dict):
        # Paramètres
        parameters = dict["Parameters"]
        self.set_parameters(parameters)

        # Règles de calcul
        rules = dict["Compute rules"]
        self.set_rules(rules)

        # Règles d'optimisation
        optimizations = dict["Optimization rules"]
        self.set_optimizations(optimizations)
