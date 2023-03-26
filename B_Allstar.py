import time

class Nodo:
    def __init__(self, estado, padre=None, g=0, h=0):
        self.estado = estado
        self.padre = padre
        self.g = g
        self.h = h
        self.f = g + h

class Grafo:
    def __init__(self):
        self.nodos = []
    
    def obtener_vecinos(self, nodo):
        vecinos = []
        for i in range(2, len(nodo.estado)+1):
            nuevo_estado = list(reversed(nodo.estado[:i])) + nodo.estado[i:]
            vecinos.append(Nodo(nuevo_estado, nodo))
        return vecinos
    
    def heuristica(self, nodo):
        # Heurística: cantidad de pancakes fuera de lugar
        objetivo = list(range(1, len(nodo.estado)+1))
        return sum([1 for i in range(len(nodo.estado)) if nodo.estado[i] != objetivo[i]])
    
    def a_estrella(self, inicio, objetivo):
        abiertos = [inicio]
        cerrados = []
        
        while abiertos:
            actual = min(abiertos, key=lambda x: x.f)
            
            if actual.estado == objetivo:
                # Se encontró la solución A*
                solucion = []
                while actual:
                    solucion.append(actual.estado)
                    actual = actual.padre
                return list(reversed(solucion))
            
            abiertos.remove(actual)
            cerrados.append(actual)
            
            for vecino in self.obtener_vecinos(actual):
                if vecino in cerrados:
                    continue
                
                nuevo_g = actual.g + 1
                if vecino not in abiertos:
                    abiertos.append(vecino)
                elif nuevo_g >= vecino.g:
                    continue
                
                vecino.g = nuevo_g
                vecino.h = self.heuristica(vecino)
                vecino.f = vecino.g + vecino.h
        
        # No se encontró solución
        return None
    
pancakes = [3 ,2 ,5 ,1 ,4 ,6 ,7 ,8]
start_time = time.time()
elapsed_time = time.time() - start_time

# Creamos un grafo
grafo = Grafo()

# Definimos el estado inicial y el estado objetivo
inicio = Nodo(pancakes)
objetivo = list(range(1, len(inicio.estado)+1))

# Resolvemos el problema con A*
solucion = grafo.a_estrella(inicio, objetivo)

print("\nMetodo busqueda por A*")

print("Lista desordenada:", pancakes)
print("Lista ordenada:", sorted(pancakes))

if solucion is not None:
    movimientos = []
    for i in range(len(solucion)-1):
        movimientos.append(list(set(solucion[i]) - set(solucion[i+1])))
    if not movimientos:
        print("La lista ya está ordenada.")
    else:
        for i, paso in enumerate(solucion):
            if i > 0:
                print(f"Paso {i}: {paso}")
        print("Movimientos totales realizados:", len(movimientos),"Pasos")
else:
    print("No se encontró solución en el límite de movimientos.")

print("Tiempo transcurrido:", elapsed_time, "segundos")


