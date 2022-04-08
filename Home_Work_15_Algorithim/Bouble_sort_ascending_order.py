def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a


input_array = [3, 2, 5, 7, 9, 1, 8, 6]
print(bubble_sort(input_array))