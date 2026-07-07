# passing values to function

   def calculate_area(width, height):

      result = width * height

      return result



   print(f"area = {calculate_area(5, 10)}")


----------------------------------------------------------------------------------------------



# default values in function

   you can specify default value to parameter and can change according to need



   def calculate_area(width, height = 10):

      return width * height



   print(f"area = {calculate_area(5)}")

   print(f"area = {calculate_area(5, 20)}")



------------------------------------------------------------------------------------------------



# finding largest number in array

def find_max(numbers):                   - no need to mention type, python automatically handles it at runtime , optional for readability: def find_max(numbers: list) -> int:

   greatest = numbers[0]



   for num in numbers:

       if num > greatest:

           greatest = num



   return greatest



array = [4, 7, 2, 9, 1]

print(f"greatest number in array = {find_max(array)}")

print(max(array))

array.sort()

print(array[-1])



---------------------------------------------------------------------------------------------------



###### **A sequence of similar things → List ["post1", "post2", "post3"]**

###### **Fixed data that won't change → Tuple ("admin", "editor", "viewer")**

###### **Data with named fields → Dictionary {"title": "My Post", "likes": 10}**



**-**

