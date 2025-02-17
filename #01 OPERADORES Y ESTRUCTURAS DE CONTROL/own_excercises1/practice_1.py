####comparators and combined operations.
"""
This is the first exercise I'm doing to learn,
how to use the functions and I will commit it

The program will coast a dynamic list where I will,
add values and I will use different types of conditionals
, and functionalities in order to practice how to apply them.
"""
#Menu

<<<<<<< HEAD
<<<<<<< HEAD
from checkings import checkings_function
=======
>>>>>>> guilem1433-logica-brais-guilem/main
=======
=======
from checkings import checkings_function
>>>>>>> 05e1a69 (finishing the main function)
>>>>>>> 53c4827 (finishing the main function)
from collector_of_values import collector_of_values
from searching_function import searching

print("main: function to enter values\nsearch: to look for value")

if __name__=="__main__":
    main()
    #__name__ will ensure that the function will run when called.

if __name__=="__search__":
    searching()

#print("main: function to enter values\nsearch: to look for value")

def main():
    the_number_list = collector_of_values()
    print("entered values",the_number_list)

    total = sum(the_number_list)
    print("The total of values is:", total)

<<<<<<< HEAD
    checkings_function(total)
=======
    checkings_function(total)

<<<<<<< HEAD
if __name__=="__main__":
    main()





>>>>>>> 53c4827 (finishing the main function)
=======
>>>>>>> d6d999c (not being able to write in the selector function)
