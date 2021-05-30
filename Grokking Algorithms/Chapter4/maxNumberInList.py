def Max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        m = Max(arr[1:])
        return m if m > arr[0] else arr[0]

print(Max([1,2,3,4,5,6,7]))