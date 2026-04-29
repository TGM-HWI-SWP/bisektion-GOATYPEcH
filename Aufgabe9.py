"""
Aufgabe 9 – Berechnung der Leitungslänge

Gegeben:
- Abstand zwischen den Masten: w = 100 m
- Durchhang in der Mitte: 10 m

Gesucht:
- Krümmungsradius a
- Länge der Leitung l

Verwendete Gleichungen:
y(x) = a * cosh(x / a) - a + y0

Randbedingung:
y(50) = y0 + 10

Daraus folgt:
a * (cosh(50 / a) - 1) - 10 = 0

Diese Gleichung wird mit dem Bisektionsverfahren gelöst.
"""

import math
from typing import Callable


def funktion_a(a: float) -> float:
    """
    Funktion zur Berechnung des Krümmungsradius a.

    Aus der Randbedingung:
    y(50) = y0 + 10

    entsteht die Nullstellenfunktion:
    f(a) = a * (cosh(50 / a) - 1) - 10

    Die Nullstelle dieser Funktion ist der gesuchte Wert für a.
    """
    return a * (math.cosh(50 / a) - 1) - 10


def bisektion(
    func: Callable[[float], float],
    a: float,
    b: float,
    epsilon: float = 1e-8,
    max_iter: int = 1000
) -> tuple[float, int]:
    """
    Berechnet eine Nullstelle mit dem Bisektionsverfahren.

    Parameter:
        func     -> Funktion, deren Nullstelle gesucht wird
        a        -> linke Intervallgrenze
        b        -> rechte Intervallgrenze
        epsilon  -> gewünschte Genauigkeit
        max_iter -> maximale Anzahl an Iterationen

    Rückgabe:
        Nullstelle und Anzahl der Iterationen
    """

    try:
        # Funktionswerte an den Intervallgrenzen berechnen
        fa = func(a)
        fb = func(b)

        # Prüfen, ob ein Vorzeichenwechsel vorhanden ist
        if fa * fb >= 0:
            raise ValueError(
                "Ungültiges Intervall! "
                "f(a) und f(b) müssen unterschiedliche Vorzeichen haben."
            )

        iteration = 0

        # Solange das Intervall größer als die Genauigkeit ist
        while abs(b - a) > epsilon and iteration < max_iter:

            # Mittelpunkt des Intervalls berechnen
            c = (a + b) / 2

            # Funktionswert am Mittelpunkt berechnen
            fc = func(c)

            # Wenn die Nullstelle genau genug gefunden wurde
            if abs(fc) < epsilon:
                return c, iteration + 1

            # Prüfen, in welcher Hälfte der Vorzeichenwechsel liegt
            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc

            # Iterationszähler erhöhen
            iteration += 1

        # Näherungswert zurückgeben
        return (a + b) / 2, iteration

    except Exception as error:
        print("Fehler:", error)
        return 0.0, 0


def berechne_leitungslaenge(a: float, w: float = 100.0) -> float:
    """
    Berechnet die Länge der durchhängenden Leitung.

    Formel:
    l = 2a * sinh(w / (2a))

    Parameter:
        a -> Krümmungsradius
        w -> Abstand zwischen den Masten

    Rückgabe:
        Länge der Leitung
    """
    return 2 * a * math.sinh(w / (2 * a))


def aufgabe_9() -> None:
    """
    Führt Aufgabe 9 vollständig aus.
    """

    # Sinnvolles Startintervall für den Krümmungsradius a
    # f(100) ist positiv, f(200) ist negativ
    start_a = 100.0
    start_b = 200.0

    # Krümmungsradius mit Bisektion berechnen
    radius, iterationen = bisektion(
        funktion_a,
        start_a,
        start_b,
        epsilon=1e-8
    )

    # Leitungslänge mit berechnetem Radius bestimmen
    laenge = berechne_leitungslaenge(radius)

    # Ergebnisse ausgeben
    print("-" * 50)
    print("Aufgabe 9 – Leitungslänge")
    print(f"Intervall für a        : [{start_a}, {start_b}]")
    print(f"Krümmungsradius a      : {radius:.10f} m")
    print(f"Iterationsschritte     : {iterationen}")
    print(f"Länge der Leitung l    : {laenge:.10f} m")


if __name__ == "__main__":
    aufgabe_9()