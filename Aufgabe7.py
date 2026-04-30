"""Aufgabe 7 – Dynamische grafische Darstellung der Nullstellenfindung"""

from __future__ import annotations

# -------------------------------------------------
# Importe
# -------------------------------------------------

import math
from dataclasses import dataclass
from typing import Callable

import matplotlib

# Wichtig: Backend setzen, damit Fenster korrekt geöffnet wird
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


# -------------------------------------------------
# Globale Variable
# -------------------------------------------------

# Wird benötigt, damit matplotlib die Animation nicht
# automatisch aus dem Speicher löscht
anim = None


# -------------------------------------------------
# Datenstruktur für Iterationen
# -------------------------------------------------

@dataclass
class IterationData:
    """
    Diese Klasse speichert alle relevanten Werte
    einer einzelnen Iteration des Bisektionsverfahrens.
    """

    iteration: int   # Nummer der Iteration
    a: float         # linke Intervallgrenze
    b: float         # rechte Intervallgrenze
    c: float         # Mittelpunkt des Intervalls
    fc: float        # Funktionswert an c


# -------------------------------------------------
# Beispiel-Funktion
# -------------------------------------------------

def funktion(x: float, n: float) -> float:
    """
    Beispiel-Funktion:

        f(x) = x² - n

    Die Nullstelle entspricht sqrt(n).

    :param x: Variable
    :param n: Parameter
    :return: Funktionswert
    """
    return x**2 - n


# -------------------------------------------------
# Bisektionsverfahren mit Speicherung
# -------------------------------------------------

def bisektion_history(
    func: Callable[[float, float], float],
    a: float,
    b: float,
    n: float,
    epsilon: float = 1e-8,
    max_iter: int = 1000
) -> list[IterationData]:
    """
    Führt das Bisektionsverfahren aus und speichert
    jeden einzelnen Iterationsschritt.

    Vorteil:
    → spätere Visualisierung möglich

    :param func: zu untersuchende Funktion
    :param a: linke Intervallgrenze
    :param b: rechte Intervallgrenze
    :param n: Parameter
    :param epsilon: gewünschte Genauigkeit
    :param max_iter: maximale Iterationen
    :return: Liste aller Iterationen
    """

    # Liste zur Speicherung aller Schritte
    history: list[IterationData] = []

    # Funktionswerte an den Intervallgrenzen berechnen
    fa = func(a, n)
    fb = func(b, n)

    # Prüfen, ob ein Vorzeichenwechsel vorliegt
    # → Voraussetzung für Bisektion!
    if fa * fb >= 0:
        raise ValueError(
            "Ungültiges Intervall: f(a) und f(b) brauchen unterschiedliche Vorzeichen."
        )

    # Iteratives Verfahren
    for iteration in range(1, max_iter + 1):

        # -----------------------------------------
        # Schritt 1: Mittelpunkt berechnen
        # -----------------------------------------
        c = (a + b) / 2

        # Funktionswert am Mittelpunkt
        fc = func(c, n)

        # -----------------------------------------
        # Schritt 2: Werte speichern
        # -----------------------------------------
        history.append(
            IterationData(iteration, a, b, c, fc)
        )

        # -----------------------------------------
        # Schritt 3: Abbruchbedingung prüfen
        # -----------------------------------------
        if abs(fc) < epsilon:
            # gewünschte Genauigkeit erreicht
            break

        # -----------------------------------------
        # Schritt 4: Intervall halbieren
        # -----------------------------------------

        # Falls Vorzeichenwechsel links → Nullstelle liegt links
        if fa * fc < 0:
            b = c
            fb = fc

        # Sonst rechts
        else:
            a = c
            fa = fc

    return history


# -------------------------------------------------
# Animation
# -------------------------------------------------

def animate_solver(
    history: list[IterationData],
    n: float,
    x_min: float,
    x_max: float
) -> None:
    """
    Erstellt eine Animation des Lösungsprozesses.

    Darstellung:
    1. Funktionsgraph + aktuelles Intervall
    2. Annäherung der Lösung über Iterationen

    :param history: gespeicherte Iterationen
    :param n: Parameter
    :param x_min: minimale x-Achse
    :param x_max: maximale x-Achse
    """

    global anim

    # Zwei Diagramme (oben: Funktion, unten: Verlauf)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # x-Werte für Graph
    x = np.linspace(x_min, x_max, 500)

    # y-Werte berechnen
    y = [funktion(i, n) for i in x]

    # Analytische Lösung (falls möglich)
    echte_loesung = math.sqrt(n) if n >= 0 else None

    # -------------------------------------------------
    # Update-Funktion (wird für jedes Frame aufgerufen)
    # -------------------------------------------------

    def update(frame: int) -> None:

        # Aktuelle Iteration holen
        daten = history[frame]

        # Diagramme leeren
        ax1.clear()
        ax2.clear()

        # =============================================
        # Diagramm 1: Funktion + Intervall
        # =============================================

        # Funktionsgraph zeichnen
        ax1.plot(x, y)

        # x-Achse (y=0)
        ax1.axhline(0)

        # Intervallgrenzen anzeigen
        ax1.axvline(daten.a, linestyle="--")
        ax1.axvline(daten.b, linestyle="--")

        # aktueller Punkt c
        ax1.plot(daten.c, daten.fc, "ro")

        ax1.set_title(
            f"Iteration {daten.iteration}, c = {daten.c:.10f}"
        )

        # =============================================
        # Diagramm 2: Konvergenz
        # =============================================

        # bisherige Iterationen
        iterationen = [d.iteration for d in history[:frame + 1]]

        # bisherige Näherungen
        werte = [d.c for d in history[:frame + 1]]

        # Plot der Annäherung
        ax2.plot(iterationen, werte, marker="o")

        # exakte Lösung als Referenz
        if echte_loesung is not None:
            ax2.axhline(echte_loesung, linestyle=":")

        ax2.set_title("Annäherung an die Lösung")

        # Layout optimieren
        plt.tight_layout()

    # -------------------------------------------------
    # Animation starten
    # -------------------------------------------------

    anim = FuncAnimation(
        fig,
        update,
        frames=len(history),
        interval=1000,
        repeat=False
    )

    # Fenster anzeigen
    plt.show()


# -------------------------------------------------
# Hilfsfunktion für Eingaben
# -------------------------------------------------

def lies_float(text: str, standard: float | None = None) -> float:
    """
    Liest eine Fließkommazahl vom Benutzer ein.

    Vorteil:
    → Standardwerte möglich

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
    Liest Eingaben und startet die Animation.
    """

    print("Aufgabe 7 – Animation dynamisch")

    # Eingaben (mit Defaults)
    n = lies_float("n eingeben [25]: ", 25.0)
    a = lies_float("linke Grenze a [0]: ", 0.0)
    b = lies_float("rechte Grenze b [28]: ", 28.0)
    epsilon = lies_float("Genauigkeit epsilon [1e-8]: ", 1e-8)
    max_iter = int(lies_float("maximale Iterationen [1000]: ", 1000))

    # Berechnung der Iterationen
    daten = bisektion_history(
        funktion, a, b, n, epsilon, max_iter
    )

    # Animation starten
    animate_solver(daten, n, min(a, b), max(a, b))


# -------------------------------------------------
# Programmstart
# -------------------------------------------------

if __name__ == "__main__":
    main()