number = int(input("enter number:"))
list1 = [10,20,30,40,50]
total = 0
while total < len(list1):
    if list1[total] == number:
        print("yes")
        break
    total = total + 1

else:
    print("no")
    
