if __name__ == "__main__":
    arr = [3, 4, 1, 2, 6]
    print("Array sin ordenar: ", arr)
    
    n = len(arr)
    
    # Construir un maxheap
    for i in range(n // 2 - 1, -1, -1):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            j = largest
            while True:
                largest = j
                left = 2 * j + 1
                right = 2 * j + 2

                if left < n and arr[j] < arr[left]:
                    largest = left

                if right < n and arr[largest] < arr[right]:
                    largest = right

                if largest != j:
                    arr[j], arr[largest] = arr[largest], arr[j]
                    j = largest
                else:
                    break

    # Extraer elementos uno por uno
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        
        j = 0
        while True:
            largest = j
            left = 2 * j + 1
            right = 2 * j + 2

            if left < i and arr[j] < arr[left]:
                largest = left

            if right < i and arr[largest] < arr[right]:
                largest = right

            if largest != j:
                arr[j], arr[largest] = arr[largest], arr[j]
                j = largest
            else:
                break

    print("Array ordenado: ", arr)

