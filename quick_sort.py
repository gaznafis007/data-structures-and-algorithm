#Sorting Algorithm: quick sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [z for z in arr[1:] if z <= pivot]
    right = [z for z in arr[1:] if z > pivot]
    print(left, pivot, right)
    return quick_sort(left) + [pivot] + quick_sort(right)


array =[3, 2, 14, 7, 67, 35, 1, 8, 13, 39, 21, 5, 54, 11]

print(quick_sort(array))