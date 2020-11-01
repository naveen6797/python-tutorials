def items_billing(apple, orange, iphone, apples_amount, oranges_amount, iphones_amount):
    choice = int(input("enter your choice sir (or) medam::"))
    while choice != 0:
        if choice == 1:
            number_of_apples = A["apple"][2]
            apples_count = int(input("how many apples you want sir (or) medam:"))
            if number_of_apples < apples_count:
                print("available apples only:",number_of_apples)
            else:
                remaining_apples = number_of_apples - apples_count
                apple_price = A["apple"][0]
                discount = A["apple"][1]/100*100
                apples_amount = apples_count*(apple_price - discount)
                print("your apples amount is:",apples_amount)
                print("remaining apples in store:",remaining_apples)
        elif choice == 2:
            number_of_oranges = A["orange"][2]
            oranges_count = int(input("how many oranges you want sir (or) medam:"))
            if number_of_oranges < oranges_count:
                print("available oranges only:",number_of_oranges)
            else:
                remaining_oranges = number_of_oranges - oranges_count
                oranges_price = A["orange"][0]
                discount = A["orange"][1]/100*100
                oranges_amount = oranges_count*(oranges_price-discount)
                print("your oranges amount is:",oranges_amount)
                print("remaining oranges in store:",remaining_oranges)
        elif choice == 3:
            number_of_iphones = A["iphone"][2]
            iphones_count = int(input("how many iphones you want sir (or) medam:"))
            if number_of_iphones < iphones_count:
                print("available iphones only:",number_of_iphones)
            else:
                remaining_iphones = number_of_iphones - iphones_count
                iphone_price = A["iphone"][0]
                discount = A["iphone"][1]/100*100
                iphones_amount = iphones_count*(iphone_price-discount)
                print("your iphones amount is:",iphones_amount)
                print("remaining iphones in store:",remaining_iphones)
        elif choice != 0:
            print("please enter valid number")
        print("total bill:",apples_amount+oranges_amount+iphones_amount)
        another = str(input("anything you want yes or no:"))
        if another == "yes":
            print("select the item:")
        else:
            return "THANK YOU"
        choice = int(input("select your choice sir (or) medam:"))


A = {"apple":[50,10,100],"orange":[20,5,200],"iphone":[20000,20,50]}
print("available items in the store:")
for item in A:
    print('{} cost {}  discount {}%'.format(item, A[item][0], A[item][1]), A[item][2])
print("choice 1 for apples")
print("choice 2 for oranges")
print("choice 3 for iphones")
apple = 'no'
orange = 'no'
iphone = 'no'
apples_amount = 0
oranges_amount = 0
iphones_amount = 0
result = items_billing(apple, orange, iphone, apples_amount, oranges_amount, iphones_amount)
print(result)

 
