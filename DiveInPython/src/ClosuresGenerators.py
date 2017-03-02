'''
Created on 27 dec. 2016

@author: radi961
'''
import os
import glob
import re

def plural(noun):
    for match, apply in get_rules('plural4-rules.txt'):
        if (match(noun)):
            return apply(noun)
            
#closures
def build_match_and_apply(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return matches_rule, apply_rule      

#generator example

def get_rules(filename):
    with open(filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield build_match_and_apply(
                pattern, search, replace)


if __name__ == "__main__":
    print(plural('test'))
    print(plural('boy'))
    

    