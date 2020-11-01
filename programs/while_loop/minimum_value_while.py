A = [5,8,3,6,2,0,9,100,1,0]
minimum_value = A[0]
index = 1
while index < len(A):
    if A[index] < minimum_value:
        minimum_value = A[index]
    index = index+1
print(minimum_value)
