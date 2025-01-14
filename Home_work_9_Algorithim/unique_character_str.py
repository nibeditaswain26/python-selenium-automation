# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.
""" #using dict.
def unique_chara(s):
    string = s.lower()
    new_dict = {}
    for letter in string:
        if letter not in new_dict:
            new_dict[letter] = 1
        else:
            new_dict[letter] += 1
            return False

    return True


string_1 = "abcde"
print(unique_chara(string_1))
"""

# using set()


def uni_char(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return False
        else:
            char_set.add(char)
    return True


string_1 = "abcddsae"
print(uni_char(string_1))