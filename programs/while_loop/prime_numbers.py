number = 2
result = 0
while (number <= 500):
   is_divisible = 0
   i=2
   while(number > i):
        if(number % i == 0):
           is_divisible = 1
        i = i+1
   if(is_divisible == 0):
       
       print(number,end=',')
   number = number + 1
   
