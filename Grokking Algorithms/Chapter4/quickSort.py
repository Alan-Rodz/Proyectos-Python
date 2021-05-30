# Performs quicksort on an array
def quicksort(array):
    
    # Base case: arrays with 0 or 1 element are already “sorted.”
    if len(array) < 2:
        return array
    
    # Recursive case
    else:
        pivot = array[0] 

        # Sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot] 

        # Sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot] 
        
        return quicksort(less) + [pivot] + quicksort(greater)

print (quicksort([10, 5, 2, 3]))
