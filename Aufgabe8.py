"""
Aufgabe 8 – Test des Solvers am Polynom P4

Polynom:
P4(x) = 2x + x² + 3x³ - x⁴

Gesuchte Nullstelle:
x ≈ 3,4567

Gewähltes Intervall:
[3, 4]
"""

from typing import Callable


def polynom(x: float) -> float:
    """
    Berechnet den Funktionswert des Polynoms.

    Parameter:
        x -> eingesetzter x-Wert

    Rückgabe:
        Wert von P4(x)
    """
    return 2 * x + x**2 + 3 * x**3 - x**4


def bisektion(
    func: Callable[[float], float],
    a: float,
    b: float,
    epsilon: float,
    max_iter: int = 1000
) -> tuple[float, int]:
    """
    Berechnet eine Nullstelle mit dem Bisektionsverfahren.

    Parameter:
        func     -> Funktion
        a        -> linke Intervallgrenze
        b        -> rechte Intervallgrenze
        epsilon  -> gewünschte Genauigkeit
        max_iter -> maximale Iterationen

    Rückgabe:
        (Nullstelle, Anzahl Iterationen)
    """

    try:
        # Funktionswerte an den Intervallgrenzen
        fa = func(a)
        fb = func(b)

        # Prüfen ob Vorzeichenwechsel vorliegt
        if fa * fb >= 0:
            raise ValueError(
                "Ungültiges Intervall! "
                "f(a) und f(b) müssen "
                "unterschiedliche Vorzeichen haben."
            )

        iteration = 0

        # Solange Intervall größer als epsilon ist
        while abs(b - a) > epsilon and iteration < max_iter:

            # Mittelpunkt berechnen
            c = (a + b) / 2

            # Funktionswert an der Mitte
            fc = func(c)

            # Wenn Nullstelle gefunden
            if abs(fc) < epsilon:
                return c, iteration + 1

            # Linke Hälfte verwenden
            if fa * fc < 0:
                b = c
                fb = fc

            # Rechte Hälfte verwenden
            else:
                a = c
                fa = fc

            iteration += 1

        # Näherungswert zurückgeben
        return (a + b) / 2, iteration

    except Exception as error:
        print("Fehler:", error)
        return 0.0, 0


def test_polynom(epsilon: float) -> None:
    """
    Führt einen Test mit gegebener Genauigkeit durch.
    """

    # Geeignetes Intervall laut Aufgabe
    a = 3.0
    b = 4.0

    # Solver starten
    nullstelle, schritte = bisektion(
        polynom,
        a,
        b,
        epsilon
    )

    # Ergebnisse ausgeben
    print("-" * 45)
    print(f"Genauigkeit epsilon : {epsilon}")
    print(f"Intervall           : [{a}, {b}]")
    print(f"Nullstelle          : {nullstelle:.10f}")
    print(f"P4(x)               : {polynom(nullstelle):.10e}")
    print(f"Iterationsschritte  : {schritte}")


if __name__ == "__main__":

    # Test mit Genauigkeit 10^-2
    test_polynom(1e-2)

    # Test mit Genauigkeit 10^-8
    test_polynom(1e-8)