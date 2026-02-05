# Projektkonzept: Vier Gewinnt

## 1. Die Grundregeln
Wir orientieren uns am klassischen Spiel. Das Spielfeld besteht aus genau 6 Reihen und 7 Spalten.Das Ziel ist einfach: Wer zuerst vier seiner Steine in einer Linie hat (egal ob waagerecht, senkrecht oder diagonal) hat gewonnen.

**Als Symbole verwenden wir:**
* Spieler 1 bekommt ein **X**.
* Spieler 2 / Computer bekommt ein **O**.
* Leere Felder werden durch ein **Leerzeichen** dargestellt.

## 2. Wie das Spiel startet
Wenn man das Programm startet, wird zuerst das leere Spielfeld im Hintergrund erstellt. Danach wird der Spieler gefragt, welchen Modus er spielen möchte:

* **Möglichkeit 1: Mensch gegen Mensch.** Wenn er diese Option wählt, kann er mit einer zweiten Person zusammen spielen.
* **Möglichkeit 2: Mensch gegen Computer.** Mit der importierten Library `random` werden Spielzüge vom Gegner simuliert. Wir benutzen die Library `random`, weil „der Computergegner“ nicht super schlau sein muss, sondern nur gültige Spielzüge simulieren soll.

## 3. Der genaue Spielablauf (Die Schleife)
Das Spiel läuft in einer dauerhaften Schleife. Jede Runde passiert Folgendes in dieser Reihenfolge:

1.  **Gewinnprüfung:** Das Programm schaut, ob der letzte Zug zum Sieg geführt hat. Wenn ja, wird der Sieger gefeiert und das Spiel ist vorbei.
2.  **Spielfeld anzeigen:** Das aktuelle Spielfeld wird angezeigt, damit man sieht, wie es steht.
3.  **Spielzug:** Der Spieler, der gerade dran ist, darf einen Stein werfen.
    * Wenn ein **Mensch** dran ist, gibt er die Spalten-Nummer (1 bis 7) ein.
    * Wenn der **Computer** dran ist, wählt er automatisch eine Spalte. Anfangs reicht es, wenn er irgendeine gültige Spalte nimmt, er muss noch nicht super schlau sein.
4.  **Validierung:** Das Programm prüft, ob der Zug erlaubt ist (also ob die Spalte existiert und noch Platz hat). Wenn der Zug gültig ist, fällt der Stein auf den tiefsten freien Platz.
5.  **Spielerwechsel:** Der Spieler wird gewechselt. War gerade Spieler 1 dran, ist jetzt Spieler 2 dran.

## 4. Die technische Struktur (Wichtig für die Bewertung)
Damit wir die Anforderungen von Hofer erfüllen, dürfen wir den ganzen Code nicht in eine einzige Datei packen. Wir nutzen eine saubere Ordner-Struktur mit Packages.

* Unser Hauptordner ist das Repository.
* Darin gibt es einen Unterordner für den Code, der eine `__init__.py` Datei enthält. Das macht ihn zum Package.

**Wir teilen den Code grob so auf:**
* `board.py`: Hier drin ist die Klasse für das Spielfeld. Sie kümmert sich nur um die Daten: Steine speichern, prüfen ob ein Zug geht und ob jemand gewonnen hat.
* `game.py`: Hier läuft das eigentliche Spiel. Diese Datei steuert den Ablauf, fragt den Benutzer nach Eingaben und ruft das Board auf.
* `player.py`: Hier definieren wir den Computergegner.

## 5. Das Spielende
Das Spiel ist vorbei, wenn einer vier Richtige hat (Sieg) oder wenn das Brett komplett voll ist, aber keiner gewonnen hat (Unentschieden).
