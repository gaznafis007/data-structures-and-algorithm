#Binary Search: Binary Search is an efficient search algorithm to find an element in a sorted array.

# ##TIME COMPLEXITY: 0(log N)
# ##SPACE COMPLEXITY: 0(1)
# ## When not to use: When the array is not sorted.

## **How Binary Search Works?**

# Binary Search works on the **divide and conquer** principle:

# 1. Find the **middle element** of the array.
# 2. If the **middle element is equal** to the target, return its index.
# 3. If the **middle element is smaller** than the target, the target must be in the **right half**, so we discard the left half.
# 4. If the **middle element is larger** than the target, the target must be in the **left half**, so we discard the right half.
# 5. Repeat steps 1-4 until the target is found or the search space is empty.

def binary_search(arr, num):
    left = 0
    right = int(len(arr)-1)
    mid = (left + right) // 2
    # print(left)
    # print(right)
    # print(mid)
    while left <= right:
        mid = (left + right) // 2
        # print(mid)
        if arr[mid] == num:
            return f'{num} found at index {mid}'
        elif arr[mid] < num:
            left = mid + 1
            # print(left)
            # print(left, 'drop left')
        else:
            right = mid - 1
            # print(right)
            # print(left, 'drop right') 
    return f'{num} not found'

arr = [9, 12, 17, 21, 25, 29, 37]

print(binary_search(arr, 25))

# Recursive Binary Search
def recursive_binary_search(arr, left, right, number):
    mid = (left + right) //2
    if(left > right):
        return f'{number} not found'
    elif arr[mid] == number:
        return f'{number} found at index {mid}' 
    elif arr[mid] < number:
        return recursive_binary_search(arr, mid + 1, right, number)
    else:
        return recursive_binary_search(arr, left, mid -1, number)
    
print('recursive', recursive_binary_search(arr, 0, len(arr)-1, 71))

#Find square root of a number using binary search
def sqr_root(num):
    left = 0
    right = num
    while left <= right:
        mid = float((left + right) //2)
        if mid * mid == num:
            return mid
        elif mid * mid < num:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result
print(sqr_root(16))

def find_smallest_of_target(arr, number):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= number:
            return arr[mid]
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return 'not found'
print(find_smallest_of_target([2, 4, 6, 8, 10], 2))

#Find the rotation count of a rotated sorted array
def find_rotation_count(arr):
    left = 0;
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        print(mid, 'mid')
        if(arr[left] <= arr[right]):
            return left
        if(mid > 0 and arr[mid] < arr[mid - 1]):
            return mid
        if(arr[mid] >= arr[left]):
            left = mid + 1
        else:
            right = mid - 1

print(find_rotation_count([0, 1, 2, 3, 4, 5, 6, 7]))
print(find_rotation_count([4, 5, 6, 7, 0, 1, 2]))