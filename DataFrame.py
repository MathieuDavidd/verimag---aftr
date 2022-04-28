"""
Fichier DataFrame.py

Création d'un dataframe pour stocker et traiter les données renvoyées par l'algorithme de deparcours de l'arbre
"""

import pandas as pd
import numpy as np
from tree import Tree

# Création d'un dataframe vide
"""
Entrée : rien
Sortie : Un dataframe vide (module pandas)
"""
def CreateDataFrameEmpty():
    ListeParametre = ['Chemin']
    return pd.DataFrame(columns = ListeParametre)

# Ajouter les paramètres utilisés dans l'algo
"""
Entrée : Un dataframe (module pandas)
Sortie : Un dataframe avec en colonne les paramètres de l'arbre
"""
def AppendParametre(df,t):
    pro = t.get_pro()
    Lpara = pro.get_parameters()
    for i in range(len(Lpara)):
        df[Lpara[i]] = ''
    df = df.fillna(0)
    return df

# Ajouter les paramètres utilisés dans l'algo
"""
Entrée : Un dataframe (module pandas)
Sortie : Un dataframe avec en colonne les paramètres de l'arbre
"""
def AppendParametreTest(df,para):
    for i in range(len(para)):
        df[para[i]] = ''
    df = df.fillna(0)
    return df

# Ajouter une ligne de donnée (cad le résultat d'un parcours de l'algo)
"""
Entrée : Un dataframe (module pandas) avec en colonne les parametres utilisés dans l'algo
Sortie : Un dataframe avec les données
"""
def AppendData(df, ListRet):
    for i in range(0, len(ListRet[0])):
        data = []
        data.append(str(ListRet[0][i]))
        for j in range(0, len(ListRet[1][i])):
            data.append(ListRet[1][i][j])
        df.loc[i] = data

    return df

############################### DATA TABLE ####################################


###############################################################################
# IMPORT DES BILBLIOTHEQUES
import pandas as pd
import numpy as np
###############################################################################

######################### AJOUT COLONNE ET VALEURS ############################
# Ajoute une colonnen et toute les valeurs qui lui sont attribué

def add_col (Colname, DataFrame, values) :
    DataFrame.insert(len(DataFrame.columns), Colname, values, False)
    return

#################### TRI CROISSANT DECROISSANT DU TABLEAU #####################

# On tri selon une colonne du tableau
def tri_croissant (col, DataFrame) :
    # On trie les valeurs par ordre croissant selon une colonne
    DataFrame = DataFrame.sort_values(by = col)
    return DataFrame

def tri_decroissant (col, DataFrame) :
    # On trie les valeurs par ordre decroissant selon une colonne
    DataFrame = DataFrame.sort_values(by = col, ascending = False)
    return DataFrame



################### RENVOIE LA TRACE LA PLUS OPTIMISE #########################

def trace_opti (col, DataFrame, croissant) :
    if croissant == True :
        DataFrame = tri_croissant(col, DataFrame)
    else :
        DataFrame = tri_decroissant(col, DataFrame)
    # Renvoie la valeur la plus optimisé pour le pramètre entrée
    DataFrame.reset_index(inplace=True, drop=False)
    return DataFrame.loc[0, col]



######################### NORMALISATION DES VALEURS ###########################
# On a choisi de normmaliser nos valeurs pour que chaque paramètre entre 0 et 1
# On a fait ce choix car on ne voulais pas que les valeurs d'une colonne aient plus
# d'impact que les valeurs d'une autre colonne.
# On a donc normaliser les valeurs entre 0 et 1, 1 etant la valeur maximum des valeurs d'une colonne
################################################################################
def Normalise(DataFrame) :
    for col in DataFrame.columns :
        if col != 'Chemin':
            value = trace_opti(col, DataFrame, False)
            for i in DataFrame.index :
                DataFrame.loc[i, col] =  DataFrame.loc[i, col] / value
    return


####################### TRI SELON PLUSIEURS COLONNES  #########################
# Paramètre : para : liste de colonnes selon lequelles on tri
#           : pids : Liste de poids appliquer au colonne (pourcentage)
# Les deux liste sont dans l'odre Poids[0] = para[0]
# On tri dans l'ordre croissant par defaut (recherche du min)


def ajouter_poids(DataFrame, para, poids) :
    i = 0
    for col in para :
        DataFrame[col] = DataFrame[col]*poids[i]
        i = i+1
    return

def tri_plusieurCol(DataFrame, para, poids) :
    somme = []
    Normalise(DataFrame)
    ajouter_poids(DataFrame, para, poids)
    for i in DataFrame.index :
        Som = 0
        for col in para :
            Som = Som + DataFrame.loc[i, col]
        Som = round(Som, 2)
        somme.append(Som)
    add_col('SOMME', DataFrame, somme)
    DataFrame = tri_croissant('SOMME', DataFrame)
    return DataFrame



#################### TRI MIN MAX SELON PLUSIEURS COLONNES #####################
# Paramètre : para : liste de colonnes selon lequelles on tri
#           : pids : Liste de poids appliquer au colonne (pourcentage)
#           : minmaxc : Liste de l'odre
# Les deux liste sont dans l'odre Poids[0] = para[0]

def ajouter_poids_min_max(DataFrame, para, poids, minmax) :
    i = 0
    for col in para:
        if minmax[i] == 'Max' :
            DataFrame[col] = 1 - DataFrame[col]
        i = i+1
    i = 0
    for col in para :
        if col != "Chemin":
            DataFrame[col] = DataFrame[col]*poids[i]
            i = i+1
    return

def tri_min_max(DataFrame, para, poids, minmax) :
    somme = []
    Normalise(DataFrame)
    ajouter_poids_min_max(DataFrame, para, poids, minmax)
    for i in DataFrame.index :
        Som = 0
        for col in para :
                Som = Som + DataFrame.loc[i, col]
        Som = round(Som, 2)
        somme.append(Som)
    add_col('SOMME', DataFrame, somme)
    DataFrame = tri_croissant('SOMME', DataFrame)
    return DataFrame

############################## TRI VIA LE MENU ##############################
# Paramètre : t : arbre
#           : paths : tous les chemins possibles
#           : expr_simpl : expressions symboliques simplifiées

def sort_dataframe_menu(t, paths, expr_simpl):
    # restructuration des donnees qui sortent de l'algo
    data = [paths, expr_simpl]
    # creation dataframe vide
    df = CreateDataFrameEmpty()
    # ajout des parametre de l'arbre
    df = AppendParametre(df, t)
    # Ajout des donnees
    df = AppendData(df, data)

    newsort = "oui"
    while newsort == "oui":
        print("*\n")

        print("Dataframe\n")

        # Affichage du dataframe
        print(df)

        # Choix du tri

        # L'utilisateur sélectionne son tri
        print()
        tri = input("Quel type de tri voulez-vous utiliser (croissant, decroissant, min_max) : ")

        # Tri choisi par l'utilisateur
        if tri == "croissant" or tri == "decroissant":
            var = input("Selon quel paramètre voulez-vous effectuer votre tri : ")
            # Tri croissant
            if tri == "croissant":
                df1 = tri_croissant(var, df)
                print(df1)
            # Tri decroissant
            else:
                df2 = tri_decroissant(var, df)
                print(df2)
        elif tri == "min_max":
            para = []
            minmax = []
            poids = []
            var = "\0"
            pondere = input("Voulez-vous pondérer les paramètres (oui, non) : ")
            while var != "stop":
                print()

                var = input(
                    "Selon quel paramètre voulez-vous effectuer votre tri (écrivez 'stop' si vous avez déjà sélectionné vos variables) : ")
                if var != "stop":
                    para.append(var)
                    m = input("Voulez-vous minimiser ou maximiser ce paramètre (Min, Max) : ")
                    minmax.append(m)
                    if pondere == "oui":
                        p = input("Quelle pondération voulez-vous appliquez à cette variable (en %) : ")
                        poids.append(float(p))
            if pondere == "non":
                poids = np.ones(len(para))

            # Tri Min Max
            df4 = tri_min_max(df, para, poids, minmax)
            print(df4)

        # Effectuer un nouveau tri
        newsort = input("Voulez-vous effectuer un nouveau tri (oui, non) : ")
     

    print("\n*\n")

