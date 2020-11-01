A = [1,2,3,4,5,6]
i = 0
length = len(A)
while (length//2)> i:
    A[i],A[length-1-i]=A[length-1-i],A[i]
    print(A)
    i = i+1
