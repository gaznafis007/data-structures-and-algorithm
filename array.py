# type: ignore # Array: an array is fixed size of collection of items stored at contiguous memory locations. In python arrays are implemented as lists.

arr = [10, 20, 30, 40, 50] #example of an array/list
print(arr)
print(arr[0]) #accessing the first element of the array
print(len(arr)) #get the length of an array

# Insertion: adding an element at the end, beginning , or at any specific index.

arr.append(60) #adding an element at the end of the array
print(arr)
arr.insert(0, 5) #adding an element at the beginning of the array
def insert_at_specific_index(arr, index, value):
    i = 0
    while i < len(arr):
        if i == index:
            arr[index] = value
            return arr
        i+=1
    return 'Index out of range'
print(arr)
print(insert_at_specific_index(arr, 1, 70))
arr.insert(3, 25) #adding an element at any specific index
print(arr)

#Deletion: removing an element from the end, beginning, or at any specific index.
arr.pop() #removing an element from the end of the array
print(arr)

# build a function to remove an element from the end of the array
def pop_at_end(arr):
    new_arr = []
    for i in range(len(arr) - 1):
        new_arr.append(arr[i])
    return new_arr
print(pop_at_end(arr), 'pop at end')

arr.pop(0) #removing an element from the beginning/any specific index of the array
print(arr)
arr.remove(25) #removing a given element which will come first
print(arr)

# build a function to remove an element from the given value
def remove_element(arr, value):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] != value:
            new_arr.append(arr[i])
    return new_arr
print(remove_element(arr, 70), 'remove element')
#Searching: search an element in an array
print(arr.index(40)) #searching an element in an array

#Linear Search: This is the simplest search algorithm. In this type of search, a sequential search is made over all elements one by one until the desired element is found or search reaches the end of the elements.

##TIME COMPLEXITY: 0(N)
##SPACE COMPLEXITY: 0(1)
## When not to use: When the array is sorted, or a large number of elements are there in the array.

def linear_search(array, num):
#using while loop
    i = 0
    while (i < len(array)):
        if(array[i] == num):
            return i
        i += 1
    return 'Element not found'

def linear_search_for_loop(array, num):
    #using for loop
    for i in range(len(array)):
        if(array[i] == num):
            return i
        return 'Element not found'

print(linear_search(arr, 40))
print(linear_search_for_loop(arr, 60))
print(arr)
#Question: Given an array of strings, find the index of a given string.

def find_word(arr, str):
    for i in range(len(arr)):
        if(arr[i] == str):
            return i
    return f'{str} is not found in the array'

str_array = ['apple, banana, cherry, date, elderberry']
print(find_word(str_array, 'cherry'))