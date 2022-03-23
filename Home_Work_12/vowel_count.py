# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def vowel_count(str_1,list_1):
    vowels_count = 0
    for l in str_1:
        if l in list_1:
            vowels_count += 1
    return vowels_count


input_str = "apple is my fav fruits."
vowels_list = ["a", "e", "i", "o", "u"]
count = vowel_count(input_str, vowels_list)
print(count)



