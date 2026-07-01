# Write a function to flatten a nested list.
# numbers =  [1,  [2,  [3, 4] ] ] → [1, 2, 3, 4]

numbers =  [1,  [2,  [3, 4] ] ]

def flat_array(numbers):
    result = []

    for item in numbers:
        if isinstance(item, list):
            result.extend(flat_array(item))
        else:
            result.append(item)

    return result

print(flat_array(numbers))