

# for i in range(26):
#     i = 10
#     i += 1
#     print(i)
# #anothe way

# for the_range in range(10,56):
#     print(the_range )
#
# ####only pairs
#
# for the_range in range(10,56):
#     if the_range % 2 == 0:
#         print(the_range )
# ###no 16 nor 3 multiples

for the_range in range(10,56):
    if the_range % 2 == 0 and the_range % 3 != 0 and the_range != 16:
        print(the_range )
