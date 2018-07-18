# -*- coding:utf-8 -*-

def BubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr)- i - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 6, 5, 4]
    print(BubbleSort(arr))

