# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and
# 2 odd digits (3 and 5)
# O(n)
def count_odd_even(num_1):
    odd_count = 0
    even_count = 0
    odd_numbers = []
    even_numbers = []

    for i in num_1:
        if int(i) % 2 == 0:
            even_count += 1
            even_numbers.append(i)
        else:
            odd_count += 1
            odd_numbers.append(i)
    even_odd_list = [odd_count, odd_numbers, even_count, even_numbers]
    return even_odd_list


given_number = input("enter a number: ")
total_count = count_odd_even(given_number)
print(f"There are {total_count[0]} odd digits {total_count[1]} and"
      f"{total_count[2]} even digits {total_count[3]}")
