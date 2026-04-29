"""
Aufgabe 7 – Grafische Darstellung der Nullstellenfindung

In diesem Programm wird das Bisektionsverfahren grafisch dargestellt.
Die Nullstelle der Funktion

    f(x) = x² - n

wird schrittweise berechnet und als Animation gezeigt.

Dargestellt werden:
1. Der Funktionsgraph mit aktuellem Intervall
2. Die Annäherung der Lösung je Iteration
"""

from __future__ import annotations

# -------------------------------------------------
# Importieren der benötigten Module
# -------------------------------------------------

# Für mathematische Funktionen (sqrt)
import math

# Dataclass zum Speichern der Iterationen
from dataclasses import dataclass

# Typehinting für Funktionen
from typing import Callable

# matplotlib Backend einstellen
# nötig damit Fenster richtig geöffnet wird
import matplotlib
matplotlib.use("TkAgg")

# Diagramme erstellen
import matplotlib.pyplot as plt

# Für Zahlenbereiche / Arrays
import numpy as np

# Für Animationen
from matplotlib.animation import FuncAnimation


# -------------------------------------------------
# Globale Variable
# -------------------------------------------------

# Wird benötigt, damit matplotlib die Animation
# nicht automatisch löscht
anim = None


# -------------------------------------------------
# Dataclass für Iterationsdaten
# -------------------------------------------------

@dataclass
class IterationData:
    """
    Speichert alle Werte eines Schrittes.
    """

    # Nummer der Iteration
    iteration: int

    # Linke Intervallgrenze
    a: float

    # Rechte Intervallgrenze
    b: float

    # Mittelpunkt
    c: float

    # Funktionswert an c
    fc: float


# -------------------------------------------------
# Funktion aus Aufgabe 1
# -------------------------------------------------

def funktion(x: float, n: float) -> float:
    """
    Berechnet:

        f(x) = x² - n

    Nullstelle entspricht sqrt(n)
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
    epsilon: float = 1e-8
) -> list[IterationData]:
    """
    Führt das Bisektionsverfahren aus.

    Jeder Schritt wird gespeichert,
    damit später eine Animation möglich ist.
    """

    # Liste für alle Iterationen
    history = []

    while True:

        # Mittelpunkt des aktuellen Intervalls
        c = (a + b) / 2

        # Funktionswert im Mittelpunkt
        fc = func(c, n)

        # Werte speichern
        history.append(
            IterationData(
                len(history) + 1,   # Iterationsnummer
                a,                  # linke Grenze
                b,                  # rechte Grenze
                c,                  # Mittelpunkt
                fc                  # Funktionswert
            )
        )

        # Prüfen ob Lösung genau genug
        if abs(fc) < epsilon:
            break

        # Prüfen in welcher Hälfte
        # die Nullstelle liegt

        # Wenn Vorzeichenwechsel links
        if func(a, n) * fc < 0:
            b = c

        # Sonst rechts
        else:
            a = c

    # Alle Schritte zurückgeben
    return history


# -------------------------------------------------
# Animation
# -------------------------------------------------

def animate_solver(
    history: list[IterationData],
    n: float
) -> None:
    """
    Erstellt die grafische Animation.
    """

    global anim

    # Zwei Diagramme erzeugen
    fig, (ax1, ax2) = plt.subplots(
        2,              # 2 Zeilen
        1,              # 1 Spalte
        figsize=(10, 8)
    )

    # x-Werte für den Graphen
    x = np.linspace(0, 28, 500)

    # y-Werte berechnen
    y = [funktion(i, n) for i in x]

    # Exakte Lösung berechnen
    echte_loesung = math.sqrt(n)

    # ---------------------------------------------
    # Wird pro Frame aufgerufen
    # ---------------------------------------------
    def update(frame):

        # Aktuelle Daten holen
        daten = history[frame]

        # Diagramme leeren
        ax1.clear()
        ax2.clear()

        # =========================================
        # Diagramm 1
        # Funktion + Intervall
        # =========================================

        # Funktion zeichnen
        ax1.plot(x, y)

        # x-Achse
        ax1.axhline(0)

        # Linke Grenze
        ax1.axvline(
            daten.a,
            linestyle="--"
        )

        # Rechte Grenze
        ax1.axvline(
            daten.b,
            linestyle="--"
        )

        # Aktueller Mittelpunkt
        ax1.plot(
            daten.c,
            daten.fc,
            "ro"
        )

        # Titel
        ax1.set_title(
            f"Iteration {daten.iteration}"
        )

        # =========================================
        # Diagramm 2
        # Annäherung an Lösung
        # =========================================

        # Bisherige Iterationen
        iterationen = [
            d.iteration
            for d in history[:frame + 1]
        ]

        # Alle bisherigen c-Werte
        werte = [
            d.c
            for d in history[:frame + 1]
        ]

        # Linie zeichnen
        ax2.plot(
            iterationen,
            werte,
            marker="o"
        )

        # Exakte Lösung anzeigen
        ax2.axhline(
            echte_loesung,
            linestyle=":"
        )

        # Titel
        ax2.set_title(
            "Annäherung an die Lösung"
        )

        # Layout schöner machen
        plt.tight_layout()

    # ---------------------------------------------
    # Animation starten
    # ---------------------------------------------
    anim = FuncAnimation(
        fig,                 # Fenster
        update,              # Update Funktion
        frames=len(history), # Anzahl Bilder
        interval=1000,       # 1 Sekunde
        repeat=False         # kein Wiederholen
    )

    # Fenster anzeigen
    plt.show()


# -------------------------------------------------
# Hauptfunktion
# -------------------------------------------------

def plotter() -> None:
    """
    Startet Aufgabe 7.
    """

    # Nullstelle von sqrt(25) suchen
    daten = bisektion_history(
        funktion,
        0,      # linke Grenze
        28,     # rechte Grenze
        25      # n
    )

    # Animation anzeigen
    animate_solver(
        daten,
        25
    )


# -------------------------------------------------
# Programmstart
# -------------------------------------------------

if __name__ == "__main__":
    plotter()