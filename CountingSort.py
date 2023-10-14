def counting_sort(arr, columna):
    # Encontrar el valor máximo en la columna
    max_val = max(arr, key=lambda x: x[columna])
    max_val = max_val[columna]

    # Crear una lista auxiliar para contar las ocurrencias de cada valor
    count = [0] * (max_val + 1)

    # Contar las ocurrencias de cada valor en la columna
    for elemento in arr:
        count[elemento[columna]] += 1

    # Reconstruir el arreglo ordenado con todas las columnas
    sorted_arr = []
    for i in range(max_val + 1):
        for elemento in arr:
            if elemento[columna] == i:
                sorted_arr.append(elemento)

    return sorted_arr
