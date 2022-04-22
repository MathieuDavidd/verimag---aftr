""" Création d'un dataframe pour stocker les données renvoyées par l'algo deparcours de l'arbre
    CreateDataframe(donnees de lalgo) -> renvoie un tableau qui pour chaque chemin associe une expression symbolique par parametre
    """
    
import pandas as pd
import numpy as np

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
    for i in range(1, len(Lpara)):
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
        data.append(ListRet[0][i][0])
        for j in range(0, len(ListRet[1][i])):
            data.append(ListRet[1][i][j])
        df.loc[i] = data
    return df



