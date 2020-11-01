def maximum_value(A):
    maximum_value = A[0]
    index = 1
    while index < len(A):
        if A[index] > maximum_value:
            maximum_value = A[index]
        index = index+1
    print("maximum value of a list is::",maximum_value)

x = [5,8,3,6,2,9,100,1]
y = [10,49,39,400,20]
maximum_value(x)
maximum_value(y)
