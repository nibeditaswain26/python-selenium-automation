# Compute the sum of digits in all numbers from 1 to n. When a user enters a number n,
# find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
# solution_1 O(n)
"""
num_1 = int(input("enter the value of num_1: "))
result = 0
if num_1 != 0:
    for i in range(1, num_1 + 1):
        result = result + i
print(f"Sum of digits from 1 to {num_1} is: ", result)
"""
# solution_2 O(1)
num_1 = int(input("enter the value of num_1: "))
sum_result = num_1 * (num_1 + 1) / 2
print(f"Sum of digits from 1 to {num_1} is: ", sum_result)


