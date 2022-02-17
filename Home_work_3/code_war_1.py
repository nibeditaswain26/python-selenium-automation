# Write a function to convert a name into initials.
# This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F
"""
full_name = input("enter your full name: ")
list_name = full_name.split()
print(list_name)
first_name = list_name[0]
last_name = list_name[1]
print(first_name[0].upper(), ".", last_name[0].upper())
"""
"""
full_name = input("enter your full name: ")
list_name = full_name.split()
# print(list_name)


def initial_name():
    final_initial_name = " "
    for i in range(0, len(list_name)):
        first_last_name = list_name[i]
        letter = first_last_name[0]

        if i == len(list_name)-1:
            final_initial_name = final_initial_name + letter
        else:
            final_initial_name = final_initial_name + letter + "."
    return final_initial_name.upper()


my_name = initial_name()
print(my_name)
"""
full_name = input("Enter your full name: ")
split_name = full_name.split()
first_name = split_name[0]
last_name = split_name[1]


def init_name(f_name, l_name):
    return print(f_name[0].upper(), ".", l_name[0].upper())


init_name(first_name, last_name)







