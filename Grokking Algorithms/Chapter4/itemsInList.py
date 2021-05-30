def recur(l):
    # keep going until list is empty
    if not l:  
        return 0
    else:
        # add length of list element 0 and move to next element
        return recur(l[1:]) + len(l[0])

print(recur(['a','b','c']))