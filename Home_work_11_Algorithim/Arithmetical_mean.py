# When given a list, the program should return a list of all the elements below
# the original list’s arithmetical mean. The arithmetical mean is the sum of all
# elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25),
# Return [1, 3, 4, 2, 3]

def arithmetical_mean(arr_1):
    if len(arr_1) == 1:
        return arr_1[0]

    new_list = []
    element_number = len(arr_1)
    sum_arr = 0
    for num in arr_1:
        sum_arr = sum_arr + num

    ari_mean = sum_arr / element_number
    for num in arr_1:
        if num < ari_mean:
            new_list.append(num)

    return new_list


input_array = [1, 3, 5, 6, 4, 10, 2, 3]
print(arithmetical_mean(input_array))