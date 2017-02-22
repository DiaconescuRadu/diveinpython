'''
Created on 28 dec. 2016

@author: radi961
'''
from _functools import reduce
from src import test

def combine(*args):
    combinedList = []
    inputLists = []
    for list in args:
        inputLists.append(list)
    
    while not lists_empty(inputLists):
        pop_lists(inputLists, combinedList)
    
    return combinedList

def lists_empty(inputLists):
    empty = True
    for list in inputLists:
        if (len(list)):
            empty = False
            break
    return empty
        
def pop_lists(inputLists, combinedList):
    for list in inputLists:
        if (len(list)):
            combinedList.append(list.pop(0))

if __name__ == "__main__":
    print(combine(['r', {'d': 7}, {'w': 9}, {'w': 9}, 1, 1, 8, 'r'], [7, {'r': 9}, 'd', 7, 'w'], ['w', 7, {'o': 6}, 1, {'c': 1}, 7, 1], [7, 'd', 8, 8, {'w': 9}], [1, 'd', 1, 1, {'d': 7}]))
    test.assert_equals(combine(['a', 'b', 'c'], [1, 2, 3]), ['a', 1, 'b', 2, 'c', 3])
    test.assert_equals(combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]), ['a', 1, 'b', 2, 'c', 3, 4, 5])
    test.assert_equals(combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]),['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5])
    test.assert_equals(combine([{ 'a': 1 }, { 'b': 2 }], [1, 2]),[{"a":1},1,{"b":2},2])
    test.assert_equals(combine([{ 'a': 2, 'b':1 }, { 'a': 1, 'b': 2 }], [1, 2, 3, 4],[5,6],[7]), [{"a":2,"b":1},1,5,7,{"a":1,"b":2},2,6,3,4])