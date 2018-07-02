# -*- coding:utf-8 -*-

def InsertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > key:
                arr[j + 1], arr[j] = arr[j], key
            j -= 1
    return arr


