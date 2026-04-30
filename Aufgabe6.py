"""Aufgabe 6 – Regula Falsi dynamisch"""

from math import sqrt
from typing import Callable


def funktion(x: float, n: float) -> float:
    """
    Beispiel-Funktion zur Nullstellenbestimmung.

    Gesucht ist die Lösung von:
        f(x) = x² - n = 0

    :param x: Variable
    :param n: Parameter
    :return: Funktionswert
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

    :param func: zu untersuchende Funktion
    :param a: linke Intervallgrenze
    :param b: rechte Intervallgrenze
    :param n: Parameter der Funktion
    :param epsilon: gewünschte Genauigkeit
    :param max_iter: maximale Iterationen
    :return: (Nullstelle, Iterationen)
    """
    try:
        # Funktionswerte an Intervallgrenzen
        fa = func(a, n)
        fb = func(b, n)

        # Prüfen auf gültiges Startintervall
        if fa * fb >= 0:
            raise ValueError(
                "Ungültiges Intervall: f(a) und f(b) müssen unterschiedliche Vorzeichen haben."
            )

        c = a  # Initialisierung

        # Iteratives Verfahren
        for iteration in range(1, max_iter + 1):

            # Werte neu berechnen
            fa = func(a, n)
            fb = func(b, n)

            # Vermeidung Division durch 0
            if fb - fa == 0:
                raise ZeroDivisionError(
                    "Division durch 0 bei der Berechnung von c."
                )

            # Regula-Falsi-Formel (Sekantenmethode mit Intervallbindung)
            c = b - fb * (b - a) / (fb - fa)
            fc = func(c, n)

            # Abbruchbedingung
            if abs(fc) < epsilon:
                return c, iteration

            # Intervall anpassen
            if fa * fc < 0:
                b = c
            else:
                a = c

        # Falls maximale Iterationen erreicht
        return c, max_iter

    except Exception as error:
        # Fehlerbehandlung
        print("Fehler:", error)
        return 0.0, 0


def lies_float(text: str, standard: float | None = None) -> float:
    """
    Liest eine Fließkommazahl von der Konsole ein.

    :param text: Eingabeaufforderung
    :param standard: Standardwert bei leerer Eingabe
    :return: eingegebener Wert
    """
    eingabe = input(text)

    if eingabe == "" and standard is not None:
        return standard

    return float(eingabe)


def main() -> None:
    """
    Hauptfunktion: liest Eingaben und startet das Verfahren.
    """
    print("Aufgabe 6 – Regula Falsi dynamisch")

    # Eingaben
    n = lies_float("n eingeben: ")
    a = lies_float("linke Grenze a [0]: ", 0.0)
    b = lies_float("rechte Grenze b [28]: ", 28.0)
    epsilon = lies_float("Genauigkeit epsilon [1e-8]: ", 1e-8)
    max_iter = int(lies_float("maximale Iterationen [1000]: ", 1000))

    # Berechnung
    nullstelle, schritte = regula_falsi(
        funktion, a, b, n, epsilon, max_iter
    )

    # Ausgabe
    print("-" * 50)
    print(f"n                  : {n}")
    print(f"Intervall          : [{a}, {b}]")
    print(f"Numerische Lösung  : {nullstelle:.10f}")

    # Vergleich mit analytischer Lösung (falls möglich)
    if n >= 0:
        print(f"Analytische Lösung : {sqrt(n):.10f}")
        print(f"Abweichung         : {abs(nullstelle - sqrt(n)):.10e}")

    print(f"Iterationen        : {schritte}")


if __name__ == "__main__":
    main()