from value_collector import the_number_list

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
