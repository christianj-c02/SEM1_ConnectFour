"""
Enthält die Board-Klasse für Vier Gewinnt.
"""


class Board:
    """
    Repräsentiert das Spielbrett von Vier Gewinnt.

    Attributes
    ----------
    rows : int
        Anzahl der Reihen (standardmäßig 6).
    cols : int
        Anzahl der Spalten (standardmäßig 7).
    empty_symbol : str
        Zeichen für leere Felder.
    grid : list[list[str]]
        2D-Liste mit dem aktuellen Brettzustand.
    """

    def __init__(self, rows=6, cols=7, empty_symbol="."):
        """
        Erstellt ein neues leeres Spielbrett.

        Parameters
        ----------
        rows : int, optional
            Anzahl der Reihen.
        cols : int, optional
            Anzahl der Spalten.
        empty_symbol : str, optional
            Symbol für leere Felder.
        """
        self.rows = rows
        self.cols = cols
        self.empty_symbol = empty_symbol
        self.grid = []

        for _ in range(self.rows):
            row = []
            for _ in range(self.cols):
                row.append(self.empty_symbol)
            self.grid.append(row)

    def print_board(self):
        """
        Gibt das aktuelle Spielbrett in der Konsole aus.
        """
        print()
        header = "  "
        for c in range(self.cols):
            header += str(c + 1) + " "
        print(header)

        for row in self.grid:
            line = "  "
            for cell in row:
                line += cell + " "
            print(line)
        print()

    def is_valid_move(self, col):
        """
        Prüft, ob in eine Spalte ein Stein geworfen werden kann.

        Parameters
        ----------
        col : int
            Spaltenindex (0-basiert).

        Returns
        -------
        bool
            True, wenn der Zug gültig ist, sonst False.
        """
        if col < 0 or col >= self.cols:
            return False

        # Spalte ist nur gültig, wenn oberstes Feld leer ist
        if self.grid[0][col] != self.empty_symbol:
            return False

        return True

    def drop_piece(self, col, symbol):
        """
        Lässt einen Stein in eine Spalte fallen.

        Parameters
        ----------
        col : int
            Spaltenindex (0-basiert).
        symbol : str
            Spielstein des Spielers (z. B. 'X' oder 'O').

        Returns
        -------
        bool
            True, wenn erfolgreich, sonst False.
        """
        if not self.is_valid_move(col):
            return False

        # Von unten nach oben suchen
        for r in range(self.rows - 1, -1, -1):
            if self.grid[r][col] == self.empty_symbol:
                self.grid[r][col] = symbol
                return True

        return False

    def check_win(self, symbol):
        """
        Prüft, ob ein Symbol bereits gewonnen hat.

        Parameters
        ----------
        symbol : str
            Zu prüfendes Symbol.

        Returns
        -------
        bool
            True, wenn 4 in einer Reihe gefunden werden, sonst False.
        """
        # Horizontal prüfen
        for r in range(self.rows):
            for c in range(self.cols - 3):
                if (
                    self.grid[r][c] == symbol
                    and self.grid[r][c + 1] == symbol
                    and self.grid[r][c + 2] == symbol
                    and self.grid[r][c + 3] == symbol
                ):
                    return True

        # Vertikal prüfen
        for c in range(self.cols):
            for r in range(self.rows - 3):
                if (
                    self.grid[r][c] == symbol
                    and self.grid[r + 1][c] == symbol
                    and self.grid[r + 2][c] == symbol
                    and self.grid[r + 3][c] == symbol
                ):
                    return True

        # Diagonal nach rechts unten prüfen (\)
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if (
                    self.grid[r][c] == symbol
                    and self.grid[r + 1][c + 1] == symbol
                    and self.grid[r + 2][c + 2] == symbol
                    and self.grid[r + 3][c + 3] == symbol
                ):
                    return True

        # Diagonal nach rechts oben prüfen (/)
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                if (
                    self.grid[r][c] == symbol
                    and self.grid[r - 1][c + 1] == symbol
                    and self.grid[r - 2][c + 2] == symbol
                    and self.grid[r - 3][c + 3] == symbol
                ):
                    return True

        return False

    def is_full(self):
        """
        Prüft, ob das Brett voll ist.

        Returns
        -------
        bool
            True, wenn kein weiterer Zug möglich ist, sonst False.
        """
        for c in range(self.cols):
            if self.grid[0][c] == self.empty_symbol:
                return False
        return True
