"""Aufgabe 9 – Leitungslänge dynamisch berechnen"""

# -------------------------------------------------
# Importe
# -------------------------------------------------

import math
from typing import Callable


# -------------------------------------------------
# Nullstellenfunktion für den Krümmungsradius
# -------------------------------------------------

def funktion_a(
    a: float,
    halbe_spannweite: float,
    durchhang: float
) -> float:
    """
    Berechnet die Nullstellenfunktion für den Krümmungsradius a.

    Grundlage ist die Kettenliniengleichung:

        y(x) = a * cosh(x / a) - a + y0

    Für die Randbedingung gilt:

        y(w / 2) = y0 + durchhang

    Daraus entsteht die Gleichung:

        a * (cosh((w / 2) / a) - 1) - durchhang = 0

    Die Nullstelle dieser Funktion ist der gesuchte Krümmungsradius.

    :param a: Krümmungsradius
    :param halbe_spannweite: halber Abstand zwischen den Masten
    :param durchhang: Durchhang in der Mitte
    :return: Funktionswert
    """
    return a * (math.cosh(halbe_spannweite / a) - 1) - durchhang


# -------------------------------------------------
# Bisektionsverfahren
# -------------------------------------------------

def bisektion(
    func: Callable[[float], float],
    a: float,
    b: float,
    epsilon: float = 1e-8,
    max_iter: int = 1000
) -> tuple[float, int]:
    """
    Berechnet eine Nullstelle mit dem Bisektionsverfahren.

    Ablauf:
    1. Funktionswerte an den Grenzen berechnen
    2. Prüfen, ob ein Vorzeichenwechsel existiert
    3. Mittelpunkt berechnen
    4. Intervall halbieren
    5. Wiederholen bis Genauigkeit erreicht ist

    :param func: Funktion, deren Nullstelle gesucht wird
    :param a: linke Intervallgrenze
    :param b: rechte Intervallgrenze
    :param epsilon: gewünschte Genauigkeit
    :param max_iter: maximale Anzahl Iterationen
    :return: gefundene Nullstelle und Anzahl der Iterationen
    """
    try:
        # -----------------------------------------
        # Schritt 1: Funktionswerte berechnen
        # -----------------------------------------

        fa = func(a)
        fb = func(b)

        # -----------------------------------------
        # Schritt 2: Startintervall prüfen
        # -----------------------------------------

        # Für das Bisektionsverfahren muss ein Vorzeichenwechsel vorliegen.
        # Das bedeutet: f(a) und f(b) müssen unterschiedliche Vorzeichen haben.
        if fa * fb >= 0:
            raise ValueError(
                "Ungültiges Intervall! f(a) und f(b) müssen unterschiedliche Vorzeichen haben."
            )

        # -----------------------------------------
        # Schritt 3: Iteratives Verfahren
        # -----------------------------------------

        for iteration in range(1, max_iter + 1):

            # Mittelpunkt des aktuellen Intervalls berechnen
            c = (a + b) / 2

            # Funktionswert am Mittelpunkt berechnen
            fc = func(c)

            # -------------------------------------
            # Abbruchbedingung
            # -------------------------------------

            # Abbrechen, wenn der Funktionswert nahe genug bei 0 liegt
            # oder das Intervall bereits kleiner als epsilon ist.
            if abs(fc) < epsilon or abs(b - a) < epsilon:
                return c, iteration

            # -------------------------------------
            # Schritt 4: Intervall halbieren
            # -------------------------------------

            # Falls zwischen a und c ein Vorzeichenwechsel liegt,
            # befindet sich die Nullstelle im linken Teilintervall.
            if fa * fc < 0:
                b = c
                fb = fc

            # Andernfalls liegt die Nullstelle im rechten Teilintervall.
            else:
                a = c
                fa = fc

        # Falls die maximale Iterationsanzahl erreicht wurde,
        # wird der bestmögliche Näherungswert zurückgegeben.
        return (a + b) / 2, max_iter

    except Exception as error:
        # Fehlerbehandlung, z.B. bei ungültigem Intervall
        print("Fehler:", error)
        return 0.0, 0


# -------------------------------------------------
# Berechnung der Leitungslänge
# -------------------------------------------------

def berechne_leitungslaenge(
    radius: float,
    spannweite: float
) -> float:
    """
    Berechnet die Länge der durchhängenden Leitung.

    Formel:

        l = 2a * sinh(w / (2a))

    Dabei ist:
    - a der Krümmungsradius
    - w die Spannweite zwischen den Masten

    :param radius: berechneter Krümmungsradius
    :param spannweite: Abstand zwischen den Masten
    :return: Länge der Leitung
    """
    return 2 * radius * math.sinh(spannweite / (2 * radius))


# -------------------------------------------------
# Eingabefunktion
# -------------------------------------------------

def lies_float(text: str, standard: float | None = None) -> float:
    """
    Liest eine Fließkommazahl vom Benutzer ein.

    Wird keine Eingabe gemacht und ein Standardwert ist vorhanden,
    wird dieser Standardwert verwendet.

    :param text: Eingabeaufforderung
    :param standard: Standardwert
    :return: eingegebener oder standardmäßiger Wert
    """
    eingabe = input(text)

    # Leere Eingabe bedeutet: Standardwert verwenden
    if eingabe == "" and standard is not None:
        return standard

    # Eingabe in float umwandeln
    return float(eingabe)


# -------------------------------------------------
# Hauptprogramm
# -------------------------------------------------

def main() -> None:
    """
    Startpunkt des Programms.

    Das Programm:
    1. liest die benötigten Werte ein
    2. berechnet den Krümmungsradius mit Bisektion
    3. berechnet daraus die Leitungslänge
    4. gibt alle Ergebnisse aus
    """

    print("Aufgabe 9 – Leitungslänge dynamisch")

    # -----------------------------------------
    # Eingaben mit Standardwerten
    # -----------------------------------------

    spannweite = lies_float(
        "Abstand zwischen den Masten w [100]: ",
        100.0
    )

    durchhang = lies_float(
        "Durchhang in der Mitte [10]: ",
        10.0
    )

    start_a = lies_float(
        "linke Grenze für Radius a [100]: ",
        100.0
    )

    start_b = lies_float(
        "rechte Grenze für Radius b [200]: ",
        200.0
    )

    epsilon = lies_float(
        "Genauigkeit epsilon [1e-8]: ",
        1e-8
    )

    max_iter = int(
        lies_float("maximale Iterationen [1000]: ", 1000)
    )

    # -----------------------------------------
    # Vorbereitung der Berechnung
    # -----------------------------------------

    # Die Kettenlinienformel arbeitet mit der halben Spannweite.
    halbe_spannweite = spannweite / 2

    # Aus der Funktion mit mehreren Parametern wird mithilfe von lambda
    # eine Funktion mit nur einer Variablen gemacht.
    # Das ist nötig, weil die Bisektionsfunktion nur func(radius) erwartet.
    func = lambda radius: funktion_a(
        radius,
        halbe_spannweite,
        durchhang
    )

    # -----------------------------------------
    # Krümmungsradius berechnen
    # -----------------------------------------

    radius, iterationen = bisektion(
        func,
        start_a,
        start_b,
        epsilon,
        max_iter
    )

    # -----------------------------------------
    # Leitungslänge berechnen
    # -----------------------------------------

    # Nur berechnen, wenn ein gültiger Radius gefunden wurde.
    # Bei Fehler gibt bisektion den Radius 0.0 zurück.
    laenge = (
        berechne_leitungslaenge(radius, spannweite)
        if radius != 0
        else 0.0
    )

    # -----------------------------------------
    # Ausgabe
    # -----------------------------------------

    print("-" * 50)
    print("Aufgabe 9 – Leitungslänge")
    print(f"Spannweite w          : {spannweite:.10f} m")
    print(f"Durchhang             : {durchhang:.10f} m")
    print(f"Intervall für Radius  : [{start_a}, {start_b}]")
    print(f"Krümmungsradius a     : {radius:.10f} m")
    print(f"Iterationsschritte    : {iterationen}")
    print(f"Länge der Leitung l   : {laenge:.10f} m")


# -------------------------------------------------
# Programmstart
# -------------------------------------------------

if __name__ == "__main__":
    main()