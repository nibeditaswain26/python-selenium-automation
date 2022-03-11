# Given a string. Split it into two equal parts. Swap these parts and return the
# result.If the string has odd characters, the first part should be one character
# greater than the second part.

def split_half_swap(s):#  string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

    length_string = len(s)
    swapped_result = " "
    if length_string % 2 != 0:
        print(f"length of the string is:{length_string}, and it is a odd number.")
        half_string_index = int(length_string / 2) + 1
        # print("half_string_index: ", half_string_index)
    else:
        print(f"{length_string} is a even number.")
        half_string_index = int(length_string / 2)
    first_half = s[0:half_string_index]
        # print(first_half)
    second_half = s[half_string_index:]
        # print(second_half)
    swapped_result = f"{second_half}{first_half}"
    return swapped_result


str_1 = 'nibeditaswain'
swapped_string = split_half_swap(str_1)
print(f"Swapped string is: {swapped_string}")






