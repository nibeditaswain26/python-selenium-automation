""" # O(n^2)
def unique_letter(str_1): # Google
    string = str_1.lower() # google
    for l in string: #O(n)
        if string.count(l) == 1: # O(n)
            return l


print(unique_letter("Google"))
"""

def unique_letter(str_1): # Google
    string = str_1.lower()
    new_dict = {}
    for l in string:
        if l not in new_dict:
            new_dict[l] = 1
        else:
            new_dict[l] += 1

    for k, v in new_dict.items():
        if v == 1:
            return k
    return False

print(unique_letter("Google"))
print(unique_letter("Amazon"))
print(unique_letter("applla"))
print(unique_letter("abcdefg"))
