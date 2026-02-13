# Theorie: Software Design

Wenn ich ein altes Modul übernehme, das nur aus wenigen Klassen mit sehr langen Methoden besteht, entstehen mehrere Nachteile.

## Nachteile durch den vorhandenen Code

1. **Schwere Lesbarkeit und Einarbeitung**  
   Sehr lange Methoden sind schwer zu verstehen. Man muss viele Zeilen lesen, bevor klar ist, was genau passiert.

2. **Fehlende Wartbarkeit**  
   Änderungen sind riskant. Wenn eine Methode mehrere Aufgaben gleichzeitig macht, kann eine kleine Änderung an einer Stelle ungewollte Nebenwirkungen haben.

3. **Schwieriger zu testen**  
   Große Methoden sind oft schwer mit Unit Tests abzudecken. Man kann einzelne Teile der Logik nicht gut isolieren.

4. **Höhere Fehleranfälligkeit**  
   Bei unklaren Abhängigkeiten und wenig Dokumentation werden Bugs oft spät gefunden.

5. **Geringe Wiederverwendbarkeit**  
   Wenn Logik stark vermischt ist, kann man Teile kaum in anderen Kontexten wiederverwenden.

## Möglicherweise verletzte Software-Design-Prinzipien

1. **Single Responsibility Principle (SRP)**  
   Eine Klasse oder Methode sollte möglichst nur eine Aufgabe haben. Bei langen Methoden ist das oft nicht der Fall.

2. **Separation of Concerns**  
   Verschiedene Verantwortlichkeiten (z. B. Logik, Datenzugriff, Darstellung) sind oft vermischt.

3. **DRY (Don’t Repeat Yourself)**  
   In großen alten Modulen wird Code häufig mehrfach ähnlich geschrieben statt zentral gelöst.

4. **KISS (Keep It Simple, Stupid)**  
   Die Lösung ist oft unnötig komplex gewachsen und dadurch schwer nachvollziehbar.

5. **Clean Code Grundsätze**  
   Z. B. sprechende Namen, kurze Funktionen, klare Struktur und brauchbare Dokumentation fehlen oft.

## Zusammenfassung

Für neue Entwickler*innen ist so ein Modul problematisch, weil Verständnis, Tests und sichere Änderungen viel Zeit kosten.  
Mit kleineren Klassen, kürzeren Methoden, klaren Verantwortlichkeiten und besserer Dokumentation wäre der Code deutlich robuster und einfacher wartbar.
