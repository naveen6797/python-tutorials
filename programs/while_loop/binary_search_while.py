def binary_search(Array, Search_Term):
    L = 0
    H = len(A)-1
    
    while L <= H:
        mid = (L+H)//2
        if Array[mid] < Search_Term:
            L = mid + 1
        elif Array[mid] > Search_Term:
            H = mid - 1
        else:
            return mid
    return -1

A = [2,3,4,10,40]
term = 2
index = binary_search(A, term)
if index >= 0:
    print("{} is at index {}".format(A[index], index))
else:
    print("Search term not found")
