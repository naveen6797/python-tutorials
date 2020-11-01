num = 1564
result = 0
for i in range(num):
    print(num)
    if num>0:
        result1 = num%10
        result = (result*10)+result1
        num = num//10
    else:
        break
print(result)
