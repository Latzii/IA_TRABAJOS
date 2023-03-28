import time

def bfs_pancake_sort(pancakes):
    # Función auxiliar para voltear los primeros k elementos de pancakes
    def flip(pancakes, k):
        return pancakes[:k][::-1] + pancakes[k:]

    # Número de elementos en pancakes
    goal = sorted(pancakes)
    n = len(pancakes)

    # Nodo objetivo (pila ordenada)
    goal = sorted(pancakes)

    # Cola para almacenar los nodos a explorar
    queue = []

    # Conjunto para almacenar los nodos explorados
    visitado = set()

    # Diccionario para almacenar los nodos padres y flips
    parent = {}
    salto_directo = {}

    # Marcar el nodo inicial como explorado y añadirlo a la cola
    visitado.add(tuple(pancakes))
    queue.append(pancakes)

    # Contador para el número de movimientos realizados
    movimientos = 0

    # Mientras la cola no esté vacía
    while queue:
        # Sacar el primer nodo de la cola
        node = queue.pop(0)

        # Comprobar si es el objetivo
        if node == goal:
            # Devolver el nodo y el camino seguido
            path = []
            flips = []
            while node != pancakes:
                path.append(node)
                flips.append(salto_directo[tuple(node)])
                node = parent[tuple(node)]
            path.append(node)
            return path[::-1], flips[::-1], movimientos

        # Generar todos los posibles flips desde ese nodo
        for k in range(2, n + 1):
            new_node = flip(node, k)

            # Si no han sido explorados previamente, añadirlos a la cola y al conjunto visitado
            if tuple(new_node) not in visitado:
                visitado.add(tuple(new_node))
                queue.append(new_node)

                # Guardar también el nodo padre y flip de cada flip
                parent[tuple(new_node)] = node
                salto_directo[tuple(new_node)] = k

        # Incrementar el contador de movimientos
        movimientos += 1

    # Si no se encontró solución en el límite de movimientos, devolver None
    return None, None, None


# Ejemplo de uso
pancakes = ['h', 'c', 'f', 'a', 'd', 'g', 'b', 'e']
start_time = time.time()  # Guarda el tiempo actual
path, flips, movimientos = bfs_pancake_sort(pancakes)
elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
print("\nMetodo busqueda por Amplitud")

# Nodo objetivo (pila ordenada)
goal = sorted(pancakes)
print("Lista desordenada:", pancakes)
print("Lista ordenada:", goal)
# Imprimir los pasos
print(path[0])
for i, paso in enumerate(path[1:], 1):
    print(f"Paso: {i} {paso}")
print("Movimientos totales realizados:", movimientos)
if path is not None:
    print("Pasos necesarios para ordenar:", len(path)-1)
else:
    print("No se encontró solución en el límite de movimientos.")

print("Tiempo transcurrido:", elapsed_time, "segundos")
