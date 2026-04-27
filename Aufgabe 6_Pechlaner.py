"""
Aufgabe 6 – Alternative Lösung mit Regula Falsi
SWP Projekt

Erfüllt:
- alternatives Verfahren zu Aufgabe 5
- dynamische Funktion
- Tests mit n = 25, 81, 144
- Fehlerbehandlung
- Funktionen, Kommentare, Typehinting
- PEP8-konforme Struktur
"""

from math import sqrt
from typing import Callable


def funktion(x: float, n: float) -> float:
    """
    Nullstellenfunktion aus Aufgabe 1.
    Gesucht ist die Lösung von x² - n = 0.
    """
    return x**2 - n


def regula_falsi(
    func: Callable[[float, float], float],
    a: float,
    b: float,
    n: float,
    epsilon: float = 1e-8,
    max_iter: int = 1000
) -> tuple[float, int]:
    """
    Berechnet eine Nullstelle mit dem Regula-Falsi-Verfahren.

    Parameter:
        func: Zu untersuchende Funktion
        a: linke Intervallgrenze
        b: rechte Intervallgrenze
        n: Parameter der Funktion
        epsilon: gewünschte Genauigkeit
        max_iter: maximale Anzahl der Iterationen

    Rückgabe:
        tuple aus (Näherung der Nullstelle, Anzahl Iterationen)
    """
    try:
        fa = func(a, n)
        fb = func(b, n)

        if fa * fb >= 0:
            raise ValueError(
                "Ungültiges Intervall: f(a) und f(b) müssen "
                "unterschiedliche Vorzeichen haben."
            )

        c = a
        iteration = 0

        while iteration < max_iter:
            fa = func(a, n)
            fb = func(b, n)

            if fb - fa == 0:
                raise ZeroDivisionError(
                    "Division durch 0 bei der Berechnung von c."
                )

            c = b - fb * (b - a) / (fb - fa)
            fc = func(c, n)

            if abs(fc) < epsilon:
                return c, iteration + 1

            if fa * fc < 0:
                b = c
            else:
                a = c

            iteration += 1

        return c, iteration

    except ValueError as error:
        print("Fehler:", error)
        return 0.0, 0
    except ZeroDivisionError as error:
        print("Fehler:", error)
        return 0.0, 0
    except Exception as error:
        print("Unerwarteter Fehler:", error)
        return 0.0, 0


def test_solver(n: float, a: float = 0.0, b: float = 28.0) -> None:
    """
    Testet den Solver für einen gegebenen n-Wert
    mit dem Intervall [0, 28].
    """
    nullstelle, schritte = regula_falsi(funktion, a, b, n)

    print("-" * 50)
    print(f"n = {n}")
    print(f"Intervall           : [{a}, {b}]")
    print(f"Numerische Lösung   : {nullstelle:.10f}")
    print(f"Analytische Lösung  : {sqrt(n):.10f}")
    print(f"Abweichung          : {abs(nullstelle - sqrt(n)):.10e}")
    print(f"Iterationen         : {schritte}")


if __name__ == "__main__":
    test_solver(25)
    test_solver(81)
    test_solver(144)