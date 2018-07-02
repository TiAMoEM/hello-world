def ShellSort(arr):
    length = len(arr)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            j = i
            while j >= gap:
                if arr[j] < arr[j - gap]:
                    arr[j], arr[j - gap] = arr[j - gap], arr[j]
                    j -= gap
                else:
                    break
        gap //= 2
    return arr

