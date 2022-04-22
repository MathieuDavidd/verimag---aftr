#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:48:44 2022

@author: engelsl
"""

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
        #print("on est dans le if")
        DataFrame = tri_croissant(col, DataFrame)
    else : 
        #print("on est dans le else")
        DataFrame = tri_decroissant(col, DataFrame)
        #print(DataFrame)
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
        # print(Som)
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
    #print(DataFrame)
    i = 0
    for col in para :
        DataFrame[col] = DataFrame[col]*poids[i]
        i = i+1
    #print(DataFrame)
    return 

def tri_min_max(DataFrame, para, poids, minmax) :
    somme = []
    Normalise(DataFrame)
    #print(DataFrame)
    ajouter_poids_min_max(DataFrame, para, poids, minmax)
    for i in DataFrame.index :
        Som = 0
        for col in para :
                Som = Som + DataFrame.loc[i, col]
        Som = round(Som, 2)
        # print(Som)
        somme.append(Som)
    add_col('SOMME', DataFrame, somme)
    DataFrame = tri_croissant('SOMME', DataFrame)
    return DataFrame
   
