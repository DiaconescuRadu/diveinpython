'''
Created on 28 dec. 2016

@author: radi961
'''

def describe(s):
    print(s)
    
def it(s):
    print(s)
    
def assert_equals(actualValue, expectedValue):
    print(actualValue + " " + expectedValue)
    if (not actualValue == expectedValue):
        raise(ValueError(' Values are not equal  actual ' + actualValue + ' expected ' + expectedValue))