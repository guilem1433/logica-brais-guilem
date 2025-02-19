from collector_of_values import collector_of_values

def list_searched_elements():

    searched_elements = []
    while True:
        input_searched_elements = input()
        if input_searched_elements == "done":
            break
        try:
            searched_data = int(input_searched_elements)
            searched_elements.append(searched_data)
        except ValueError:
            print("enter, valid elements")
    return searched_elements

def searching():

    the_number_list = collector_of_values()

    values_to_be_searched = input(print("enter the values to be searched"))

    try:
        values_to_be_searched = int(values_to_be_searched)
        if values_to_be_searched in the_number_list:
            print(values_to_be_searched,"are in the list")
        else:
            print(values_to_be_searched, "values to be searched are not in the list")
    except ValueError:
        print("Please, enter a valid element")