def findSmalleest(arr):
    # наименьшее значение
    smallest = arr[0]
    # индекс наименьшего значения
    smallest_index = 0
    for i in range(1, len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        print(i)
        smallest = findSmalleest(arr)
        print(smallest)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
