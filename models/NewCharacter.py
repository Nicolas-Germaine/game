

class NewPlayers:
    """add players for tournament"""

    def __init__(self, name, char):
        self.name = name
        self.char = char


    def __repr__(self) -> str:
        """Used in print"""
        return f"Vous êtes {self.name}, et vous êtes un {self.char}"
