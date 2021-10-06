class HomeMenuView:
    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print()
        print(">>>>> Accueil du jeu <<<<<")
        print()
        for key, entry in self.menu.items():
            print(f"{key}: {entry.option}")

    def get_user_choice(self):
        while True:
            # afficher le menu à l'utilisateur
            self._display_menu()
            # demander à l'utilisateur de faire un choix
            print()
            choice = input("Entrez votre choix >> ")
            print()
            # valider le choix utilisateur
            if choice in self.menu:
                # retourner le choix de l'utilisateur
                return self.menu[choice]