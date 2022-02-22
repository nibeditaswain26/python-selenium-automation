# Given a random non-negative number,
# you have to return the digits of this number within an array in reverse order.
# 12345 = [5,4,3,2,1]
given_number = int(input("Enter a random number: "))
converted_list = []
while given_number != 0:
    num = given_number % 10
    converted_list.append(num)
    # print(given_number)
    given_number = int(given_number / 10)

print(converted_list)
