if __name__ == "__main__":
    # Definimos el array que queremos ordenar
    arr = [3, 4, 1, 2, 7, 0, 5]
    print("Array sin ordenar: ", arr)

    # Almacenamos el tamaño del array
    n = len(arr)

    # Construcción del "max heap":
    # Aquí vamos a construir el heap (un árbol binario donde cada nodo es mayor que sus hijos)
    # Empezamos desde el último nodo que tiene hijos, que es en la posición (n // 2 - 1)
    # y vamos hacia atrás hasta el primer elemento.
    for i in range(n // 2 - 1, -1, -1):
        # Inicializamos la variable `largest` como la raíz actual `i`
        largest = i
        # Calculamos la posición del hijo izquierdo de `i`
        left = 2 * i + 1
        # Calculamos la posición del hijo derecho de `i`
        right = 2 * i + 2

        # Verificamos si el hijo izquierdo es más grande que la raíz
        if left < n and arr[i] < arr[left]:
            largest = left

        # Verificamos si el hijo derecho es más grande que el nodo más grande hasta ahora
        if right < n and arr[largest] < arr[right]:
            largest = right

        # Si el nodo más grande no es la raíz, intercambiamos
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            # Aplicamos "heapify" a la nueva sub-raíz para asegurarnos de que sigue siendo un heap.
            # Para ello, seguimos "empujando" hacia abajo el nodo mayor hasta que quede en su posición correcta.
            # Reutilizamos el mismo proceso que antes, pero ahora con `largest` como la raíz.
            while True:
                largest = i
                left = 2 * i + 1
                right = 2 * i + 2

                if left < n and arr[i] < arr[left]:
                    largest = left

                if right < n and arr[largest] < arr[right]:
                    largest = right

                if largest != i:
                    arr[i], arr[largest] = arr[largest], arr[i]
                    i = largest  # Continuamos heapificando la nueva posición
                else:
                    break

    # Ahora que tenemos el heap construido, empezamos el proceso de ordenamiento.
    # Vamos a extraer el mayor elemento (que está en la raíz) uno por uno.
    for i in range(n-1, 0, -1):
        # Intercambiamos el primer elemento (el mayor del heap) con el último elemento del array
        arr[i], arr[0] = arr[0], arr[i]

        # Reducimos el tamaño efectivo del heap y aplicamos heapify al nuevo elemento de la raíz
        # Esto reorganiza el heap para que el nuevo mayor quede en la raíz.
        largest = 0
        left = 2 * largest + 1
        right = 2 * largest + 2

        # Realizamos el proceso de heapify manualmente, como hicimos antes
        while True:
            largest = 0
            left = 2 * largest + 1
            right = 2 * largest + 2

            if left < i and arr[largest] < arr[left]:
                largest = left

            if right < i and arr[largest] < arr[right]:
                largest = right

            if largest != 0:
                arr[0], arr[largest] = arr[largest], arr[0]
                largest = 0  # Seguimos heapificando
            else:
                break

    # Imprimimos el array ya ordenado
    print("Array ordenado: ", arr)


