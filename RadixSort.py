def counting_sort_radix(arr, exp, columna):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i][columna] // exp)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i][columna] // exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr, columna):
    max_val = max(arr, key=lambda x: x[columna])[columna]

    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(arr, exp, columna)
        exp *= 10

    return arr
