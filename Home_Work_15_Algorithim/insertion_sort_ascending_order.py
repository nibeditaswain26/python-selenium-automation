def insertion_sort_asc(arr_1):
    for i in range(1, len(arr_1)):
        key = arr_1[i]
        j = i - 1
        while j >= 0 and key < arr_1[j]:
            arr_1[j+1] = arr_1[j]
            j -= 1
        arr_1[j + 1] = key

    return arr_1


input_array = [3, 2, 5, 7, 9, 1, 8, 6]
print(insertion_sort_asc(input_array))