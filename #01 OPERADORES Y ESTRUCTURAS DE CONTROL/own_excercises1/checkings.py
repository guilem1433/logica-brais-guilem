#conditionals based in numbers

def checkings (sum_function):
    if sum_function < 1500:
        print("*entrances are not matching the minimum quantities*")
    if sum_function > 1500:
        print("*entrances are over the expected*")
    if sum_function == 1500:
        print("*entrances are the expected values*")


