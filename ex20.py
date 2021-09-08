from sys import argv
script, input_file = argv
# %%
def print_all(f):
    # this function take f-object from f = open(filename)
    # then reads it wih f.read() then prints it with print()
    print(">>> f=",f)
    print(f.read())
    print("<<< f=",f)

def rewind(f):
    # f is an object from f = open(filename)
    # seek methods finds start of a line 
    f.seek(0) # seek method scans character by character 'wise
    # start of stream-offset should be zero or positive
    
def print_a_line(line_count, f):        
    print(line_count, f.readline())    
    
# %%
#input_file = 'ex15_sample.txt'
current_file = open(input_file)
print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# if you don't rewind the after reading the file End of File thus you see nothing
rewind(current_file) 

# %%
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
# %%
current_line += 1
#print(f"This is a current line: {current_line}")
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# %% 
print(current_file.seek(0))
# current_file - <_io.TextIOWrapper name='ex15_sample.txt' mode='r' encoding='cp1252'>
# %%
# readline method - reads file contents line-by-line
# while open method reads all the contents 
#print(len(current_file.readline()))
#print(current_file.readline())
