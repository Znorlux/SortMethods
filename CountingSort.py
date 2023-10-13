#No funciona porque solo retorna dos columnas
def counting_sort(arr, columna):
    # Encontrar el valor máximo en la columna
    max_val = max(arr, key=lambda x: x[columna])
    max_val = max_val[columna]

    # Crear una lista auxiliar para contar las ocurrencias de cada valor
    count = [0] * (max_val + 1)

    # Contar las ocurrencias de cada valor en la columna
    for elemento in arr:
        count[elemento[columna]] += 1

    # Reconstruir el arreglo ordenado
    sorted_arr = []
    for i in range(max_val + 1):
        sorted_arr.extend([i] * count[i])

    return sorted_arr