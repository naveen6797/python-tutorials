A = [13,15,7,18,2,20,1]
maximum_value = A[0]
for i in range(1,len(A)):
    if A[i] > maximum_value:
        maximum_value = A[i]

print(maximum_value)
