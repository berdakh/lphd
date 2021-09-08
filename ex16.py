from sys import argv
script, filename = argv
# %%
print(f"we're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
# opens the file as an object 
print("Opening the file...")

# open(filename, 'w') + w-means to write 
target = open(filename,'w') 
#object: <_io.TextIOWrapper name='ex15.py' mode='w' encoding='cp1252'>
# truncate/erase everything 
print("Truncating the file. Goodbye!")
# call the def truncate() method of a class open(filename,'w')
target.truncate()

# %% 
print("Now I am going to ask you for three lines.")

# get each separate line text input
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file.")

# %% 
x = f"{line1}\n{line2}\n{line3}"
target.write(x)

#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
print("And finally, we close it")
target.close()
