

class Regle:

    def __init__(self, nom_regle, amorce, apartirde, prefixe, nom_fichier, postfixe, extension):
        self._nom_regle = nom_regle
        self._amorce = amorce
        self._apartirde = apartirde
        self._prefixe = prefixe
        self._nom_fichier = nom_fichier
        self._postfixe = postfixe
        self._extension = extension

    @property
    def nom_regle(self):
        """
        getter of nom_regle
        :return:
        """
        return self._nom_regle

    @nom_regle.setter
    def nom_regle(self, value):
        """
        setter of nom_regle
        :param value:
        :return:
        """
        self._nom_regle = value

    @property
    def amorce(self):
        """
        property of amorce
        :return:
        """
        return self._amorce

    @amorce.setter
    def amorce(self, value):
        """
        setter of amorce
        :param value:
        :return:
        """
        self._amorce = value

    @property
    def apartirde(self):
        """
        property of apartirde
        :return:
        """
        return self._apartirde

    @apartirde.setter
    def apartirde(self, value):
        """
        setter of apartirde
        :param value:
        :return:
        """
        self._apartirde = value

    @property
    def prefixe(self):
        """
        property of prefixe
        :return:
        """
        return self._prefixe

    @prefixe.setter
    def prefixe(self, value):
        """
        setter of prefixe
        :param value:
        :return:
        """
        self._prefixe = value

    @property
    def nom_fichier(self):
        """
        getter of nomfichier
        :return:
        """
        return self._nom_fichier

    @nom_fichier.setter
    def nom_fichier(self, value):
        """
        setter of nom_fichier
        :param value:
        :return:
        """
        self._nom_fichier = value

    @property
    def postfixe(self):
        """
        getter of postfixe
        :return:
        """
        return self._postfixe

    @postfixe.setter
    def postfixe(self, value):
        """
        setter of postfixe
        :param value:
        :return:
        """
        self._postfixe = value

    @property
    def extension(self):
        """
        getter of extension
        :return:
        """
        return self._extension

    @extension.setter
    def extension(self, value):
        """
        setter of extension
        :param value:
        :return:
        """
        self._extension = value

    def __str__(self):
        """
        Retourne une chaine de charactère contenant tous les attributs de l'objet
        :return:
        """
        def extension_propre():
            exten = ""
            for i in self.extension:
                exten = exten + i
            #exten = exten[0:-1]
            return exten

        return self.nom_regle + " " + self.amorce + " " + self.apartirde + " " \
            + self.prefixe + " " + self.nom_fichier + " " + self.postfixe \
             + " " + extension_propre()
