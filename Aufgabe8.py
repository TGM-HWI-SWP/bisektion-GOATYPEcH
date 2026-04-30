"""Aufgabe 8 – Polynom P4 dynamisch testen"""

# -------------------------------------------------
# Import
# -------------------------------------------------

from typing import Callable


# -------------------------------------------------
# Polynomdefinition
# -------------------------------------------------

def polynom(x: float) -> float:
    """
    Definiert das gegebene Polynom:

        P4(x) = 2x + x² + 3x³ - x⁴

    Ziel:
    → Nullstelle im Intervall [3, 4] finden

    :param x: Eingabewert
    :return: Funktionswert
    """
    return 2 * x + x**2 + 3 * x**3 - x**4


# -------------------------------------------------
# Bisektionsverfahren
# -------------------------------------------------

def bisektion(
    func: Callable[[float], float],
    a: float,
    b: float,
    epsilon: float,
    max_iter: int = 1000
) -> tuple[float, int]:
    """
    Berechnet eine Nullstelle mit dem Bisektionsverfahren.

    Ablauf:
    1. Intervall prüfen (Vorzeichenwechsel)
    2. Intervall halbieren
    3. Teilintervall mit Nullstelle auswählen
    4. Wiederholen bis Genauigkeit erreicht

    :param func: zu untersuchende Funktion
    :param a: linke Intervallgrenze
    :param b: rechte Intervallgrenze
    :param epsilon: gewünschte Genauigkeit
    :param max_iter: maximale Iterationen
    :return: (Nullstelle, Iterationen)
    """
    try:
        # -----------------------------------------
        # Schritt 1: Funktionswerte an Grenzen
        # -----------------------------------------
        fa = func(a)
        fb = func(b)

        # Prüfen auf Vorzeichenwechsel
        if fa * fb >= 0:
            raise ValueError(
                "Ungültiges Intervall! f(a) und f(b) müssen unterschiedliche Vorzeichen haben."
            )

        # -----------------------------------------
        # Schritt 2: Iteration starten
        # -----------------------------------------
        for iteration in range(1, max_iter + 1):

            # Mittelpunkt berechnen
            c = (a + b) / 2

            # Funktionswert im Mittelpunkt
            fc = func(c)

            # -------------------------------------
            # Abbruchbedingung:
            # - Funktionswert nahe 0
            # - Intervall sehr klein
            # -------------------------------------
            if abs(fc) < epsilon or abs(b - a) < epsilon:
                return c, iteration

            # -------------------------------------
            # Schritt 3: Intervall halbieren
            # -------------------------------------

            # Vorzeichenwechsel links → Nullstelle links
            if fa * fc < 0:
                b = c
                fb = fc

            # sonst rechts
            else:
                a = c
                fa = fc

        # -----------------------------------------
        # Falls max_iter erreicht
        # -----------------------------------------
        return (a + b) / 2, max_iter

    except Exception as error:
        # Fehlerbehandlung
        print("Fehler:", error)
        return 0.0, 0


# -------------------------------------------------
# Eingabefunktion
# -------------------------------------------------

def lies_float(text: str, standard: float | None = None) -> float:
    """
    Liest eine Fließkommazahl vom Benutzer ein.

    Vorteil:
    → Standardwerte möglich (einfach Enter drücken)

    :param text: Eingabeaufforderung
    :param standard: Standardwert
    :return: eingegebener Wert
    """
    eingabe = input(text)

    if eingabe == "" and standard is not None:
        return standard

    return float(eingabe)


# -------------------------------------------------
# Hauptprogramm
# -------------------------------------------------

def main() -> None:
    """
    Startpunkt des Programms.

    Liest Eingaben ein und führt die Nullstellenberechnung aus.
    """

    print("Aufgabe 8 – P4 dynamisch")

    # -----------------------------------------
    # Eingaben (mit sinnvollen Standardwerten)
    # -----------------------------------------

    a = lies_float("linke Grenze a [3]: ", 3.0)
    b = lies_float("rechte Grenze b [4]: ", 4.0)
    epsilon = lies_float("Genauigkeit epsilon [1e-8]: ", 1e-8)
    max_iter = int(lies_float("maximale Iterationen [1000]: ", 1000))

    # -----------------------------------------
    # Berechnung starten
    # -----------------------------------------

    nullstelle, schritte = bisektion(
        polynom, a, b, epsilon, max_iter
    )

    # -----------------------------------------
    # Ausgabe
    # -----------------------------------------

    print("-" * 45)
    print(f"Intervall          : [{a}, {b}]")
    print(f"Genauigkeit        : {epsilon}")
    print(f"Nullstelle         : {nullstelle:.10f}")

    # Funktionswert an der gefundenen Stelle (Qualitätscheck)
    print(f"P4(x)              : {polynom(nullstelle):.10e}")

    print(f"Iterationsschritte : {schritte}")


# -------------------------------------------------
# Programmstart
# -------------------------------------------------

if __name__ == "__main__":
    main()