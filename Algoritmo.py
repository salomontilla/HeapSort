def heapify(arr, n, i):
    largest = i  # Inicializar el nodo más grande como raíz
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2  # Hijo derecho

    # Verificar si el hijo izquierdo es más grande que la raíz
    if left < n and arr[i] < arr[left]:
        largest = left

    # Verificar si el hijo derecho es más grande que el nodo más grande hasta ahora
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Cambiar la raíz si es necesario
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambiar
        heapify(arr, n, largest)  # Heapify la raíz

def heapSort(arr):
    n = len(arr)

    # Construir un maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiar
        heapify(arr, i, 0)
        

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Array sin ordenar: ", arr)
    heapSort(arr)
    print("Array ordenado: ", arr)
