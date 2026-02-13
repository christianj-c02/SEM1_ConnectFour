"""
Steuert den Spielablauf.
"""

from .board import Board
from .player import Player, ComputerPlayer


class Game:
    """
    Führt den gesamten Spielablauf von Vier Gewinnt aus.

    Attributes
    ----------
    board : Board
        Das Spielbrett.
    players : list
        Liste der zwei Spielerobjekte.
    current_index : int
        Index des aktuellen Spielers (0 oder 1).
    """

    def __init__(self):
        """
        Erstellt ein neues Spielobjekt.
        """
        self.board = Board()
        self.players = []
        self.current_index = 0

    def setup_game(self):
        """
        Fragt den Spielmodus ab und erstellt die Spieler.
        """
        print("Willkommen bei Vier Gewinnt!")
        print("Modus wählen:")
        print("1) Mensch gegen Mensch")
        print("2) Mensch gegen Computer")

        while True:
            mode = input("Eingabe (1 oder 2): ").strip()
            if mode == "1":
                name1 = input("Name Spieler 1 (X): ").strip()
                name2 = input("Name Spieler 2 (O): ").strip()
                if name1 == "":
                    name1 = "Spieler1"
                if name2 == "":
                    name2 = "Spieler2"
                self.players = [Player(name1, "X"), Player(name2, "O")]
                break
            elif mode == "2":
                name1 = input("Dein Name (X): ").strip()
                if name1 == "":
                    name1 = "Spieler"
                self.players = [Player(name1, "X"), ComputerPlayer("Computer", "O")]
                break
            else:
                print("Ungültige Eingabe. Bitte 1 oder 2 eingeben.")

    def switch_player(self):
        """
        Wechselt zum nächsten Spieler.
        """
        if self.current_index == 0:
            self.current_index = 1
        else:
            self.current_index = 0

    def get_human_move(self, player):
        """
        Liest den Zug eines menschlichen Spielers ein.

        Parameters
        ----------
        player : Player
            Aktueller Spieler.

        Returns
        -------
        int | None
            Spaltenindex (0-basiert) oder None, wenn Spiel beendet werden soll.
        """
        while True:
            user_input = input(
                f"{player.name} ({player.symbol}) - Spalte 1-7 wählen oder q zum Beenden: "
            ).strip().lower()

            if user_input == "q":
                return None

            if not user_input.isdigit():
                print("Bitte eine Zahl eingeben.")
                continue

            col = int(user_input) - 1
            if not self.board.is_valid_move(col):
                print("Ungültiger Zug (Spalte voll oder außerhalb).")
                continue

            return col

    def run(self):
        """
        Startet das Spiel und führt die Spielschleife aus.
        """
        self.setup_game()
        self.board.print_board()

        while True:
            current_player = self.players[self.current_index]

            # Zug holen
            if isinstance(current_player, ComputerPlayer):
                col = current_player.choose_move(self.board)
                if col == -1:
                    print("Keine gültigen Züge mehr möglich.")
                    print("Unentschieden.")
                    break
                print(f"Computer ({current_player.symbol}) spielt Spalte {col + 1}")
            else:
                col = self.get_human_move(current_player)
                if col is None:
                    print("Spiel wurde beendet.")
                    break

            # Zug durchführen
            success = self.board.drop_piece(col, current_player.symbol)
            if not success:
                # Sollte normal nicht passieren, da vorher geprüft wurde
                print("Zug konnte nicht durchgeführt werden.")
                continue

            # Brett anzeigen (laut Angabe nach jedem Zug)
            self.board.print_board()

            # Gewinn prüfen
            if self.board.check_win(current_player.symbol):
                print(f"Gewonnen: {current_player.name} ({current_player.symbol})")
                break

            # Auf Unentschieden prüfen
            if self.board.is_full():
                print("Unentschieden. Das Brett ist voll.")
                break

            # Zum nächsten Spieler
            self.switch_player()
