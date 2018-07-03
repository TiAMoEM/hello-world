def QuickSort(arr, l, r):
    if l < r:
        q = partition(arr, l, r):
        QuickSort(arr, l, q - 1)
        QuickSort(arr, q + 1, r)

def partition(arr, l, r):
    x = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1
