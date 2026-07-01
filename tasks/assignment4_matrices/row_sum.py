# numbers =  [
# [5 , 8,   1,   3]
# [9,   2,   7,   6]
# [4,   0,   5,   9]
# [3,   6,   8,   2]
# ]

# from the given matrix find the sum of all rows and sort them in descending order.

numbers = [[5, 8, 1, 3], 
           [9, 2, 7, 6], 
           [4, 0, 5, 9], 
           [3, 6, 8, 2]]

rows_sum = [sum(row) for row in numbers]
print(sorted(rows_sum, reverse=True))


# OR
# sum_rows = []
# for row in numbers:
#     value = sum(row)
#     sum_rows.append(value)

# print(sorted(sum_rows, reverse=True))
