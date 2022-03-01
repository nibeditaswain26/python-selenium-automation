# You've just moved into a perfectly straight street
# with exactly n identical houses on either side of the
# road. Naturally, you would like to find out the house
# number of the people on the other side of the street.
# The street looks something like this:
# 1|   |6
# 3|   |4
# 5|   |2
given_house_no = int(input("enter your house number: "))
street_length = int(input("enter your length of the street: "))
# Total_no_of_house = street_length * 2
start_house_number = 1
opposite_house_number = (2 * street_length) - (given_house_no - start_house_number)
print(f"for your house number: {given_house_no}, opposite house number is: {opposite_house_number}")