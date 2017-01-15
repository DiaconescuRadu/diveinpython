'''
Created on 28 dec. 2016
The Story:

Aliens from Kepler 27b have immigrated to Earth! They have learned English and go to our stores, eat our food, dress like us, ride Ubers, use Google, etc. However, they speak English a little differently. Can you write a program that converts their Alien English to our English?
Task:

Write a function converting their speech to ours. They tend to speak the letter a like o and o like a u. NOTE: There is an issue with this kata when it is solved in python 2x. The issue turned out to be easy to fix but there is a bug in the re-publishing system preventing the kata from being updated. The issue has been posted on Github.

@author: radi961
'''
from _functools import reduce
import re
from src import test
    
def convert(st):
    dict = {"a" : "o",
            "o": "u"}
    regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
    
    
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], st)

if __name__ == "__main__":
    test.assert_equals(convert('codewars'), 'cudewors')
    #test.assert_equals(convert('hello'), 'hellu')