# Write a function is_palindrome that:

# Takes a string
# Returns True if it's a palindrome, False if not
# Should be case insensitive and ignore spaces

# Examples:
# pythonis_palindrome("racecar")     # True
# is_palindrome("Race Car")    # True
# is_palindrome("hello")       # False
# is_palindrome("Never odd or even")  # True

def check_pallindrome(string):
    string = string.replace(" ","").lower()
    rev = string[::-1]
    return (string == rev)

print(check_pallindrome("Race Car"))
