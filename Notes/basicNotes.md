# concatenation

   age = 25

   print("My age is " + age)



   * cannot concatenate two different data types like this



   \--solution:

   age = 25

   print("My age is " + str(age))



   or better



   age = 25

   print(f"My age is {age}")



----------------------------------------



# Identation

* (tab)



----------------------------------------



# shift from js to python

   * no curly braces {} and less small brackets () , colon : and identation takes place
   * no semicolon

-----------------------------------------

# Range

   for number in range(5):

      print(number)



   * this gives 0 to 4



   range(1, 6)     output: 1, 2, 3, 4, 5

   range(0, 10, 2) output: 0, 2, 4, 6, 8  (step by 2)



------------------------------------------------



# List

   fruits = \["apple", "banana", "mango"]



   * fruits\[0]  result: first item
   * fruits\[-1] result: last item
   * fruits.append("orange") result: puts item on last
   * fruits.remove("banana") result: removes by name
   * print(len(fruits)) ps: there is no such thing as fruits.len()

---------------------------------------------------

# when a function returns nothing, it returns None automatically

   * example:

   print(fruits.append("pineapple")) result:None cause it returns nothing but does its job



\-

