def products_billing(total_bill):
        selecting_items = int(input( "select items in a given list if anything you want (OR ) enter ' 4 ' to EXIT : "))
        if selecting_items == 1 :
            apples_count = int(input("how many apples you want::"))
            return  (apples_count *(available_products['1.apples'][0] - available_products['1.apples'][1])) + products_billing(total_bill)
        elif selecting_items == 2 :
            oranges_count = int(input("how many oranges you want "))
            return  (oranges_count *(available_products["2.oranges"][0] - available_products["2.oranges"][1])) + products_billing(total_bill)
        elif selecting_items == 3 :
            iphones_count= int(input("how many oranges you want "))
            return  (iphones_count * (available_products["3.iphone"][0] - available_products["3.iphone"][1])) + products_billing(total_bill)
        elif selecting_items == 4:
            return (total_bill)
    

available_products = {"1.apples" : [100,10] ,"2.oranges" : [30,5] , "3.iphone" :[20000,10]}
print("Available items in the store :")
for i in available_products:
    print('{} cost  {}  DISSOUNT {}'.format(i,available_products[i][0], available_products[i][1]))
print("""selecte the items 1 or 2 or 3 """ )
print("TOTAL BILL:" ,products_billing(0) ,"WITH DISCOUNT")
