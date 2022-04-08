def insertion_sort_desc(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i -1
        while j >= 0 and key > a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

    return a

input_array = [3, 2, 5, 7, 9, 1, 8, 6]
print(insertion_sort_desc(input_array))