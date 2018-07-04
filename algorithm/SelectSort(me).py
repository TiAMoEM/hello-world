def SelectSort(arr):
    for i in range(0, len(arr)):
        flag = arr[i]
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < flag:
                flag = arr[j]
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr