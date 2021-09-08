# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:07:48 2017

@author: berdakh.abibullaev
"""
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))

print(formatter.format(
        "Try your",
        "Own text here",
        "Maybe a poem",
        "Or a song about fear"              
        ))


print("""
        There's something going on here.
        With the three double-quotes.
        We'll be able to type as much as we like.
        Even 4 lines if we want, or 5, or 6      
""");


