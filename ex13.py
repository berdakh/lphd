from sys import argv # argv-argument vector/variable 
# read the WYSS section for how to run this
script, first, second, third = argv # we require four variables
print(">>>> argv = ",repr(argv)) 
# repr() is like a disp() in matlab
print("The script is called: ",(script))
print("Your first variable: ", int(first))
print("Your second variable is:",second)
print("Your third variable is:", third)

#run ex13.py first 2nd 3rd
fourth = input("This one is the fourth input ")
print("Your forth input is:", fourth)