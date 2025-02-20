the_number_list = []

def collector_of_values():

    print("enter numbers for the list:")

    while True:
        general_user_input = input()
        if general_user_input.lower() == "done":
            break
        try:
            values = int(general_user_input)  # to transform all value to ints
            the_number_list.append(values)
        except ValueError:
            print("Please, enter right values")

    return the_number_list

def checkings_function (sum_function):
    if sum_function < 1500:
        print("*entrances are not matching the minimum quantities*")
    if sum_function > 1500:
        print("*entrances are over the expected*")
    if sum_function == 1500:
        print("*entrances are the expected values*")
    if sum_function < 1000:
        sum_function += 500
        print("over-plus added")
    if sum_function > 2000:
        sum_function -= 1000
        print("over-plus diminished")








