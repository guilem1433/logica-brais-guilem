####In order to handle exceptions in a code to avoid problems
from decimal import DivisionByZero

try:
    print(10/0)
except DivisionByZero: #catch
    print("And error has occurred")
finally:
    print("Error handling if finished")