# Vier Gewinnt (SEM – AI WS 2025)

In diesem Projekt wurde das Spiel **Vier Gewinnt** in Python umgesetzt.  
Es gibt ein Spielbrett mit 6 Reihen und 7 Spalten. Zwei Spieler lassen abwechselnd Steine in Spalten fallen.  
Wer zuerst 4 eigene Steine horizontal, vertikal oder diagonal hat, gewinnt.

Das Spiel kann entweder **Mensch gegen Mensch** oder **Mensch gegen Computer** gespielt werden.  
Der Computer spielt absichtlich einfach (zufälliger gültiger Zug), nur um grundsätzlich das SPiel simulieren zu können.

## Starten

1. Virtuelle Umgebung erstellen
2. Abhängigkeiten installieren
3. Spiel starten

```bash
pip install -r requirements.txt
python -m src.main
```

## Tests starten

```bash
pytest
```

Die Tests prüfen nur die Spielzug- und Gewinnlogik (Board).
