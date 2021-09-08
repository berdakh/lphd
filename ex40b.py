# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 08:34:37 2018

@author: Berdakh
"""
class Studydrills(object):
    defaulto = "this is a default song"

    def __init__(self,lyrics = defaulto):
        self.lyrics = lyrics 
        print('--- Constructor Initialize ---')        
    def print_the_song(self):
        for textline in self.lyrics:
            print(textline)        
#%% 
song = Studydrills(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I will stop right there"])  
    
 