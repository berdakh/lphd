# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 16:34:01 2017
@author: berdakh.abibullaev
"""
from sys import argv
script, first, user_name = argv
prompt = '->: '

print(f"Your first argument {first}")
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")

print(f"Do you like me {user_name}?",end = ' ')
# end is equal to '' but not \n 
# end without \n new line 

likes = input(prompt)
print(f"Where do you live {user_name}?",end = ' ')
lives = input(prompt)

print("What kind of a computer do you have ?",end = ' ')
computer = input(prompt)
print("""
   Alright, so you said {} about liking me.
   You live in {} Not sure where that is.
   And you have a {} computer. Nice.   
""".format({likes},{lives},{computer}))
