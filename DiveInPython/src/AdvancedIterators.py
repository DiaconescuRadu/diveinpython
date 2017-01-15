'''
Created on Jan 14, 2017

@author: griz
'''

import re
import itertools

def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
        ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation


def my_experiments(puzzle):
    print(puzzle)
    words = re.findall('[A-Z]+', puzzle)
    print(words)
    
    first_set = {1, 3}
    second_set = {2}
    print(first_set - second_set)

if __name__ == '__main__':
    import sys
    
    my_experiments(sys.argv[1])
    
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)