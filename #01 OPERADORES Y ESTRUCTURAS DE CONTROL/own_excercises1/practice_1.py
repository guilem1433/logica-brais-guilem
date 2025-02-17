####comparators and combined operations.
"""
This is the first exercise I'm doing to learn,
how to use the functions and I will commit it

The program will coast a dynamic list where I will,
add values and I will use different types of conditionals
, and functionalities in order to practice how to apply them.
"""

#Menu

print(
    
)

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

print("entered elements:",the_number_list)

#conditionals based in numbers

sum_function = sum(the_number_list)
print("total of values:",sum_function)

if sum_function < 1500:
    print("*entrances are not matching the minimum quantities*")
if sum_function > 1500:
    print("*entrances are over the expected*")
if sum_function == 1500:
    print("*entrances are the expected values*")






