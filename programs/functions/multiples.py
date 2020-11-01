def number(num):
    count = 0
    while num >= count:
        if count%5 == 0:
            print("{}".format(count),end=',')
        count = count+5

number(200)
