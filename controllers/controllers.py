from ..views.NewCharacterView import NewCharacterView
from ..models.Utils import Menu
from ..views.HomeMenuView import HomeMenuView
from ..views.BeginView import BeginDungeon
from tinydb import TinyDB

class AppliController:
    """ Main controller """

    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenu()
        while self.controller:
            self.controller = self.controller()


class HomeMenu:
    """ Liste des menus """
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        # Construction du menu
        self.menu.add("auto", "Creation du personnage", NewCharacter())
        self.menu.add("auto", "Début de l'aventure", Begin())
        self.menu.add("q", "Quitter", End())

        user_choice = self.view.get_user_choice()
        return user_choice.handler

class NewCharacter:
    """ Controller pour la création du perso """
    def __init__(self):
        self.view = NewCharacterView()

    def __call__(self):
        user_input = self.view.information_player()
        print(user_input)
        db = TinyDB("./game/db.json")
        create_character = db.table("perso")
        serialized_player1 = {
            'name': user_input[0].name,
            'char': user_input[0].char,
            }
        create_character.insert(serialized_player1)

        return HomeMenu

class Begin:
    """ Controller pour le début des aventures """
    def __init__(self):
        self.view = BeginDungeon()

    def __call__(self):
        self.view.bg()
        user_input = self.view.acte1()
        #print(user_input)

        return HomeMenu

class End:
    """ Controller pour fin de la partie """

    def __call__(self):
        print(" Au revoir ! ")
        print()


if __name__ == "__main__":
    app = AppliController()
    app.start()
