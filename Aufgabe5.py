# Aufgabe 5 – Dynamische Nullstellenbestimmung mit Bisektionsverfahren

from math import sqrt


class Solver:
    """
    Klasse zur Nullstellenbestimmung mit dem Bisektionsverfahren.
    Die Funktion wird als String übergeben und dynamisch ausgewertet.
    """

    def __init__(self, funktion: str):
        """
        Konstruktor speichert die Funktion als String.

        :param funktion: Funktion als String, z.B. "x**2 - n"
        """
        self.funktion = funktion

    def f(self, x: float, n: float) -> float:
        """
        Berechnet den Funktionswert f(x).

        :param x: aktuelle Stelle
        :param n: Parameter der Funktion
        :return: Funktionswert
        """
        # eval wertet den String als mathematischen Ausdruck aus
        # __builtins__ wird deaktiviert → Sicherheit
        return eval(self.funktion, {"__builtins__": {}}, {"x": x, "n": n})

    def bisektion(
        self,
        a: float,
        b: float,
        n: float,
        tol: float = 1e-10,
        max_iter: int = 100
    ) -> tuple[float | None, int]:
        """
        Führt das Bisektionsverfahren zur Nullstellenbestimmung aus.

        :param a: linke Intervallgrenze
        :param b: rechte Intervallgrenze
        :param n: Parameter der Funktion
        :param tol: gewünschte Genauigkeit
        :param max_iter: maximale Anzahl Iterationen
        :return: (Nullstelle, Iterationen)
        """
        try:
            # Funktionswerte an den Grenzen berechnen
            fa = self.f(a, n)
            fb = self.f(b, n)

            # Prüfen, ob ein Vorzeichenwechsel vorliegt
            if fa * fb > 0:
                raise ValueError(
                    "Kein gültiges Startintervall! "
                    "f(a) und f(b) haben gleiches Vorzeichen."
                )

            # Iterative Intervallhalbierung
            for i in range(max_iter):

                # Mittelpunkt berechnen
                c = (a + b) / 2
                fc = self.f(c, n)

                # Abbruch, wenn Genauigkeit erreicht
                if abs(fc) < tol:
                    return c, i + 1

                # Intervall halbieren (Vorzeichenwechsel prüfen)
                if fa * fc < 0:
                    b = c
                    fb = fc
                else:
                    a = c
                    fa = fc

            # Falls max_iter erreicht → bestmögliche Näherung zurückgeben
            return (a + b) / 2, max_iter

        except Exception as error:
            # Fehlerbehandlung
            print("Fehler:", error)
            return None, 0


def lies_float(text: str, standard: float | None = None) -> float:
    """
    Liest eine Fließkommazahl von der Konsole ein.

    :param text: Eingabeaufforderung
    :param standard: Standardwert bei leerer Eingabe
    :return: eingegebener Wert
    """
    eingabe = input(text)

    # Falls nichts eingegeben wird → Standardwert verwenden
    if eingabe == "" and standard is not None:
        return standard

    return float(eingabe)


def main() -> None:
    """
    Hauptfunktion: liest Eingaben ein und startet den Solver.
    """
    print("Aufgabe 5 – Bisektionsverfahren dynamisch")

    # Funktion dynamisch eingeben
    funktion = input("Funktion eingeben [x**2 - n]: ") or "x**2 - n"

    # Parameter einlesen
    n = lies_float("n eingeben: ")
    a = lies_float("linke Grenze a [0]: ", 0.0)
    b = lies_float(f"rechte Grenze b [{n}]: ", n)
    tol = lies_float("Genauigkeit tol [1e-10]: ", 1e-10)
    max_iter = int(lies_float("maximale Iterationen [100]: ", 100))

    # Solver erstellen
    solver = Solver(funktion)

    # Nullstelle berechnen
    numerisch, iterationen = solver.bisektion(a, b, n, tol, max_iter)

    # Ausgabe
    print("-" * 50)
    print(f"Funktion           : {funktion}")
    print(f"n                  : {n}")
    print(f"Intervall          : [{a}, {b}]")

    if numerisch is not None:
        print(f"Numerische Lösung  : {numerisch:.10f}")

        # Spezialfall: Vergleich mit analytischer Lösung
        if funktion.replace(" ", "") == "x**2-n" and n >= 0:
            analytisch = sqrt(n)
            print(f"Analytische Lösung : {analytisch:.10f}")
            print(f"Abweichung         : {abs(numerisch - analytisch):.10e}")

        print(f"Iterationen        : {iterationen}")


if __name__ == "__main__":
    main()