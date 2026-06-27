# Write a function word_count that:

# Takes a sentence as input
# Returns a dictionary with each word as key and its count as value
# Should be case insensitive

# Example:
# word_count("the cat sat on the mat the cat")
# # {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}


def word_count(sentence="my cat is cat blue is my cat"):
    words = sentence.strip().lower().split(" ")
    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict


print(word_count())


# OR
# def word_count(sentence):
#     words = sentence.strip().lower().split()
#     return {word: words.count(word) for word in set(words)}

# print(word_count("the cat sat on the mat the cat"))

# OR
# def word_count(sentence = "my cat is cat blue is my cat"):
#     words = sentence.strip().lower().split(" ")
#     words_list = []
#     count_list = []

#     for index,value in enumerate(words):
#         count = 1
#         for i in range(index+1, len(words)):
#             if(not value in words_list):
#                 words_list.append(value)
#             if(value == words[i] and value in words_list):
#                 count += 1
#             if(i == len(words)-1 and value not in words[:index] ):
#                 count_list.append(count)

#     print(words_list)
#     print(count_list)
#     return(dict(zip(words_list,count_list)))

# print(word_count())
