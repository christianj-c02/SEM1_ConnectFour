"""
Startpunkt des Programms.
"""

from .game import Game


def main():
    """
    Startet das Spiel.
    """
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
