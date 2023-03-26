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

    def dfs(self, nodo, max_profundidad):
        if nodo.estado == sorted(self.estado_inicial):
            return nodo

        self.nodos_visitados.add(tuple(nodo.estado))
        if nodo.profundidad < max_profundidad:
            nodo.expandir()
            for hijo in nodo.hijos:
                if tuple(hijo.estado) not in self.nodos_visitados:
                    resultado = self.dfs(hijo, max_profundidad)
                    if resultado is not None:
                        return resultado

        return None


def pancake_sorting(pancakes):
    grafo = Grafo(pancakes)
    max_profundidad = 20
    solucion = grafo.dfs(grafo.nodo_inicial, max_profundidad)
    if solucion is None:
        return None

    movimientos = []
    while solucion.padre is not None:
        movimientos.append(solucion.estado)
        solucion = solucion.padre

    movimientos.reverse()
    return movimientos

pancakes = [3 ,2 ,5 ,1 ,4 ,6 ,7 ,8]

start_time = time.time()
movimientos = pancake_sorting(pancakes)
elapsed_time = time.time() - start_time

print("\nMetodo busqueda por profundidad")

print("Lista desordenada:", pancakes)
print("Lista ordenada:", sorted(pancakes))

if movimientos is not None:
    print("Pasos necesarios para ordenar:", len(movimientos))
    for i, paso in enumerate(movimientos):
        print(f"Paso {i + 1}: {paso}")
else:
    print("No se encontró solución en el límite de movimientos.")

print("Movimientos totales realizados:", len(movimientos))
print("Tiempo transcurrido:", elapsed_time, "segundos")