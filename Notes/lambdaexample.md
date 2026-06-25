numbers = []

result = []



for i in range(1,21):

   numbers.append(i)



def check_num(num):

   if (num % 3 == 0 and num % 5 == 0):

       result.append(num)



for n in numbers:

   check_num(n)



print(result)



result2 = list(filter(lambda x: x%3 == 0 and x%5==0, numbers))

print(result2)



names = ["name1", "name2", "name3", "name4"]



for i in range(len(names)):

   print(f"{i} {names[i]}")

       

