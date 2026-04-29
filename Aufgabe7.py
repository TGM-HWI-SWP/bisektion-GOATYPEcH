#Aufgabe 7

from __future__ import annotation

import math
from dataclasses import dataclass
from typing import Callable

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pylot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

anim = None #Global speicher


@dataclass
class IterationData:
    interation: int
    a: float
    b: float
    c: float
    fc: float

def funktion(x: float, n: float) -> float:
    return x**2 -n

def bisektion_history(
    func: Callable[[float, float], float],
    a: float,
    b: float,
    n: float,
    epsilon: float = 1e-8
) ->list[IterationData]:

    history = []

    while True:
        c = (a + b) /2
        fc = func(c, n)

        history.append(
            InterationData(len(history) + 1, a, b, c, fc )
        )

        if abs(fc) < epsilon:
            break

        if func(a, n) * fc < 0:
            b = c
        else:
            a =c

        return history

def animate_solver(
    history: list[InterationData],
    n: float
) -> None:

    global anim

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (10, 8))

    x = np.linspace(0, 28, 500)
    y = [funktion(i, n) for i in x]

    echte_loesung = math.sqrt(n)

    def update(frame):

        daten = history[frame]

        ax1.clear()
        ax2.clear()

        #Diagramm
        ax1.plot(x, y)
        ax1.axhline(0)
        ax1.axvline(daten.a, linestyle="--")
        ax1.axvline(daten.b, linestyle="--")
        ax1.plot(daten.c, daten.fc, "ro")

        ax1.set_title(
            f"Interation {daten.Interationen}"
        )

        #Diagramm 2
        interationen = [d.interationen for d in history[:frame + 1]]
        werte = [d.c for d in history[:frame + 1]]

        ax2.plot(interationen, werte, marker="0")
        ax2.axhline(echte_loesung, linestyle=":")

        ax2.set_title("Annäherung")

        plt.thight_layout()

    anim = FuncAnimation(
        fig,
        update,
        frames=len(history),
        interval=1000,
        repeat=False
    )

    plt.show()

def plotter():
    
    daten = bisektion_history(
        funktion,
        0,
        28,
        25
    )

    animate_solver(daten, 25)

if __name__ == "__main__":
    plotter()