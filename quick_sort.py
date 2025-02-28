#Sorting Algorithm: quick sort
# Big(O) - O(N^2)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [z for z in arr[1:] if z <= pivot]
    right = [z for z in arr[1:] if z > pivot]
    # print(left, pivot, right)
    return quick_sort(left) + [pivot] + quick_sort(right)


array =[3, 2, 14, 7, 67, 35, 1, 8, 13, 39, 21, 5, 54, 11]

print(quick_sort(array))

#Sort an array of floating-point numbers using Quick Sort.
def floating_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [y for y in arr[1:] if y > pivot]

    return floating_quick_sort(left) + [pivot] + floating_quick_sort(right)

print(floating_quick_sort([3.92, 0.76, 7.24, 1, 4.54, 6.21, 0.12, 9.87, 3.45]))

#reverse sort
def reverse_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x >= pivot]
    right = [x for x in arr[:-1] if x < pivot]

    return reverse_quick_sort(left) + [pivot] + reverse_quick_sort(right)

print(reverse_quick_sort(array), 'reverse')
