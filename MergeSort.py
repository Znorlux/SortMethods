def merge_sort(arr, column_name):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left, column_name)
    right = merge_sort(right, column_name)

    return merge(left, right, column_name)

def merge(left, right, column_name):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][column_name] < right[j][column_name]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

