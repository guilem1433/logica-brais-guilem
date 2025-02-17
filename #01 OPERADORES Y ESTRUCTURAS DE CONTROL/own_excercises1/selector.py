from practice_1 import main
from searching_function import searching

def selector_function():
    print("select function to use")
    print("run: to run the program")
    print("search: to look for a value")

    choice = input("Enter choice here: ")

    if choice == "run":
        main()

    elif choice == "search":
        searching()
    else:
        print("invalid entrance")
