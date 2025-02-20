from practice_1_main import main
from searching import searching

def selector_function():

    """
    in order to keep running the program, even
    after finishing an action, we should set it
    into a loop, with condition to stop
    :return
    """
    while True:
        print("\nselect function to use")
        print("run: to run the program")
        print("search: to look for a value")
        print("exit: to stop program")

        choice = input("Enter choice here: ")

        if choice == "run":
            main()

        elif choice == "search":
            searching()
            #list_searched_elements()

        elif choice == "exit":
            print("finishing program")
            break
        else:
            print("invalid entrance")