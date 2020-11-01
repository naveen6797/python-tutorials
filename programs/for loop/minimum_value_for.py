A = [13,15,7,18,2,20,1]
minimum_value = A[0]
for i in range(1,len(A)):
    if A[i] < minimum_value:
        minimum_value = A[i]

print(minimum_value)
