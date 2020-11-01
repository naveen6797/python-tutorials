a = [5,8,2,6]
i=0
j=1
while i < len(a):
    if a[i] >a[j]:
        i = j
    i = i+1

    a[i],a[j]=a[j],a[i]
print(a)

