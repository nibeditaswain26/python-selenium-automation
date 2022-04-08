def selection_sort_desc(arr_1):
    for i in range(len(arr_1)):
        max_index = i
        for j in range(i+1, len(arr_1)):
            if arr_1[j] > arr_1[max_index]:
                max_index = j
        arr_1[i], arr_1[max_index] = arr_1[max_index], arr_1[i]

    return arr_1


input_array = [3, 2, 5, 7, 9, 1, 8, 6]
print(selection_sort_desc(input_array))
