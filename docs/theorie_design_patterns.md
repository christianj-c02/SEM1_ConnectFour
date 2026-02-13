# Theorie: Design Patterns

## Pattern 1: Strategy

### Problem
Man hat eine Aufgabe, die auf unterschiedliche Arten gelöst werden kann.  
Wenn man alles mit vielen `if/else` in eine Klasse schreibt, wird der Code schnell unübersichtlich.

### Idee/Lösung
Beim Strategy-Pattern kapselt man verschiedene Algorithmen in eigene Klassen (Strategien).  
Die Hauptklasse bekommt eine Strategie übergeben und verwendet sie, ohne die Details zu kennen.

### Beispiel
Bei einem Spiel könnte ein Computergegner unterschiedliche Strategien haben:
- Zufallszug
- defensiv (blocken)
- aggressiv (Gewinnzug suchen)

Die Game-Logik muss dann nur noch sagen: „Bitte wähle einen Zug“, und die Strategie macht den Rest.

### Vorteil
- Algorithmen sind austauschbar
- weniger `if/else`
- besser testbar und erweiterbar

### Nachteil
- mehr Klassen
- für kleine Projekte manchmal zu viel Aufwand


---

## Pattern 2: Observer

### Problem
Wenn sich ein Objektzustand ändert, sollen mehrere andere Objekte informiert werden (z. B. Anzeige, Logging, Statistik).  
Ohne Pattern koppelt man diese Dinge oft direkt zusammen, was unflexibel ist.

### Idee/Lösung
Beim Observer-Pattern gibt es ein Subjekt (Publisher), das Ereignisse meldet.  
Observer (Subscriber) registrieren sich und werden bei Änderungen benachrichtigt.

### Beispiel
In einem GUI-Spiel könnte das Spielmodell nach jedem Zug ein Event auslösen:
- UI aktualisiert das Brett
- Logger schreibt den Zug mit
- Statistik zählt Züge

Das Modell kennt nur die Observer-Schnittstelle, nicht deren konkrete Implementierung.

### Vorteil
- lose Kopplung
- flexibel erweiterbar
- gut bei Event-basierten Systemen

### Nachteil
- Ablauf kann schwerer nachvollziehbar werden
- bei vielen Observern mehr Komplexität
