#JUEGO DEL 15 (TAKEN)
class Nodo:
    #METODO MANHATTAN
    def __init__(self, estado, padre=None):
        self.estado = estado
        self.padre = padre
        self.g = 0 if padre is None else padre.g + 1
        self.h = sum(abs((val - 1) % 4 - i % 4) + abs((val - 1) // 4 - i // 4)
                     for i, val in enumerate(estado) if val)
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.estado == other.estado

    def __hash__(self):
        return hash(self.estado)

    def obtener_hijos(self):
        indice_cero = self.estado.index(0)
        x, y = indice_cero % 4, indice_cero // 4
        hijos = []
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nuevo_x, nuevo_y = x + dx, y + dy
            if 0 <= nuevo_x < 4 and 0 <= nuevo_y < 4:
                nuevo_indice_cero = nuevo_y * 4 + nuevo_x
                nuevo_estado = list(self.estado)
                nuevo_estado[indice_cero], nuevo_estado[nuevo_indice_cero] = nuevo_estado[nuevo_indice_cero], nuevo_estado[indice_cero]
                hijos.append(Nodo(tuple(nuevo_estado), self))
        return hijos

#BUSQUEDA POR IDA
def ida(estado_inicial):
    nodo_inicial = Nodo(estado_inicial)
    limite = nodo_inicial.h
    camino = [nodo_inicial]
    visitados = set([nodo_inicial])
    while True:
        t = busqueda(camino, 0, limite, visitados)
        if t == 'ENCONTRADO':
            return camino
        if t == float('inf'): #INFINITO
            return []
        limite = t

def busqueda(camino, g, limite, visitados):
    nodo = camino[-1]
    f = g + nodo.h
    if f > limite:
        return f
    if nodo.h == 0:
        return 'ENCONTRADO'
    costo_minimo = float('inf') #INFINITO
    for hijo in nodo.obtener_hijos():
        if hijo not in visitados:
            camino.append(hijo)
            visitados.add(hijo)
            t = busqueda(camino, g + 1, limite, visitados)
            if t == 'ENCONTRADO':
                return 'ENCONTRADO'
            if t < costo_minimo:
                costo_minimo = t
            camino.pop()
            visitados.remove(hijo)
    return costo_minimo

def resolver_puzzle(estado_inicial):
    if not es_resolvible(estado_inicial):
        return []
    camino = ida(estado_inicial)
    return camino

def imprimir_estado(estado):
    for fila in range(4):
        fila_strs = [] #LISTA VACIA, ALMACENA TEMPORALMENTE VALORES DEL ROMPECABEZA
        for col in range(4):
            val = estado[fila * 4 + col]
            fila_strs.append(f"[{val:2d}]" if val else "[   ]")
        print(" ".join(fila_strs))

def es_resolvible(estado):
    inversiones = 0
    for i in range(len(estado)):
        for j in range(i + 1,len(estado)):
            if estado[j] and estado[i] and estado[i] > estado[j]:
                inversiones += 1
    return inversiones % 2 == 0

estado_inicial = (5 ,1 ,7 ,3 ,9 ,2 ,11 ,4 ,13 ,6 ,15 ,8 ,0 ,10 ,14 ,12) #LISTA PUEDE SER MODIFICABLE

if not es_resolvible(estado_inicial): 
    print("\nEstado Inicial:") 
    imprimir_estado(estado_inicial) 
    print("\nEste rompecabezas no tiene solución.") 
else:
    camino = resolver_puzzle(estado_inicial)
    if camino: 
        print("\nEstado Inicial:")
        imprimir_estado(estado_inicial)
        for i, nodo in enumerate(camino): 
            print(f"\nMovimiento {i}:") 
            imprimir_estado(nodo.estado) 
        print(f"\nTotal numeros de moviminetos utilizados: {len(camino) - 1}") 




          
