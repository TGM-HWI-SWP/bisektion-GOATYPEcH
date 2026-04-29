#Solver zur Nullstellenbestimmung mit Bisektionsverfahren

from math import sqrt   #Importieren der Quadratwurzel-Funktion aus dem math-Modul


class Solver:   #Definieren einer Klasse namens Solver, die Methoden zur Nullstellenbestimmung mit dem Bisektionsverfahren enthält
    
    def __init__(self, funktion: str):  #Definieren des Konstruktors der Klasse, der eine Funktion als String entgegennimmt und speichert
        """
        Konstruktor

        :param funktion: Funktion als String, z.B. "x**2 - n"
        """
        self.funktion = funktion

    def f(self, x: float, n: float) -> float:   #Definieren einer Methode f, die den Funktionswert für gegebene Werte von x und n berechnet, indem sie den gespeicherten Funktionsstring auswertet
        """
        Berechnet Funktionswert

        :param x: Variable x
        :param n: Parameter n
        :return: Ergebnis
        """
        return eval(self.funktion)  #Auswerten des Funktionsstrings mit den aktuellen Werten von x und n, um den Funktionswert zu berechnen

    def bisektion(  #Definieren der Methode bisektion, die das Bisektionsverfahren zur Nullstellenbestimmung implementiert und die Nullstelle sowie die Anzahl der Iterationen zurückgibt
        self,
        a: float,   #Definieren der Parameter a und b als die Grenzen des Intervalls, in dem die Nullstelle gesucht wird, sowie n als den Parameter der Funktion, tol als die gewünschte Genauigkeit und max_iter als die maximale Anzahl der Iterationen
        b: float,   #Definieren der Parameter a und b als die Grenzen des Intervalls, in dem die Nullstelle gesucht wird, sowie n als den Parameter der Funktion, tol als die gewünschte Genauigkeit und max_iter als die maximale Anzahl der Iterationen
        n: float,   #Definieren der Parameter a und b als die Grenzen des Intervalls, in dem die Nullstelle gesucht wird, sowie n als den Parameter der Funktion, tol als die gewünschte Genauigkeit und max_iter als die maximale Anzahl der Iterationen
        tol: float = 1e-10, #Definieren der Standardwerte für tol als 1e-10 und max_iter als 100, die verwendet werden, wenn keine spezifischen Werte bei der Aufrufung der Methode angegeben werden
        max_iter: int = 100 #Definieren der Standardwerte für tol als 1e-10 und max_iter als 100, die verwendet werden, wenn keine spezifischen Werte bei der Aufrufung der Methode angegeben werden
    ) -> tuple: #Definieren des Rückgabetyps der Methode als Tuple, das die Nullstelle und die Anzahl der Iterationen enthält
        """
        Bisektionsverfahren

        :param a: linke Grenze
        :param b: rechte Grenze
        :param n: Parameter n
        :param tol: Genauigkeit
        :param max_iter: maximale Iterationen
        :return: Nullstelle, Iterationen
        """

        try:
            if self.f(a, n) * self.f(b, n) > 0: #Überprüfen, ob die Funktion an den Grenzen a und b das gleiche Vorzeichen hat, was bedeutet, dass keine Nullstelle im Intervall [a, b] liegt. Wenn dies der Fall ist, wird eine ValueError-Ausnahme ausgelöst, um anzuzeigen, dass kein gültiges Startintervall vorliegt.
                raise ValueError(   #Auslösen einer ValueError-Ausnahme mit einer entsprechenden Fehlermeldung, wenn die Funktion an den Grenzen a und b das gleiche Vorzeichen hat, was bedeutet, dass keine Nullstelle im Intervall [a, b] liegt
                    "Kein gültiges Startintervall! "
                    "f(a) und f(b) haben gleiches Vorzeichen."
                )

            for i in range(max_iter):   #Durchführen der Iterationen des Bisektionsverfahrens, wobei i die aktuelle Iterationsnummer ist, die von 0 bis max_iter - 1 läuft
                c = (a + b) / 2 #Berechnen des Mittelpunkts c des Intervalls [a, b], der als neue Näherung für die Nullstelle verwendet wird

                if abs(self.f(c, n)) < tol: #Überprüfen, ob der Funktionswert an der Stelle c kleiner als die gewünschte Genauigkeit tol ist, was bedeutet, dass c eine ausreichend genaue Näherung für die Nullstelle ist. Wenn dies der Fall ist, wird c zusammen mit der Anzahl der Iterationen (i + 1) zurückgegeben.
                    return c, i + 1 #Zurückgeben der Nullstelle c und der Anzahl der Iterationen (i + 1), wenn der Funktionswert an der Stelle c kleiner als die gewünschte Genauigkeit tol ist, was bedeutet, dass c eine ausreichend genaue Näherung für die Nullstelle ist

                if self.f(a, n) * self.f(c, n) < 0: #Überprüfen, ob die Funktion an den Punkten a und c unterschiedliche Vorzeichen hat, was bedeutet, dass die Nullstelle im Intervall [a, c] liegt. Wenn dies der Fall ist, wird b auf c gesetzt, um das Intervall zu verkleinern und die Suche nach der Nullstelle fortzusetzen.
                    b = c   
                else:
                    a = c

            return c, max_iter  #Wenn die maximale Anzahl der Iterationen erreicht ist, wird die letzte Näherung c zusammen mit der maximalen Anzahl der Iterationen zurückgegeben, um anzuzeigen, dass die Suche nach der Nullstelle nicht innerhalb der gewünschten Genauigkeit tol abgeschlossen werden konnte.

        except Exception as error:  #Abfangen von allgemeinen Ausnahmen, die während der Ausführung des Bisektionsverfahrens auftreten können, und Ausgabe einer entsprechenden Fehlermeldung. In diesem Fall wird None und 0 zurückgegeben, um anzuzeigen, dass die Nullstellenbestimmung nicht erfolgreich war.
            print("Fehler:", error) #Ausgeben der Fehlermeldung, wenn eine Ausnahme auftritt, die während der Ausführung des Bisektionsverfahrens abgefangen wird
            return None, 0


def test_solver():  #Definieren einer Testfunktion, die den Solver mit verschiedenen n-Werten testet und die Ergebnisse ausgibt
    """
    Test mit n = 25, 81, 144
    """

    solver = Solver("x**2 - n") #Erstellen einer Instanz der Solver-Klasse mit der Funktion "x**2 - n", die die Nullstelle für die Quadratwurzel von n berechnet

    werte = [25, 81, 144]   #Definieren einer Liste von n-Werten, die für die Tests verwendet werden, in diesem Fall 25, 81 und 144, um die Quadratwurzeln dieser Werte zu berechnen und mit den analytischen Lösungen zu vergleichen

    for n in werte: #Durchlaufen der Liste der n-Werte, um den Solver für jeden Wert zu testen und die Ergebnisse auszugeben
        print("-" * 50)
        print(f"Test für n = {n}")  #Ausgeben einer Trennlinie und einer Überschrift für den Test mit dem aktuellen n-Wert, um die Ergebnisse für jeden Test klar zu kennzeichnen

        # Intervall aus deiner PDF:
        # Start bei 0 bis n
        a = 0
        b = n

        numerisch, iterationen = solver.bisektion(a, b, n)  #Aufrufen der bisektion-Methode des Solvers mit den Grenzen a und b sowie dem aktuellen n-Wert, um die numerische Näherung der Nullstelle (Quadratwurzel von n) und die Anzahl der Iterationen zu erhalten
        analytisch = sqrt(n)    #Berechnen der analytischen Lösung für die Quadratwurzel von n mit der sqrt-Funktion aus dem math-Modul, um die numerische Näherung mit der exakten Lösung zu vergleichen

        print(f"Numerische Lösung : {numerisch:.10f}")  #Ausgeben der numerischen Lösung mit 10 Dezimalstellen, um die Genauigkeit der Näherung zu zeigen
        print(f"Analytische Lösung: {analytisch:.10f}") #Ausgeben der analytischen Lösung mit 10 Dezimalstellen, um die exakte Quadratwurzel von n zu zeigen
        print(f"Abweichung        : {abs(numerisch - analytisch):.10f}")    #Ausgeben der Abweichung zwischen der numerischen Lösung und der analytischen Lösung mit 10 Dezimalstellen, um die Genauigkeit der Näherung zu quantifizieren
        print(f"Iterationen       : {iterationen}") #Ausgeben der Anzahl der Iterationen, die für die Berechnung der Nullstelle benötigt wurden, um die Effizienz des Bisektionsverfahrens zu zeigen


if __name__ == "__main__":
    test_solver()