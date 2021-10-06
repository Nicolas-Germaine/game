from ..models.NewCharacter import NewPlayers

class NewCharacterView:

    def info_menu(self):
        print()
        print("######## Creation de votre personnage !!! ############")
        print()

    def information_player(self):

        new_player = []

        name = input("Tapez votre pseudo >> ")
        char = input("\n #### Qu'elle classe ? #### \n\n 1 pour Guerrier \n 2 pour Mage \n 3 pour Archer \n\n >>>>> ")
        if char == "1":
            char = "Guerrier"
        elif char == "2":
            char = "Mage"
        else:
            char = "Archer"
        print()
        
        info = NewPlayers(name, char)
        new_player.append(info)
        return new_player
