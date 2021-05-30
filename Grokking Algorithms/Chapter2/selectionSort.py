# Takes an array and finds the smallest element in it
def findSmallest(arr):
    
    # Stores the smallest value
    smallest = arr[0] 

    # Stores the index of the smallest value
    smallest_index = 0 
    
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index


# Sorts an array
def selectionSort(arr): 
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
