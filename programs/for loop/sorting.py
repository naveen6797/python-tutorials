a = [10,23,5,8,90]
for i in range(len(a)):
    x = i
    for j in range(i+1, len(a)):
        if a[x] > a[j]:
           x=j
           
    a[i],a[x] = a[x],a[i]
print(a)

