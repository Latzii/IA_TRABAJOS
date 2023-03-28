import heapq
import time

class Nodo:
    def __init__(self, estado, padre=None, accion=None, costo_camino=0):
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.costo_camino = costo_camino
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __lt__(self, otro):
        return self.costo_camino < otro.costo_camino

class Grafo:
    def __init__(self):
        self.nodos = []

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)

def voltear(pancakes, k):
    return pancakes[:k+1][::-1] + pancakes[k+1:]

def es_objetivo(pancakes):
    return pancakes == sorted(pancakes)

def heuristica(pancakes):
    cuenta = 0
    for i in range(len(pancakes)-1):
        if abs(ord(pancakes[i]) - ord(pancakes[i+1])) > 1:
            cuenta += 1
    return cuenta

def a_estrella(pancakes):
    grafo = Grafo()
    nodo_inicial = Nodo(pancakes)
    grafo.agregar_nodo(nodo_inicial)
    frontera = []
    heapq.heappush(frontera, (0, nodo_inicial))
    explorados = set()
    while frontera:
        nodo_actual = heapq.heappop(frontera)[1]
        if es_objetivo(nodo_actual.estado):
            return nodo_actual
        explorados.add(tuple(nodo_actual.estado))
        for i in range(len(nodo_actual.estado)):
            estado_hijo = voltear(nodo_actual.estado, i)
            if tuple(estado_hijo) not in explorados:
                nodo_hijo = Nodo(estado_hijo, nodo_actual, i, nodo_actual.costo_camino + 1)
                grafo.agregar_nodo(nodo_hijo)
                nodo_actual.agregar_hijo(nodo_hijo)
                heapq.heappush(frontera, (nodo_hijo.costo_camino + heuristica(estado_hijo), nodo_hijo))
    return None

def obtener_solucion(nodo):
    solucion = []
    while nodo.padre is not None:
        solucion.append(nodo.estado)
        nodo = nodo.padre
    solucion.reverse()
    return solucion

pancakes = ['h', 'c', 'f', 'a', 'd', 'g', 'b', 'e']

tiempo_inicio = time.time()  # Guarda el tiempo actual
nodo_solucion = a_estrella(pancakes)
solucion = obtener_solucion(nodo_solucion)
tiempo_transcurrido = time.time() - tiempo_inicio  # Calcula el tiempo transcurrido

print("\nMetodo busqueda por A*")

# Nodo objetivo (pila ordenada)
objetivo = sorted(pancakes)
print("Lista desordenada:", pancakes)
print("Lista ordenada:", objetivo)

# Imprimir los pasos
for i, paso in enumerate(solucion, 1):
    print(f"Paso: {i} {paso}")

print("Movimientos totales realizados:", len(solucion))
if solucion is not None:
    print("Pasos necesarios para ordenar:", len(solucion))
else:
    print("No se encontró solución en el límite de movimientos.")

print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
