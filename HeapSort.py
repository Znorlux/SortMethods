def heapify(arr, n, i, columna):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left][columna] > arr[largest][columna]:
        largest = left

    if right < n and arr[right][columna] > arr[largest][columna]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambia los elementos
        heapify(arr, n, largest, columna)

def heap_sort(arr, columna):
    n = len(arr)

    # Construye un Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, columna)

    # Extrae elementos uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambia los elementos
        heapify(arr, i, 0, columna)

    return arr
