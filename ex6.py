# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:09:07 2017

@author: berdakh.abibullaev
"""
types_of_people = 10;
x = f"There are {types_of_people} types of people."
# %%
binary = "binary"
do_not = "don't"

y = f"Those who know {binary} and those who {do_not}."

print(x), print(y)

print(f"I said: {x}")
print(f"I also said: {y}\n")

#print(f"\n {x} + {y}\n")

hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"
# this is another way of formatting - that is - instead of putting "f" in front
# we can defind .format() after the string.
print(joke_evaluation.format(hilarious))

# we can also do:
print("Isn't that joke so funny?! {}".format(hilarious))
# %%
w = "This is the left side of ..."
e = "a string with a right side."
print(w+e)