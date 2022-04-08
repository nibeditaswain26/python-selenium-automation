def merge_sort_asc(arr_1):
    if len(arr_1) <= 1:
        return arr_1

    middle_ele = len(arr_1) // 2
    return merge_array(merge_sort_asc(arr_1[:middle_ele]), merge_sort_asc(arr_1[middle_ele:]))


def merge_array(left_array, right_array):
    merged_array = []
    i = j = 0
    while i < len(left_array) or j < len(right_array):
        if i == len(left_array):
            merged_array.append(right_array[j])
            j += 1
            continue
        if j == len(right_array):
            merged_array.append(left_array[i])
            i += 1
            continue
        if left_array[i] < right_array[j]:
            merged_array.append(left_array[i])
            i += 1

        else:
            merged_array.append(right_array[j])
            j += 1
    return merged_array


input_array = [3, 2, 5, 7, 9, 1, 8, 6]
print(merge_sort_asc(input_array))