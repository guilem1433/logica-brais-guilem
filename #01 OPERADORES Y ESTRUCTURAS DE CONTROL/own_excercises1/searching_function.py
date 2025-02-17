from collector_of_values import collector_of_values

def searching():
    the_number_list = collector_of_values()
    values_to_be_searched = input(print("enter the values to be searched"))

    try:
        if values_to_be_searched in the_number_list:
            print(values_to_be_searched,"are in the list")
        else:
            print(values_to_be_searched, "values to be searched are not in the list")

    except ValueError:
        print("Please, enter a valid element")
