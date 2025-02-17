####comparators and combined operations.
"""
This is the first exercise I'm doing to learn,
how to use the functions and i will commit it
"""

the_number_list = []

print("enter numbers for the list:")

while True:
    general_user_input = input()
    if general_user_input.lower() == "done":
        break
    try:
        values = int(general_user_input) #to transform all value to ints
        the_number_list.append(values)
    except ValueError:
        print("Please, enter right values")

print(the_number_list)