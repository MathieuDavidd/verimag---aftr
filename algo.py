"""Algo de parcours arbre
    Parcours de l'arbre
    Fonction traitement([CheminJusqu'auNoeud],LeNoeud,)
                         Fait le calcul des Paramètres du noeud courant
                         e.g. Pour une porte AND Somme Des Traitement des fils
                         Et donc Appel récursif sur les fils
                        Cas terminal feuille
                            Ajout du chemin dans la liste des chemins
                            Ajout des paramètres dans la liste des paramètres
        Appel à traitement sur le noeud zéro
        """
        
        
import numpy as np

#Oper Gate prends en compte les differents parametres de l'arbres, l'indice du
#paramètre recherché ainsi que l'indice du type de porte associé et renvoie
#le string de l'opération e.g. "+", "_min_" etc cf Paramètre

def OperGate(arbre, IGate, IParam):
        Param = arbre.get__param()  # Param c'est le paramètre cherché
        Oper = Param.GetRuleNo(IGate)  # Oper (str) l'opération associé à la gate d'indice IGate
        return (Oper)
        
#TrouveChemins : 
#Entrées : Un arbre
#Sortie : Une liste 
#Specification : TrouveChemins prend un arbre et renvoie la liste des id de tous les chemins possibles a parcourir,
#On part du principe qu'il n'y a que des portes AND ou SAND (cf fonctions precedemment utilisées pour split les OR)

def TrouveChemins(arbre, IParam, NCourant = Noeud(-1,test,kek,[],[]), ListRet = np.array([])):
	if (NCourant.getId() == -1):
	    NCourant = arbre.getRoot() 
        if (NCourant.getGate() == 'None - Leaf'):  # Ncourant est une feuille de l'arbre
            return ([[NCourant.getId()], str(NCourant.getParamValueNo(IParam))])
        else:  # On a donc affaire à une porte
	    for child in arbre.getChildNode(NCourant):
	        if (child == arbre.getChildNode(NCourant)[-1]):
         	    ListeRet = np.array([arbre.TrouveChemins(arbre,IParam,NCourant = child)]) + np.array([NCourant.getId(), ')'])		    
         	elif (child == arbre.getChildNode(NCourant)[0]):
	            ListeRet = np.array([arbre.TrouveChemins(arbre,IParam,NCourant = child)]) + np.array([NCourant.getId(), '(' + OperGate(arbre,0,IParam)])
		else :
		    ListeRet = np.array([arbre.TrouveChemins(arbre,IParam,NCourant = child)]) + np.array([NCourant.getId(), OperGate(arbre,0,IParam)])
            return ListRet


