##Functions inside others functions

def outer_function():
    def inside_function():
        print("print a function")
    inside_function()

outer_function()

"""
In order to use function that are inside 
other function, you must call the inner one in the 
inside the outer one; then call it.

This may change, language to language.
"""