#####Variable number of arguments
#using *
def greet_variable(*names):
    for name in names:
        print(f"hello, {name}")
#the program will use the first element with each element we at the argument.
greet_variable("Python", "Javier", "Guillermo", "People")
