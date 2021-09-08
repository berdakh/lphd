# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:38:47 2017
@author: berdakh.abibullaev
"""
# %%
print("How old are you?", end = ' ')
# end =' ' tells print to not end the line with a newline character but go to the next line
age = int(input());

print("How tall are you?", end = ' ')
height = int(input());

print("How much do you weigh?", end = ' ');
weight = int(input());

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
#age = int(input());

#%%
def print_full_name(a, b):
    print(f"Hello {a} {b}. You just delved into python")
    

print_full_name("Berdakh","Abibullaev")