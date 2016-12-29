'''
Created on 27 dec. 2016

@author: radi961
'''
import os
import glob
import re
from src import test


def extractMilleniumString(date):
    patternMillenium = r'^M*C{0,1}M{1,1}'
    match = re.match(patternMillenium, date)
    if (match == None):
        return date
    else:
        if (date[match.end()] == 'C'):
            raise ValueError("Invalid syntax")
        else:
            return date[match.end():]
    


def extractCenturiesString(date):
    patternMillenium = r'^C{0,1}D{1,1}C{0,3}'
    match = re.match(patternMillenium, date)
    if (match == None):
        return date
    else:
        if (date[match.end()] == 'C'):
            raise ValueError("Invalid syntax")
        else:
            return date[match.end():]


def extractDecadesString(date):
    patternMillenium = r'^X{0,1}L{1,1}X{0,3}'
    match = re.match(patternMillenium, date)
    if (match == None):
        return date
    else:
        if (date[match.end()] == 'C'):
            raise ValueError("Invalid syntax")
        else:
            return date[match.end():]


def extractYearsString(date):
    patternMillenium = r'^I{0,1}V{1,1}I{0,3}'
    match = re.match(patternMillenium, date)
    if (match == None):
        return date
    else:
        if (match.end() < len(date)):
            raise ValueError("Invalid syntax")
        else:
            return date[match.end():]


#def isRomanDateWellFormed(date):
#    remaningString = extractMilleniumString(date)
#    print(remaningString)
#    remaningString = extractCenturiesString(remaningString)
#    print(remaningString)
#    remaningString = extractDecadesString(remaningString)
#    print(remaningString)
#    remaningString = extractYearsString(remaningString)
    
def isRomanDateWellFormed(date):
    pattern = r'^M*(CM|CD|DC{0,3}|C{0,3}|)(XC|XL|LX{0,3}|X{0,3})(IX|IV|VI{0,3}|I{0,3}|)'
    
    match = re.match(pattern, date)
    print("Initial string " + date)
    print(date[match.start():match.end()])
    if (match == None or match.end() != len(date)):
        return False
    else:
        return True
    
def transform_phone_number(number):
    phonePattern = re.compile(r'''\D* #prefix
        (\d{3})
        \D*
        (\d{3})
        \D*
        (\d{4})
        \D*
        (\d{4})*
        $''', re.VERBOSE|re.MULTILINE)
    
    if (phonePattern.search(number) != None):
        return phonePattern.search(number).groups()
    else:
        raise ValueError('Phone number is unparsable')
    

if __name__ == "__main__":
    #some regular expression play
    s = '100 NORTH MAIN ROAD'
    print(re.sub('[ ][R][O][A][D]', ' RD.', s))
    
    s = '100 NORTH ROAD MAIN ROAD'
    print(re.sub('[ ][R][O][A][D]', ' RD.', s))
    
    s = '100 NORTH ROAD MAIN ROAD'
    print(re.sub(r'\bROAD\b', 'RD.', s))
    
    #matching roman letters exercise
    
    testSample = 'MCMC'
    
    sample = 'MCMXLVI'
    sample2 = 'MDCCCLXXXVIII'
    
    test.assert_true(isRomanDateWellFormed('MCMXLVI'))
    test.assert_true(isRomanDateWellFormed('MDCCCLXXXVIII'))
    test.assert_true(isRomanDateWellFormed('MDCCLXXXVII'))
    test.assert_true(isRomanDateWellFormed('MDCCLXXXVII'))
    test.assert_true(isRomanDateWellFormed('MCM'))
    #test.assert_true(isRomanDateWellFormed('MDCCCZ'))

    print(transform_phone_number('800-555-1212'))
    print(transform_phone_number('800 555 1212'))
    print(transform_phone_number('800.555.1212'))
    print(transform_phone_number('1-800-555-1212'))
    print(transform_phone_number('(800) 555-1212'))
    print(transform_phone_number('800-555-1212-1234'))
    print(transform_phone_number('800-555-1212x1234'))
    print(transform_phone_number('800-555-1212 ext. 1234'))
    print(transform_phone_number('work 1-(800) 555.1212 #1234'))
    
    