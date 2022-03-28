# Your input is an array of integers, and you have to reorder its entries so
# that the even entries appear first. You are required to solve it without allocating
# additional storage (operate with the input array).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
def even_first(l_1):
    count = 0
    for num in range(len(l_1)):
        print("num_1= ", num)
        if l_1[num] % 2 == 0:
            print("Index for even num is and i is", num, count)
            for num1 in range(num, count, -1):
                l_1[num1-1], l_1[num1] = l_1[num1], l_1[num1-1]
                print(l_1)
            count = count + 1
    return l_1


input_list = [7, 3, 5, 6, 4, 10, 3, 2]
print(even_first(input_list))

