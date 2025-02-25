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
