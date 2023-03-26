import time

class Nodo:
    def __init__(self, estado, profundidad, padre=None):
        self.estado = estado
        self.profundidad = profundidad
        self.padre = padre
        self.hijos = []

    def expandir(self):
        for i in range(2, len(self.estado) + 1):
            nuevo_estado = self.estado[:i][::-1] + self.estado[i:]
            nuevo_nodo = Nodo(nuevo_estado, self.profundidad + 1, self)
            self.hijos.append(nuevo_nodo)


class Grafo:
    def __init__(self, estado_inicial):
        self.estado_inicial = estado_inicial
        self.nodo_inicial = Nodo(estado_inicial, 0)
        self.nodos_visitados = set()

    def dls(self, nodo, limite_profundidad):
        if nodo.estado == sorted(self.estado_inicial):
            return nodo

        self.nodos_visitados.add(str(nodo.estado))
        if nodo.profundidad < limite_profundidad:
            nodo.expandir()
            for hijo in nodo.hijos:
                if tuple(hijo.estado) not in self.nodos_visitados:
                    resultado = self.dls(hijo, limite_profundidad)
                    if resultado is not None:
                        return resultado

        return None

    #Metodo Profundidad iterativa
    def iddfs(self):
        for limite_profundidad in range(10):
            resultado = self.dls(self.nodo_inicial, limite_profundidad)
            if resultado is not None:
                return resultado

        return None


def pancake_sorting(pancakes):
    grafo = Grafo(pancakes)
    solucion = grafo.iddfs()
    if solucion is None:
        return None

    movimientos = []
    while solucion.padre is not None:
        movimientos.append(solucion.estado)
        solucion = solucion.padre

    movimientos.reverse()
    return movimientos


pancakes = [3 ,2 ,5 ,1 ,4 ,8 ,7 ,6]

start_time = time.time()
movimientos = pancake_sorting(pancakes)
elapsed_time = time.time() - start_time

print("\nMetodo busqueda por Profundidad Iterativa")

print("Lista desordenada:", pancakes)
print("Lista ordenada:", sorted(pancakes))

if movimientos is not None:
    print("Pasos necesarios para ordenar:", len(movimientos))
    for i, paso in enumerate(movimientos):
        print(f"Paso {i + 1}: {paso}")
    print("Movimientos totales realizados:", len(movimientos))
else:
    print("No se encontró solución en el límite de movimientos.")

print("Tiempo transcurrido:", elapsed_time, "segundos")