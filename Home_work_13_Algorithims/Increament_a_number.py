# Write a program that takes as input an array of digits encoding a
# non-negative decimal integer D and updates the array to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array
# to [1, 3, 0].
def increment_a_num(a):
    if len(a) == 1:
        return a[0]
    s = 0
    j = 1
    for i in range(len(a)-1, -1, -1):
        s = s + a[i]*j
        j *= 10

    result = s + 1 # 130
    result_list = []
    for k in str(result):
        result_list.append(int(k))

    return result_list


input = [9,2,0]
print(increment_a_num(input))
