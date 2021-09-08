from sys import argv
# from system imports argv library or module
script, filename = argv
# definition of the filename
txt = open(filename) # create an object file to open 
""" txt is now a TextIOWrapper class with the following default info
    <_io.TextIOWrapper name='ex15_sample.txt' mode='r' encoding='cp1252'>
"""
#at = txt.read(); # call the read method of an open object txt.
# open the filename
print(f"Here's your file {filename}:",end = '\n')
print(txt.read())
#load the .txt file and print its contents
txt.close()  
# %%
print("Type the filename again:")
file_again = input("> ") # ask the user input filename
# use the input method to ask the user to enter the txt filename again
txt_again = open(file_again) # create an object that contains infor about the file to be read 
print(txt_again.read())      # read it 
# run ex15.py ex15_sample.txt
txt_again.close() # close the object               
"""
To close a “file object” returned by the built-in function open() 
or by popen() or fdopen(), use its close() method.
"