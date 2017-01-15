'''
Created on 28 dec. 2016

@author: radi961
'''
from _functools import reduce
import re
from src import test

def iq_test(numbers_string):
    numbers = re.findall('[0-9]+', numbers_string)
    even_numbers = [number for number in numbers if (int(number) % 2) == 0]
    odd_numbers = [number for number in numbers if (int(number) % 2) == 1]
    if (len(even_numbers) == 1):
        return numbers.index(even_numbers[0]) + 1
    if (len(odd_numbers) == 1):
        return numbers.index(odd_numbers[0]) + 1
    return 1
    

if __name__ == "__main__":
    test.assert_equals_int(iq_test("2 4 7 8 10"),3)
    test.assert_equals_int(iq_test("1 2 2"), 1)
