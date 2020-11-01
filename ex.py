a = [2,7,1,4,100]
x = a[0]
for i in range(1,len(a)):
    if a[i] > x:
        x = a[i]
print("minimum value:",x)
