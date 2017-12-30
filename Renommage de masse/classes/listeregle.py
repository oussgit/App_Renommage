from regle import *


class ListeRegle:

    def __init__(self):
        regles = []
        self.regles = regles

    def get(self):
        return self.regles

    @property
    def regles(self):
        return self._regles

    @regles.setter
    def regles(self, value):
        """
        setter of regles
        :param value:
        :return:
        """
        self._regles = value

    def sauvegarder(self, regle):
        """
        Permet de sauvegarder les regles dans un fichier txt regles.ini
        :param regle:
        :return:
        """
        fichier = open("./files/regles.ini", "a")
        saved = str(regle).replace(" ", ";")
        print(saved, file=fichier)
        fichier.close()

    def charger(self):
        """
        Permet de charger les reglès extraites depuis le fichier txt regles.ini
        :return:
        """
        fichier = open("./files/regles.ini", "r")
        mon_fichier = fichier.readlines()   #On lit les lignes du fichier une a une
        for ligne in mon_fichier:           #on affecte, une par une, chaque valeur du fichier à ligne
            t = ligne.replace("\n", "").split(";")  #on créer une liste T qui prend chaque caractéristique de la regle

            self.regles.append(Regle(t[0], t[1], t[2], t[3], t[4], t[5], t[6]))
            #on ajoute chaque regle à regles construisant une "liste de regles"
            fichier.close()

    def __str__(self):
        liste_regle = ""
        for rule in self.regles:
            liste_regle = liste_regle + str(rule) + "\n"
        return liste_regle




