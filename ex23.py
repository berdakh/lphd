# it is the same as *from sys import argv
#import sys
#script, input_encoding, error = sys.argv # sys.argv can be multiple input variables
# %%
# =============================================================================
# this is going to be an example of a block comment 
# =============================================================================
input_encoding = 'utf-8'
error = 'strict'
def main(language_file, encoding, errors):
    # pass the language_file object and read it line by line
    line = language_file.readline() 
    print(">>>>> line",line)       
    if not(line):  
        print(">>> Line is empty <<<")
    elif line: # if text exists in each line of the text then 
        print(">>> line exists <<<")
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
# %         
def print_line(line, encoding, errors):    
    # strip() - Return a copy of the string 
    # with the leading and trailing characters removed
    stripped_line = line.strip()   
    # given a line of a text (stripped) 
    # use specific encoding using encode()
    raw_bytes = stripped_line.encode(encoding, errors = errors)     
    # then try to decode the encoded text again
    decoded_string = raw_bytes.decode(encoding, errors = errors)        
    # print the results 
    print("Encoded text with UTF-8 <<===>>> decoded text")
    print(raw_bytes, "<===>", decoded_string)  

# %% the main function calling is located here 
# 1) we open the text file (returns the string object)    
languages = open("languages.txt", encoding = "utf-8")
# 2) we pass it to the main() to read, encode, decode and print results
line = main(languages,input_encoding,error)        
