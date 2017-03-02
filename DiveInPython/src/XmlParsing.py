'''
Created on Feb 23, 2017

@author: griz
'''

import xml.etree.ElementTree as etree

if __name__ == '__main__':
    #doing some xml processing
    
    with open('input.xml', encoding='utf-8') as input_xml:
        tree = etree.parse(input_xml)
        root = tree.getroot()
        
        print(root.attrib)
        
        print(root.findall('{http://www.w3.org/2005/Atom}entry'))
        
        #getting the first entry
        
        entry1 = root.find('{http://www.w3.org/2005/Atom}entry')
        print(entry1.find('{http://www.w3.org/2005/Atom}title'))
        
        #searching through all the subelements
        
        links = tree.findall('.//{http://www.w3.org/2005/Atom}link')
        
        print(list(link.attrib for link in links))
        