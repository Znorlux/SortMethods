from QuickSort import quick_sort
def bucket_sort(lista, columna_ordenar):
    max_value = max(lista, key=lambda x: int(x[columna_ordenar]))
    min_value = min(lista, key=lambda x: int(x[columna_ordenar]))
    range_value = max_value[columna_ordenar] - min_value[columna_ordenar]

    # Crear los buckets
    num_buckets = len(lista)
    buckets = [[] for _ in range(num_buckets)]

    # Colocar elementos en los buckets
    for item in lista:
        index = int((item[columna_ordenar] - min_value[columna_ordenar]) / (range_value / (num_buckets - 1)))
        buckets[index].append(item)

    #Ordenamos cada bucket y combinar
    for i in range(num_buckets):
        buckets[i] = quick_sort(buckets[i], columna_ordenar)

    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(bucket)

    return sorted_list
