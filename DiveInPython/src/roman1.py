'''
Created on Jan 15, 2017

@author: griz
'''
from orca.punctuation_settings import cent
import re

valuemap = {3000 : 'MMM',
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

numeralToIntDict = {value : key for key,value in valuemap.items()}

def to_roman(int_value):
    ''' convert from integer years to roman years. Returns string representation of the roman year'''

    if type(int_value) != int:
        raise NonIntegerError('Value is not an integer')
    if (int_value >= 4000 or int_value <= 0):
        raise OutOfRangeError('number out of range, should be in 1-3999')
    millenium = int_value // 1000
    int_value = int_value - millenium * 1000
    century = int_value // 100
    int_value = int_value - century * 100
    decade = int_value // 10
    year = int_value - decade * 10
    return valuemap.get(millenium * 1000) + valuemap.get(century * 100) + valuemap.get(decade * 10) + valuemap.get(year)

def isRomanDateWellFormed(date):
    pattern = r'^M{0,3}(CM|CD|DC{0,3}|C{0,3}|)(XC|XL|LX{0,3}|X{0,3})(IX|IV|VI{0,3}|I{0,3}|)'
    
    match = re.match(pattern, date)
    print("Initial string " + date)
    print(date[match.start():match.end()])
    if (match == None or match.end() != len(date)):
        return False
    else:
        return True

def roman_to_numeral(roman_date):
    if (not roman_date):
        raise NonValidRomanValueError('Roman date is not valid')
    if (not isRomanDateWellFormed(roman_date)):
        raise NonValidRomanValueError('Roman date is not valid')
    
    regex = re.compile(r'^(M{0,3})(CM|CD|DC{0,3}|C{0,3}|)(XC|XL|LX{0,3}|X{0,3})(IX|IV|VI{0,3}|I{0,3}|)')
    returnInteger = 0
    regex_match = regex.match(roman_date)
    for i in range(4,0,-1):
        returnInteger = returnInteger + numeralToIntDict.get(regex_match.group(i))
    return returnInteger
    
    

class OutOfRangeError(ValueError):
    pass    

if __name__ == '__main__':
    print(to_roman(1))
    print(roman_to_numeral('I'))
    pass

class NonIntegerError(ValueError):
    pass


class NonValidRomanValueError(ValueError):
    pass
