A = [2,3,5,7,8,9]
length = len(A)
for i in range(length//2):
    A[i],A[length-1-i] =  A[length-1-i],A[i]
    print(A)
    
