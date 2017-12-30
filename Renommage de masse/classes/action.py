from regle import *
import re
import os

class Action:

    def __init__(self, regle, nom_du_rep):
        """
        Constructeur d'un objet Action
        :param regle: attends un objet Regle en entrée
        :param nom_du_rep: attends un chemin en entrée
        """
        self._nom_du_rep = nom_du_rep
        self._regle = regle

    #Décorateur getters/setters
    @property
    def nom_du_rep(self):
        """
        getter of nom_du_rep
        :return:
        """
        return self._nom_du_rep

    @nom_du_rep.setter
    def nom_du_rep(self, value):
        """
        setter of nom_du_rep
        :param value:
        :return:
        """
        self.nom_du_rep = value

    @property
    def regle(self):
        """
        getter of regle
        :return:
        """
        return self._regle

    @regle.setter
    def regle(self, value):
        """
        setter of regle
        :param value:
        :return:
        """
        self._regle = value

    def __str__(self):
        """
        retorune une chaine de charactère composée des variables de l'objet
        :return:
        """
        return "{} {}".format(self.nom_du_rep, self.regle)

    def simulate(self):
        nom_original = []
        nom_modifie = []                           #On initialise 2 listes vides servant à stocker
        regle = self.regle                          #on place self.regle dans regle
        chf = str(regle.apartirde)                  #récupère l'ammorce initiale
        if regle.extension == "":
            for element in os.listdir(self.nom_du_rep):     #on parcours le directory au chemin "nom_du_rep"
                nom_original.append(element)                #On stock le noms des fichier dans la liste nom_original

                nom_complet = element.split(".")            #On récupère le nom complet du fichier qu'on split au point
                extension = nom_complet[1]                  #on stock le nom de l'extension dans la variable extension
                if regle.nom_fichier != "":
                    nom = regle.nom_fichier
                else:                               #permet de remplacer ou nom par nom_fichier en fonctions des options
                    nom = nom_complet[0]
                if regle.amorce == "Aucune":            #Instructions si il n'y a pas d'ammorce
                    nom_modifie.append(regle.prefixe+nom+regle.postfixe+"."+extension)     #population de la liste "nom_modifier"


                else:
                    if regle.amorce == "Chiffres":
                        regle.apartirde = int(regle.apartirde)
                        nom_modifie.append(str(regle.apartirde) + regle.prefixe + nom+regle.postfixe + "." + extension)
                        regle.apartirde += 1            #instructions si il y'a une ammorce (CHiffre ou lettre)
                    elif regle.amorce == "Lettres":
                        nom_modifie.append(chf + regle.prefixe + nom + regle.postfixe + "." + extension)
                        chf = inc_char(chf)             #fais appel à la fonction "inc_char" qui permet d'incrementer lettres
        else:
            for element in os.listdir(self.nom_du_rep):
                bool = False
                bool2 = False
                nom_original.append(element)
                nom_complet = element.split(".")
                extension = nom_complet[1]
                if regle.nom_fichier != "":
                    nom = regle.nom_fichier
                else:                               #permet de remplacer ou nom par nom_fichier en fonctions des options
                    nom = nom_complet[0]
                for i in regle.extension.split(","):
                    if ("."+extension) == i:    #ici on verifie que l'extension match avec le filtre avant de renommer
                        bool2 = True            #Previens que l'extension à bien matché avec AU MOINS une des extensions spécifiées
                        if regle.amorce == "Aucune":
                            nom_modifie.append(regle.prefixe+nom+regle.postfixe+"."+extension)
                        else:
                            if regle.amorce == "Chiffres":
                                regle.apartirde = int(regle.apartirde)
                                nom_modifie.append(str(regle.apartirde) + regle.prefixe + nom + regle.postfixe + "."+ extension)
                                regle.apartirde += 1
                            elif regle.amorce == "Lettres":
                                nom_modifie.append(chf + regle.prefixe + nom + regle.postfixe + "." + extension)
                                chf = inc_char(chf)
                    else:
                        bool = True             #Previens que le fichier est non éligible à la modification
                if bool == True and bool2 == False:             #Si le fichier est non eligible à la modification &
                    nom_original.remove(element)                #qu'il ne l'a pas été pour aucune de la liste alors on supprime
        return nom_original, nom_modifie      #Retourne un tuple composé d'une liste des noms avant modif et une après


def inc_char(text, chlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """
    Permet l'incrémentation d'une variable de type string
    :param text: La lettre à incrémenter
    :param chlist: spécifie les caractéristique de la lettre (Majuscule ou miniscule)
    :return:
    """
    chlist = ''.join(sorted(set(str(chlist))))
    chlen = len(chlist)
    if not chlen:
        return ''
    text = str(text)
    #Remplace tous les charactères sauf chlist
    text = re.sub('[^' + chlist + ']', '', text)
    if not len(text):
        return chlist[0]
    #Incrementation
    inc = ''
    over = False
    for i in range(1, len(text)+1):
        lchar = text[-i]
        pos = chlist.find(lchar) + 1
        if pos < chlen:
            inc = chlist[pos] + inc
            over = False
            break
        else:
            inc = chlist[0] + inc
            over = True
    if over:
        inc += chlist[0]
    result = text[0:-len(inc)] + inc
    return result
