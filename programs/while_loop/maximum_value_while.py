A = [5,8,3,6,2,9,100,1]
maximum_value = A[0]
index = 1
while index < len(A):
    if A[index] > maximum_value:
        maximum_value = A[index]
    index = index+1
print(maximum_value)

