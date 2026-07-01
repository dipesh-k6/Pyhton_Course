# Find the sum of all unique positive even number from the following:
# matrix = [
# [1,2,3,-4],
# [4,10,-20,30],
# [2,4, 6, 8, 10],
# [4, 8, 16, - 20, 30]
# ] 

matrix = [
[1,2,3,-4],
[4,10,-20,30],
[2,4, 6, 8, 10],
[4, 8, 16, - 20, 30]
] 

all_data = []
list(map(lambda row: all_data.extend(row), matrix))
print(sum(set(filter(lambda x: x>0 and x%2 == 0, all_data))))


# OR
# numbers = []
# for rows in matrix:
#     for column in rows:
#         if column>0 and column%2 == 0:
#             numbers.append(column)

# print(sum(set(numbers)))