from typing import List
import time

class Node:
    def __init__(self, estado: List[int], g: int, h: int):
        self.estado = estado
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

class Pancakegrafo:
    def __init__(self, start: List[int]):
        self.start = start

    def get_neighbors(self, node: Node) -> List[Node]:
        neighbors = []
        for i in range(2, len(node.estado) + 1):
            new_estado = node.estado[:i][::-1] + node.estado[i:]
            new_node = Node(new_estado, node.g + 1, self.heuristic(new_estado))
            neighbors.append(new_node)
        return neighbors

    def heuristic(self, estado: List[int]) -> int:
        return sum([1 for i in range(len(estado) - 1) if abs(ord(estado[i]) - ord(estado[i+1])) > 1])

def ida_star_recursiva(grafo: Pancakegrafo) -> int:
    bound = grafo.heuristic(grafo.start)
    start_node = Node(grafo.start, 0, bound)
    path = [start_node]
    while True:
        min_f = dfs_recursive(grafo, path, 0, bound)
        if min_f == float('inf'):
            return -1
        if min_f == 0:
            return path[-1].g
        bound = min_f

def dfs_recursive(grafo: Pancakegrafo, path: List[Node], g: int, bound: int) -> int:
    node = path[-1]
    f = g + node.h
    if f > bound:
        return f
    if node.h == 0:
        return 0

    min_f = float('inf')
    for neighbor in grafo.get_neighbors(node):
        if neighbor not in path:
            path.append(neighbor)
            new_min_f = dfs_recursive(grafo, path, g + 1, bound)
            if new_min_f == 0:
                return 0
            min_f = min(min_f, new_min_f)
            path.pop()

    return min_f

def dfs(grafo: Pancakegrafo, path: List[Node], g: int, bound: int) -> int:
    node = path[-1]
    f = g + node.h
    if f > bound:
        return f
    if node.h == 0:
        return 0

    min_f = float('inf')
    for neighbor in grafo.get_neighbors(node):
        if neighbor not in path:
            path.append(neighbor)
            new_min_f = dfs(grafo, path, g + 1, bound)
            if new_min_f == 0:
                return 0
            min_f = min(min_f, new_min_f)
            path.pop()
    return min_f

def pancake_sorting(piles: List[int]) -> List[List[int]]:
    grafo = Pancakegrafo(piles)
    bound = grafo.heuristic(grafo.start)
    start_node = Node(grafo.start, 0, bound)

    while True:
        path = [start_node]
        min_f = dfs(grafo, path, 0, bound)
        if min_f == float('inf'):
            return None
        if min_f == 0:
            return [node.estado for node in path]
        bound = min_f

pancakes = ['h', 'c', 'f', 'a', 'd', 'g', 'b', 'e']

start_time = time.time()
movimientos = pancake_sorting(pancakes)
elapsed_time = time.time() - start_time

print("\nMetodo busqueda por IDA")

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
