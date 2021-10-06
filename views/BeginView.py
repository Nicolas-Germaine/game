from tinydb import TinyDB, Query
db = TinyDB("./game/db.json")
User = Query()
perso = db.table("perso")

class BeginDungeon:

    def bg(self):

        print()
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("Vous êtes", (perso.search(all)[0].name), ", un jeune Noob de lvl 1 et vous decidez de partir à l'aventure.")
        print("Vous arrivez apres des heures de marche en foret devant une magnifique grotte qui vous semble un coin parfait pour vos debut.")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print()

    def acte1(self):


        entry = input("Voulez vous entrer dans la grotte ? ( O/n ) ")
        decide = entry
        if decide == "o" or decide == "O":
            print("\n Vous entrez dans la grotte !")
        else:
            print("\n Vous êtes un lache.")

