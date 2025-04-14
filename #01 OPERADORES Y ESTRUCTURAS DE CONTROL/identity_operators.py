##########Identity operators############
#to see the value of the memory location of the element
###   IS

element_to_compare = 67484.934984
other_one = 456789078
comparison1 = element_to_compare is other_one
print("Element no1 to be compared is:",comparison1)

#The moment, I changed the value of variable, the comparator is
#going to tell me "the value is the same."
element_to_compare2: int = 70987
other_one2 = 87976
element_to_compare2 = other_one2
comparison2 = element_to_compare2 is not other_one2
print("element to be compared no2 is:", comparison2)


