dict_item = {"apples": [100, 10], "oranges": [30, 5], "iphone":[20000, 10]}
choice = int(input("enter number"))
total_apples_amount = 0
total_oranges_amount = 0
total_iphones_amount = 0
while choice != 0:
    if choice == 1:
        print("apples")
        number_of_apples = 100
        apple_count = int(input("how many apples you want:"))
        remaining_apples = number_of_apples - apple_count
        apple_price = 100
        discount = 10
        apple_amount = apple_count*(apple_price - discount)
        total_apples_amount = total_apples_amount + apple_amount
        print("your apples amount is:",apple_amount)
        print("remaining apples in store:",remaining_apples)
        print("total_apples_amount is::",total_apples_amount)
        print("THANK YOU")
    elif choice == 2:
        print("oranges")
        number_of_oranges = 50
        oranges_count = int(input("how many oranges you want:"))
        remaining_oranges = number_of_oranges - oranges_count
        orange_price = 30
        discount = 5
        oranges_amount = oranges_count*(orange_price - discount)
        total_oranges_amount = total_oranges_amount + oranges_amount
        print("your oranges amount is:",oranges_amount)
        print("remaining oranges in store:",remaining_oranges)
        print("total_oranges_amount::",total_oranges_amount)
        print("THANK YOU")
    elif choice == 3:
        print("iphones")
        number_of_iphones = 100
        iphone_count = int(input("how many iphones you want:"))
        remaining_iphones = number_of_iphones - iphone_count
        iphone_price = 20000
        discount = 2000
        iphone_amount = iphone_count*(iphone_price - discount)
        total_iphones_amount = total_iphones_amount + iphone_amount
        print("your iphones amount is:",iphone_amount)
        print("remaining iphones in store:",remaining_iphones)
        print("total_iphones_amount:",total_iphones_amount)
        total_amount = (total_apples_amount + total_oranges_amount + total_iphones_amount)
        print("total_items_amount::",total_amount)
        print("THANK YOU")
    elif choice != 0:
        print("please enter valid number:")

    choice = int(input("enter number:"))

