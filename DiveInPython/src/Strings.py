'''
Created on 27 dec. 2016

@author: radi961
'''
import os
import glob

if __name__ == "__main__":
    #unicde stuff, file has to be saved in UTF-8
    s = '深入 Python'
    print(len(s))
    stringList = ['asd', 'bcd']
    print('{0[0]} {0[1]}'.format(stringList))
    
    s1 = '''string on 
        several lines'''
    
    print(s1.splitlines())
    
    #split and dictionary from list of lists
    
    query = 'user=pilgrim&database=master&password=PapayaWhip'
    
    elementList = query.split('&')
    print(elementList)
    
    elementListList = [f.split('=') for f in elementList]
    
    print(elementListList)
    dictionary = dict(elementListList)
    
    print(dictionary)
    
    #String slicing 
    
    s = 'Test string'
    print(s[0:4])
    print(s[5:])
    
    #bytes MAGIC
    
    b = b'asd\x32\x34'
    
    print(b[0])
    
    #bytearrays
    
    barr = bytearray(b)
    barr[0] = 33
    print(barr)
    
    #encoding / decoding
    
    s = '深入 Python'
    barr = s.encode(encoding='utf-8', errors='strict')
    print(len(barr))
    
    s1 = barr.decode('utf-8', 'strict')
    
    print(s1)