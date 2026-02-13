"""
Enthält Klassen für Spieler.
"""

import random


class Player:
    """
    Repräsentiert einen menschlichen Spieler.

    Attributes
    ----------
    name : str
        Name des Spielers.
    symbol : str
        Spielsymbol des Spielers.
    """

    def __init__(self, name, symbol):
        """
        Erstellt einen neuen Spieler.

        Parameters
        ----------
        name : str
            Spielername.
        symbol : str
            Spielsymbol.
        """
        self.name = name
        self.symbol = symbol


class ComputerPlayer(Player):
    """
    Repräsentiert einen einfachen Computergegner.

    Der Computer wählt nur zufällige gültige Züge.
    """

    def choose_move(self, board):
        """
        Wählt eine gültige Spalte zufällig aus.

        Parameters
        ----------
        board : Board
            Aktueller Brettzustand.

        Returns
        -------
        int
            Gewählte Spalte (0-basiert). Gibt -1 zurück, falls kein Zug möglich.
        """
        valid_cols = []
        for c in range(board.cols):
            if board.is_valid_move(c):
                valid_cols.append(c)

        if len(valid_cols) == 0:
            return -1

        return random.choice(valid_cols)
