from sys import argv
script, filetoread, filetowrite = argv
# %%
print(f"we're going to write into {filetowrite}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
# opens the file as an object 
print("Opening the file...")

# open(filename, 'w') + w-means to write 
target = open(filetoread,'r')
ex15 = target.read() 
target.close()

target2 = open(filetowrite,'w')
ex15x = target2.write(ex15) 
target2.close()

print("Writing to the file. Goodbye!")
# call the def truncate() method of a class open(filename,'w')
print("And finally, we close it")
