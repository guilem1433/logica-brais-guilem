#########for########3
#in order to create bucles
for i in range(25):
 print(i)
#knowing in this kind of exercises, the first number will the 0.

####while
# this will be a condition that will be executed,
#while the condition be true.
i = 0
while i <= 24:
    print(i)
    i += 1

####management of exceptions/try catch
try:
#    "algo" / "otro algo"
    3/3
except:
     print("existe un error")
finally:
    print("Se ha terminado el manejo de excepciones")
"""
The try function, will go directly to the
except function, in order to keep the program running.
And the finally function, will the end of the program, 
in this case. Because the finally element, will
be the action to notify that the management of the exception
has been completed.
"""


