import sys
sys.path.append('.\\classes')
from regle import *
from listeregle import *
from renommage import *
from action import *
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import Combobox


class MyWindow(Tk):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.geom_fen(950, 400)
        self.menu()
        self.main_window()



    def main_window(self):

        self.title("Renommage de fichier")
        # Label
        title_lab = Label(self, text="Renommer en lot").grid(row=0, column=2)
        Label(self, text="Amorce").grid(row=4, column=0, pady=10)
        Label(self, text="Prefixe").grid(row=4, column=1)
        Label(self, text="Nom du fichier").grid(row=4, column=2)
        Label(self, text="Postfixe").grid(row=4, column=3)
        Label(self, text="Extension concernée\n(à séparer par des espaces)").grid(row=4, column=4)
        Label(self, text="A partir de : ").grid(row=6, column=0, pady=10)

        # Entry

        self.prefixe = StringVar()
        Entry(self, textvariable=self.prefixe).grid(row=5, column=1, padx=15)

        self.nom_fichier = StringVar()
        Entry(self, textvariable=self.nom_fichier).grid(row=5, column=2, padx=15)

        self.apartirde = StringVar()
        Entry(self, textvariable=self.apartirde).grid(row=7, column=0, padx=15)

        self.postfixe = StringVar()
        Entry(self, textvariable=self.postfixe).grid(row=5, column=3, padx=15)

        self.extension = StringVar()
        Entry(self, textvariable=self.extension).grid(row=5, column=4, padx=15)

        ### Image ###
        picture = PhotoImage(file="./data/Rename.gif")
        label1 = Label(self, image=picture)
        label1.image = picture
        label1.grid(row=1, column=5)
        
        ### Combobox ###
        self.amorce = StringVar()
        amorce_choice = ('Aucune', 'Lettres', 'Chiffres')
        Combobox(self, textvariable=self.amorce,
                 values=amorce_choice, state='readonly').grid(row=5, column=0, padx=15)
        self.amorce.set(amorce_choice[0])

        ### Button ###
        Button(self, text="Parcourir", command=self.browse).grid(row=1, column=2)
        Button(self, text="Renommer", command=self.renommer_fichers).grid(row=8, column=4)
        Button(self, text="Quitter", command=lambda: self.quit()).grid(row=8, column=3)



    def geom_fen(self, larg, haut):
        if self.winfo_screenwidth() < 1920:
            larg *= 0.8
            haut *= 0.8
        self.geometry(
            "%dx%d%+d%+d" % (larg, haut, (self.winfo_screenwidth() - larg) // 2,
                             (self.winfo_screenheight() - haut) // 2))

    def menu(self):
        """
        Création d'un menu sur la fenetre principale permettant d'accéder aux differentes options
        :return:
        """
        main_menu = Menu(self)
        roll_menu = Menu(main_menu, tearoff=0)                              # Menu déroulant
        roll_menu.add_command(label="Lister", command=self.window_liste)     # Option lister, renvoie sur une fenêtre listant les règles
        roll_menu.add_command(label="Créer", command=self.window_creer)#)    # Option créer, renvoie sur une fenêtre de creation

        help_menu = Menu(main_menu, tearoff=0)  # Menu Fils
        help_menu.add_command(label="À propos", command=self.help)          #A propos menu

        main_menu.add_cascade(label="Règles", menu=roll_menu)
        main_menu.add_cascade(label="?", menu=help_menu)

        self.config(menu=main_menu)

    def creer_nouvelle_regle(self):
        """
        Fonction permettant la sauvegarde d'une nouvelle regle dans regles.ini
        :return:
        """
        nom_regle = self.nomregle.get().replace(" ", "_")
        amorce = self.amorce.get()
        apartirde = self.apartirde.get()
        prefixe = self.prefix.get()
        nomfich = self.nom_fich.get()
        postfixe = self.postfix.get()
        ext = self.ext.get().replace(" ", ",")
        ma_regle = Regle(nom_regle, amorce, apartirde, prefixe, nomfich, postfixe, ext)
        ma_liste = ListeRegle()
        ma_liste.sauvegarder(ma_regle)
        messagebox.showinfo("Succès","Règle " + nom_regle + " créée")


    def window_creer(self):
        """
        Fenetre de création de règle
        :return:
        """
        win_creer = Toplevel(self)
        win_creer.geometry(
            "%dx%d%+d%+d" % (800, 225, (self.winfo_screenwidth() - 800) // 2,
                             (self.winfo_screenheight() - 225) // 2))
        win_creer.title("Création nouvelle règle")
        Label(win_creer, text="Nom de règle").grid(row=2, column=0)
        Label(win_creer, text="Amorce").grid(row=5, column=0, pady=10)
        Label(win_creer, text="Prefixe").grid(row=5, column=1)
        Label(win_creer, text="Nom du fichier").grid(row=5, column=2)
        Label(win_creer, text="Postfixe").grid(row=5, column=3)
        Label(win_creer, text="Extension concernée\n(à séparer par des espaces)").grid(row=5, column=4)
        Label(win_creer, text="A partir de : ").grid(row=7, column=0, pady=10)

        ### Entry ###
        self.nomregle = StringVar()
        Entry(win_creer, textvariable=self.nomregle).grid(row=3, column=0)
        self.prefix = StringVar()
        Entry(win_creer, textvariable=self.prefix).grid(row=6, column=1, padx=15)
        self.apartirde = StringVar()
        Entry(win_creer, textvariable=self.apartirde).grid(row=8, column=0, padx=15)
        self.postfix = StringVar()
        Entry(win_creer, textvariable=self.postfix).grid(row=6, column=3, padx=15)
        self.nom_fich = StringVar()
        Entry(win_creer, textvariable=self.nom_fich).grid(row=6, column=2, padx=15)
        self.ext = StringVar()
        Entry(win_creer, textvariable=self.ext).grid(row=6, column=4, padx=15, sticky = E)

        ### Combobox ###
        self.amorce = StringVar()
        amorce_choice = ('Aucune', 'Lettres', 'Chiffres')
        Combobox(win_creer, textvariable=self.amorce,
                 values=amorce_choice, state='readonly').grid(row=6, column=0, padx=15)
        self.amorce.set(amorce_choice[0])

        ### Button ###
        Button(win_creer, text="Créer", command = lambda: self.win_creer_destroyer(win_creer)).grid(row=8, column=4)
        Button(win_creer, text="Retour", command=lambda: win_creer.destroy()).grid(row=8, column=3)

        ### Image ###
        picture = PhotoImage(file="./data/Rename.gif")
        label1 = Label(self, image=picture)
        label1.image = picture
        label1.grid(row=1, column=5)

    def win_creer_destroyer(self, win):
        self.creer_nouvelle_regle()
        win.destroy()


    def regle_choisie(self):
        self.withdraw()
        win_regle_choisie = Toplevel(self)
        win_regle_choisie.geometry(
            "%dx%d%+d%+d" % (950, 400, (self.winfo_screenwidth() - 950) // 2,
                             (self.winfo_screenheight() - 400) // 2))
        win_regle_choisie.title("Renommage de fichier")
        # Label
        Label(win_regle_choisie, text="Renommer en lot").grid(row=0, column=2)
        Label(win_regle_choisie, text="Amorce").grid(row=3, column=0, pady=10)
        Label(win_regle_choisie, text="Prefixe").grid(row=3, column=1)
        Label(win_regle_choisie, text="Nom du fichier").grid(row=3, column=2)
        Label(win_regle_choisie, text="Postfixe").grid(row=3, column=3)
        Label(win_regle_choisie, text="Extension concernée").grid(row=3, column=4)
        Label(win_regle_choisie, text="A partir de : ").grid(row=6, column=0, pady=15)

        # Picture
        picture = PhotoImage(file="./data/Rename.gif")
        label1 = Label(win_regle_choisie, image=picture)
        label1.image = picture
        label1.grid(row=1, column=5)

        #Entry

        self.amorce = StringVar()
        a = Entry(win_regle_choisie, textvariable=self.amorce)
        a.grid(row=5, column=0, padx=15)
        a.insert(0,self.amorc.get())

        self.prefixe = StringVar()
        p = Entry(win_regle_choisie, textvariable=self.prefixe)
        p.grid(row=5, column=1, padx=15)
        p.insert(0, self.prefix.get())

        self.nom_fichier = StringVar()
        n = Entry(win_regle_choisie, textvariable=self.nom_fichier)
        n.grid(row=5, column=2, padx=15)
        n.insert(0, self.nomFichier.get())

        self.apartirde = StringVar()
        ap = Entry(win_regle_choisie, textvariable=self.apartirde)
        ap.grid(row=7, column=0, padx=15)
        ap.insert(0, self.apart.get())

        self.postfixe = StringVar()
        po = Entry(win_regle_choisie, textvariable=self.postfixe)
        po.grid(row=5, column=3, padx=15)
        po.insert(0, self.postfix.get())

        self.extension = StringVar()
        e = Entry(win_regle_choisie, textvariable=self.extension)
        e.grid(row=5, column=4, padx=15)
        e.insert(0, self.extens.get())

        ### Button ###
        Button(win_regle_choisie, text="Parcourir", command=self.browse).grid(row=1, column=2)
        Button(win_regle_choisie, text="Renommer", command=lambda: self.test_deconify(win_regle_choisie)).grid(row=8, column=4)
        Button(win_regle_choisie, text="Retour", command=lambda: self.regle_choisie_destroyer(win_regle_choisie)).grid(row=8, column=3)
        Button(win_regle_choisie, text="Quitter", command=lambda: self.quit()).grid(row=9, column=4)

    def test_deconify(self, win):
        if self.renommer_fichers() == 1:
            win.destroy()

    def regle_choisie_destroyer(self, window):
        window.destroy()
        self.deiconify()

    @staticmethod #pour extension
    def occ(char, liste):
        cpt = 0
        for i in liste:
            if i == char:
                cpt += 1
        return cpt

    def launch(self):

        toto = self.amorce.get()
        nom_regle = toto.split(" ")[0]
        amorce = toto.split(" ")[1]
        apartirde = toto.split(" ")[2]
        prefixe = toto.split(" ")[3]
        nom_fichier = toto.split(" ")[4]
        postfixe = toto.split(" ")[5]
        ext = toto.split(" ")[6]

        win_liste_select = Toplevel(self)
        win_liste_select.geometry(
            "%dx%d%+d%+d" % (750, 225, (self.winfo_screenwidth() - 750) // 2,
                           (self.winfo_screenheight() - 225) // 2))
        ### Label ###
        Label(win_liste_select, text="Nom de règle").grid(row=2, column=0)
        Label(win_liste_select, text="Amorce").grid(row=5, column=0, pady=10)
        Label(win_liste_select, text="Prefixe").grid(row=5, column=1)
        Label(win_liste_select, text="Nom du fichier").grid(row=5, column=2)
        Label(win_liste_select, text="Postfixe").grid(row=5, column=3)
        Label(win_liste_select, text="Extension concernée").grid(row=5, column=4)
        Label(win_liste_select, text="A partir de : ").grid(row=7, column=0, pady=10)

        ## Entry ###
        self.nomR = Entry(win_liste_select)
        self.nomR.grid(row=3, column=0)
        self.nomR.insert(0, nom_regle)

        self.amorc = Entry(win_liste_select)
        self.amorc.grid(row=6, column=0)
        self.amorc.insert(0, amorce)

        self.apart = Entry(win_liste_select)
        self.apart.grid(row=8, column=0, padx=15)
        self.apart.insert(0, apartirde)

        self.prefix = Entry(win_liste_select)
        self.prefix.grid(row=6, column=1, padx=15)
        self.prefix.insert(0, prefixe)

        self.nomFichier = Entry(win_liste_select)
        self.nomFichier.grid(row=6, column=2, padx=15)
        self.nomFichier.insert(0, nom_fichier)

        self.postfix = Entry(win_liste_select)
        self.postfix.grid(row=6, column=3)
        self.postfix.insert(0, postfixe)

        self.extens = Entry(win_liste_select)
        self.extens.grid(row=6, column=4,padx = 15, sticky = E)
        self.extens.insert(0, ext)

        Button(win_liste_select, text="Choisir", command=lambda: self.launch_destroyer(win_liste_select)).grid(row=8, column=4)
        Button(win_liste_select, text="Retour", command=lambda: win_liste_select.destroy()).grid(row=8, column=3)

    def launch_destroyer(self, window):
        MyWindow.regle_choisie(self)
        window.destroy()


    def window_liste(self):

        try:
            win_liste = Toplevel(self)
            win_liste.geometry(
            "%dx%d%+d%+d" % (150, 50, (self.winfo_screenwidth() - 150) // 2,
                             (self.winfo_screenheight() - 50) // 2))
            win_liste.title("Liste des règles")

            try:

                liste_regle = ListeRegle()
                liste_regle.charger()
                liste = liste_regle.get()

                ### Combobox ###
                self.amorce = StringVar()
                Combobox(win_liste, textvariable=self.amorce,
                        values=liste, state='readonly', ).grid(row=0, column=0)
                self.amorce.set(liste[0])
            except IndexError:
                win_liste.destroy()
                messagebox._show("Oups", "Liste vide, sauvegarder des règles pour la remplir.")

            Button(win_liste, text="valider", command= lambda: self.window_liste_destroyer(win_liste)).grid(row=1, column=0)
        except TclError:
            pass


    def window_liste_destroyer(self, window):
        self.launch()
        window.destroy()


    @staticmethod
    def help(): #help
        messagebox.showinfo("About", "Logiciel crée par Oussama CALLAS")

    def renommer_fichers(self):
        try:
            nomrep = self.file_path
        except AttributeError:
            messagebox._show("Erreur", "Chemin invalide ou non précisé.")
        a_partir_de = self.apartirde.get()
        amorce = self.amorce.get()
        prefixe = self.prefixe.get()
        nom_fichier = self.nom_fichier.get()
        postfixe = self.postfixe.get()
        extension = self.extension.get().replace(" ",",")
        ma_regle = Regle(" ", amorce, a_partir_de, prefixe, nom_fichier, postfixe, extension)
        try:
            toto = Renommage(ma_regle, nomrep)
            if toto.renommer(toto)== 1:
                self.deiconify()
                return 1
        except UnboundLocalError:
            pass
    def browse(self):
        self.file_path = filedialog.askdirectory()


