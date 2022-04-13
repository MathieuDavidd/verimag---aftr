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

def OperGate(self, IGate, IParam):
        Param = self.__param[IParam]  # Param c'est le paramètre cherché
        Oper = Param.GetRuleNo(IGate)  # Oper (str) l'opération associé à la gate d'indice IGate
        return (Oper)
        
#Traitement : A changer
#Entrées : Le chemin actuellement suivi(vide au depart), la liste de tous les chemins parcourus (vide au depart)
#Le Noeud actuellement en cours de traitement, l'expression symbolique du chemin actuellement traité associée
#Au parametre d'indice Iparam dans la liste de tous les parametres LParam, ainsi que
#La liste des expressions associée a chaque chemin.
#Sortie : La liste des chemins tous les chemins possible ainsi que la liste de chaque expression symbolique 
#Associée a chaque chemin




def TrouveChemins2a(self, NCourant):
        if (NCourant.getGate() == 'None - Leaf'):  # Ncourant est une feuille de l'arbre
            return [NCourant.getId()]
        else:  # On a donc affaire à une porte
            if (NCourant.getGate() == 'AND'):
                return [NCourant.getId(), [self.TrouveChemins2a(child) for child in self.getChildNode(NCourant)]]
            if (NCourant.getGate() == 'OR'):
                return [NCourant.getId(), [self.TrouveChemins2a(child) for child in self.getChildNode(NCourant)]]

#Il faut changer la porte  OR pour dupliquer les listes n fois où n est le nombre de fils de la porte OR

