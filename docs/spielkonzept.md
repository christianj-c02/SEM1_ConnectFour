# Projektkonzept: Vier Gewinnt

## 1. Die Grundregeln
[cite_start]Wir orientieren uns am klassischen Spiel[cite: 9]. [cite_start]Das Spielfeld besteht aus genau 6 Reihen und 7 Spalten[cite: 42]. [cite_start]Das Ziel ist einfach: Wer zuerst vier seiner Steine in einer Linie hat (egal ob waagerecht, senkrecht oder diagonal) hat gewonnen[cite: 42].

**Als Symbole verwenden wir:**
* Spieler 1 bekommt ein **X**.
* Spieler 2 / Computer bekommt ein **O**.
* Leere Felder werden durch ein **Leerzeichen** dargestellt.

## 2. Wie das Spiel startet
Wenn man das Programm startet, wird zuerst das leere Spielfeld im Hintergrund erstellt. [cite_start]Danach wird der Spieler gefragt, welchen Modus er spielen möchte[cite: 43]:

* **Möglichkeit 1: Mensch gegen Mensch.** Wenn er diese Option wählt, kann er mit einer zweiten Person zusammen spielen.
* **Möglichkeit 2: Mensch gegen Computer.** Mit der importierten Library `random` werden Spielzüge vom Gegner simuliert. [cite_start]Wir benutzen die Library `random`, weil „der Computergegner“ nicht super schlau sein muss, sondern nur gültige Spielzüge simulieren soll[cite: 49].

## 3. Der genaue Spielablauf (Die Schleife)
Das Spiel läuft in einer dauerhaften Schleife. [cite_start]Jede Runde passiert Folgendes in dieser Reihenfolge[cite: 44]:

1.  **Gewinnprüfung:** Das Programm schaut, ob der letzte Zug zum Sieg geführt hat. [cite_start]Wenn ja, wird der Sieger gefeiert und das Spiel ist vorbei[cite: 45].
2.  [cite_start]**Spielfeld anzeigen:** Das aktuelle Spielfeld wird angezeigt, damit man sieht, wie es steht[cite: 46].
3.  [cite_start]**Spielzug:** Der Spieler, der gerade dran ist, darf einen Stein werfen[cite: 48].
    * Wenn ein **Mensch** dran ist, gibt er die Spalten-Nummer (1 bis 7) ein.
    * Wenn der **Computer** dran ist, wählt er automatisch eine Spalte. [cite_start]Anfangs reicht es, wenn er irgendeine gültige Spalte nimmt, er muss noch nicht super schlau sein[cite: 49].
4.  **Validierung:** Das Programm prüft, ob der Zug erlaubt ist (also ob die Spalte existiert und noch Platz hat). Wenn der Zug gültig ist, fällt der Stein auf den tiefsten freien Platz.
5.  **Spielerwechsel:** Der Spieler wird gewechselt. War gerade Spieler 1 dran, ist jetzt Spieler 2 dran.

## 4. Die technische Struktur (Wichtig für die Bewertung)
Damit wir die Anforderungen von Hofer erfüllen, dürfen wir den ganzen Code nicht in eine einzige Datei packen. [cite_start]Wir nutzen eine saubere Ordner-Struktur mit Packages[cite: 22].

* Unser Hauptordner ist das Repository.
* Darin gibt es einen Unterordner für den Code, der eine `__init__.py` Datei enthält. [cite_start]Das macht ihn zum Package[cite: 22, 23].

**Wir teilen den Code grob so auf:**
* `board.py`: Hier drin ist die Klasse für das Spielfeld. Sie kümmert sich nur um die Daten: Steine speichern, prüfen ob ein Zug geht und ob jemand gewonnen hat.
* `game.py`: Hier läuft das eigentliche Spiel. Diese Datei steuert den Ablauf, fragt den Benutzer nach Eingaben und ruft das Board auf.
* `player.py`: Hier definieren wir den Computergegner.

## 5. Das Spielende
[cite_start]Das Spiel ist vorbei, wenn einer vier Richtige hat (Sieg) oder wenn das Brett komplett voll ist, aber keiner gewonnen hat (Unentschieden)[cite: 45].