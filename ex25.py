def break_words(stuff):
    """ This function will break up words for us."""
    words = stuff.split(' ')    
    return words

def sort_words(words):
    """ Sort the words."""
    return sorted(words)

def print_first_word(words):
    """ Prints the first word after popping it off."""
    word = words.pop(0) # it is actually is a method :)) 
    # equivalent in Matlab would be pop(words(1)):)
    print(word)

def print_last_word(words):
    """ Prints the last word after after popping it off.""" 
    word = words.pop(-1) # -1 is equivalent to (end) in matlab 
    print(word)
    
def sort_sentence(sentence):
    """ This takes in a full sentence and returns the sorted words"""
    words = break_words(sentence) # first break the words 
    return sort_words(words) # then call the function to sort it

def print_first_and_last(sentence):
    """ Prints the first and last words of the sentence."""
    words = break_words(sentence) # first break the words 
    print_first_word(words) # using the indicies print first/last words 
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """ Sorts the words then prints the first and last one. """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)    
    
"""
import ex25.py into python (assuming you are working on terminal without any IDE
and we can call it using for instance ex25.print_first_and_last(sentence)
whatever comes after the dot is the function defition. 

"""