####comparators and combined operations.
"""
This is the first exercise I'm doing to learn,
how to use the functions and I will commit it

The program will coast a dynamic list where I will,
add values and I will use different types of conditionals
, and functionalities in order to practice how to apply them.
"""
#Menu

from checkings import checkings_function
from searching_valuecollector import collector_of_values

#print("main: function to enter values\n search: to look for value")

def main():
    the_number_list = collector_of_values()
    print("entered values:",the_number_list)

    total = sum(the_number_list)
    print("The total of values is:", total)

    checkings_function(total)

if __name__=="__main__":
    main()

