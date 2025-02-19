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

searched_elements = []

def searching():
    print("enter the values:")

    values_to_be_searched = input()

    while True:

        input_searched_elements = input()
        if input_searched_elements == "done":
            break

        try:
            searched_data = int(input_searched_elements)
            searched_elements.append(searched_data)

        except ValueError:
            print("enter, valid elements")

    try:
        values_to_be_searched = int(values_to_be_searched)
        if values_to_be_searched in the_number_list:
            print(values_to_be_searched,"are in the list")
        else:
            print(values_to_be_searched, "values not in the list")
    except ValueError:
        print("Please, enter a valid element")


    return searched_elements
