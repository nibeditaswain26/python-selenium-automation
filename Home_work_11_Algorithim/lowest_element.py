# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def two_lowest_ele(arr_1):
    first_low_ele = seco_low_ele = arr_1[0]
    for ele in range(1, len(arr_1)):
        # print("ele=", ele)
        if arr_1[ele] < first_low_ele:
            if arr_1[ele] < seco_low_ele:
                seco_low_ele = first_low_ele
                first_low_ele = arr_1[ele]

        else:
            if arr_1[ele] < seco_low_ele:
                seco_low_ele = arr_1[ele]

    return first_low_ele, seco_low_ele


input_arr = [20, 29, 23, 10, 70, 2, 1, 0]
lowest_output = two_lowest_ele(input_arr)
print(lowest_output)