'''
Created on Jan 15, 2017

@author: griz
'''
import re

valuemap = {4000 : 'MMMM',
            3000 : 'MMM',
            2000 : 'MM',
            1000 : 'M',
            900: 'CM',
            800: 'DCCC',
            700: 'DCC',
            600: 'DC',
            500: 'D',
            400: 'CD',
            300: 'CCC',
            200: 'CC',
            100: 'C',
            90: 'XC',
            80: 'LXXX',
            70: 'LXX',
            60: 'LX',
            50: 'L',
            40: 'XL',
            30: 'XXX',
            20: 'XX',
            10: 'X',
            9: 'IX',
            8: 'VIII',
            7: 'VII',
            6: 'VI',
            5: 'V',
            4: 'IV',
            3: 'III',
            2: 'II',
            1: 'I',
            0: ''}

numeral_to_roman = []
roman_to_numeralDict = {}

class NonIntegerError(ValueError):
    pass

class NonValidRomanValueError(ValueError):
    pass

class OutOfRangeError(ValueError):
    pass

def to_roman(int_value):
    ''' convert from integer years to roman years. Returns string representation of the roman year'''

    if type(int_value) != int:
        raise NonIntegerError('Value is not an integer')
    if (not 0 < int_value < 5000):
        raise OutOfRangeError('number out of range, should be in 1-4999')
    return numeral_to_roman[int_value - 1]

def roman_to_numeral(roman_date):
    if (not roman_to_numeralDict.get(roman_date)):
        raise NonValidRomanValueError('Roman date is not valid')
    return roman_to_numeralDict.get(roman_date)

def build_lookup_dictionaries():
    for int_value in range(1,5000):
        orig_value = int_value
        millenium = int_value // 1000
        int_value = int_value - millenium * 1000
        century = int_value // 100
        int_value = int_value - century * 100
        decade = int_value // 10
        year = int_value - decade * 10
        romanLiteral = valuemap.get(millenium * 1000) + valuemap.get(century * 100) + valuemap.get(decade * 10) + valuemap.get(year)
        numeral_to_roman.append(romanLiteral)
        roman_to_numeralDict[romanLiteral] = orig_value



build_lookup_dictionaries()

if __name__ == '__main__':
    pass


