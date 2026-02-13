# Planung und Umsetzung

## Anfangsplanung

Am Anfang wollten wir das Projekt in mehrere einfache Klassen teilen:

1. **Board**
   - hält das 6x7 Spielfeld
   - prüft gültige Züge
   - führt Züge aus
   - prüft Gewinn und Unentschieden

2. **Player / ComputerPlayer**
   - enthält Name und Symbol
   - ComputerPlayer wählt einen zufälligen gültigen Zug

3. **Game**
   - steuert den Spielablauf
   - fragt Modus ab (Mensch vs Mensch / Mensch vs Computer)
   - wechselt Spieler
   - prüft nach jedem Zug Gewinn und Ende

Wir haben uns bewusst für eine einfache Konsolenlösung entschieden.

## Geplante Methoden (vorab)

- Board:
  - `print_board()`
  - `is_valid_move(col)`
  - `drop_piece(col, symbol)`
  - `check_win(symbol)`
  - `is_full()`

- Game:
  - `setup_game()`
  - `switch_player()`
  - `get_human_move(player)`
  - `run()`

## Änderungen während der Umsetzung

- Ursprünglich wollten wir zuerst alles in `main.py` schreiben, haben es dann aber auf `board.py`, `player.py`, `game.py` aufgeteilt, damit es übersichtlicher bleibt.
- Die Gewinnprüfung war am Anfang nur horizontal/vertikal, diagonal wurde danach ergänzt.
- Bei der Eingabe gab es zuerst keinen Quit-Befehl, später wurde `q` eingebaut, weil es in der Angabe steht („Spiel beenden“).
- Wir haben die Computerlogik absichtlich einfach gelassen (zufälliger gültiger Zug), weil „nicht intelligent“ laut Angabe ausreichend ist.

## Kurzes Fazit

Die Aufteilung in wenige Klassen war für uns gut verständlich.  
Der schwierigste Teil war die diagonale Gewinnprüfung und die Testfälle dafür.
