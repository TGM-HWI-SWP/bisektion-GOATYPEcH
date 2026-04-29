# README – Numerisches Lösen / Bisektionsverfahren

Dieses Projekt behandelt numerische Verfahren zur Nullstellenbestimmung. Die einzelnen Python-Dateien gehören zu den Aufgaben 5 bis 9.

## Beschreibung

Dieses Projekt wurde im Fach **Softwareentwicklung und Projektmanagement (SWP)** erstellt.  
Ziel des Projekts war die Umsetzung numerischer Verfahren zur **Nullstellenbestimmung** mit Python.

Dabei wurden verschiedene mathematische Aufgaben bearbeitet:

- Entwicklung eines Solvers mit dem **Bisektionsverfahren**
- Erweiterung durch das **Regula-Falsi-Verfahren**
- Grafische Darstellung der Iterationen mit **matplotlib**
- Test des Solvers mit einem Polynom
- Anwendung auf ein reales Problem (Leitungslänge einer Stromleitung)

---

## Voraussetzungen

Benötigt wird Python 3.12 oder neuer.

Zusätzlich werden für Aufgabe 7 folgende Bibliotheken benötigt:

```bash
pip install matplotlib numpy
```

## Dateien im Projekt

```text
Aufgabe5.py   # Bisektionsverfahren
Aufgabe6.py   # Regula-Falsi-Verfahren
Aufgabe7.py   # Grafische Visualisierung / Animation
Aufgabe8.py   # Test am Polynom P4
Aufgabe9.py   # Berechnung der Leitungslänge
```

---

## Aufgabe 5 – Solver mit Bisektionsverfahren

In `Aufgabe5.py` wird ein Solver zur Nullstellenbestimmung mit dem Bisektionsverfahren umgesetzt.

Die Klasse `Solver` bekommt eine Funktion als String übergeben, zum Beispiel:

```python
solver = Solver("x**2 - n")
```

Die Methode `f()` berechnet den Funktionswert mit `eval()`. Dadurch kann die Funktion relativ einfach geändert werden.

Die Methode `bisektion()` sucht eine Nullstelle im Intervall `[a, b]`. Dafür wird immer der Mittelpunkt berechnet:

```python
c = (a + b) / 2
```

Danach wird geprüft, in welcher Hälfte des Intervalls sich der Vorzeichenwechsel befindet. Diese Hälfte wird weiterverwendet. Das wiederholt sich so lange, bis die gewünschte Genauigkeit erreicht ist.

Getestet wird der Solver mit:

```text
n = 25
n = 81
n = 144
```

Dabei wird die numerische Lösung mit der analytischen Lösung `sqrt(n)` verglichen.

Starten:

```bash
python Aufgabe5.py
```

---

## Aufgabe 6 – Regula Falsi

In `Aufgabe6.py` wird als alternatives Verfahren das Regula-Falsi-Verfahren verwendet.

Auch hier wird die Funktion

```python
f(x) = x**2 - n
```

verwendet. Der Unterschied zur Bisektion ist, dass nicht der Mittelpunkt genommen wird, sondern der Schnittpunkt der Sekante mit der x-Achse berechnet wird:

```python
c = b - fb * (b - a) / (fb - fa)
```

Das Verfahren arbeitet ebenfalls mit einem Intervall `[a, b]`, bei dem `f(a)` und `f(b)` unterschiedliche Vorzeichen haben müssen.

Getestet wird mit:

```text
n = 25
n = 81
n = 144
```

Starten:

```bash
python Aufgabe6.py
```

---

## Aufgabe 7 – Grafische Visualisierung

In `Aufgabe7.py` soll die Nullstellenfindung grafisch mit `matplotlib` dargestellt werden.

Die Datei verwendet:

```python
matplotlib
numpy
FuncAnimation
```

Die Animation zeigt den Verlauf der Annäherung an die Nullstelle. Dabei werden zwei Diagramme dargestellt:

1. Funktionsgraph mit aktuellem Intervall und aktuellem Punkt `c`
2. Verlauf der Annäherung an die analytische Lösung

Wichtig ist, dass die Animation in einer globalen Variable gespeichert wird:

```python
anim = None
```

und später:

```python
anim = FuncAnimation(...)
```

Dadurch verhindert man die Warnung, dass die Animation gelöscht wurde, bevor sie angezeigt wird.

Starten:

```bash
python Aufgabe7.py
```

Hinweis: In der aktuellen Datei müssen Schreibfehler wie `annotation`, `pylot`, `InterationData`, `interation` und `thight_layout` korrigiert werden, damit sie fehlerfrei läuft.

---

## Aufgabe 8 – Polynom P4

In `Aufgabe8.py` wird der Solver an einem Polynom getestet:

```python
P4(x) = 2x + x**2 + 3x**3 - x**4
```

Gesucht ist die Nullstelle bei ungefähr:

```text
x ≈ 3,4567
```

Als Intervall wird gewählt:

```text
[3, 4]
```

Das Intervall ist passend, weil ein Vorzeichenwechsel zwischen `P4(3)` und `P4(4)` vorhanden ist.

Es werden zwei Genauigkeiten getestet:

```text
epsilon = 10^-2
epsilon = 10^-8
```

Damit wird geprüft, wie viele Iterationsschritte für verschiedene Genauigkeiten benötigt werden.

Starten:

```bash
python Aufgabe8.py
```

---

## Aufgabe 9 – Berechnung der Leitungslänge

In `Aufgabe9.py` wird ein reales Anwendungsbeispiel berechnet.

Gegeben:

```text
Abstand zwischen den Masten: 100 m
Durchhang in der Mitte: 10 m
```

Gesucht:

```text
Krümmungsradius a
Länge der Leitung l
```

Aus der Kettenlinie wird folgende Nullstellenfunktion gebildet:

```python
f(a) = a * (cosh(50 / a) - 1) - 10
```

Diese Gleichung kann nicht einfach nach `a` umgestellt werden. Deshalb wird sie mit dem Bisektionsverfahren gelöst.

Als Startintervall wird verwendet:

```text
[100, 200]
```

Nach der Berechnung des Krümmungsradius wird die Länge der Leitung mit folgender Formel berechnet:

```python
l = 2 * a * sinh(w / (2 * a))
```

Starten:

```bash
python Aufgabe9.py
```

Erwartetes Ergebnis ungefähr:

```text
Krümmungsradius a ≈ 126,63 m
Leitungslänge l   ≈ 102,62 m
```

---