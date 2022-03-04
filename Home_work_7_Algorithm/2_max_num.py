# Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.
# O(1)
def max_value(num_1, num_2, num_3):
    if num_1 > num_2 and num_1 > num_3:
        return num_1
    if num_2 > num_1 and num_2 > num_3:
        return num_2
    else:
        return num_3


value_1 = int(input("enter your 1st value: "))
value_2 = int(input("enter your 2nd value: "))
value_3 = int(input("enter your 3rd value: "))
print("max number from 3 values is: ", max_value(value_1, value_2, value_3))
