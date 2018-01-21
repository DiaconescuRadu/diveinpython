'''
Created on 27 dec. 2016

@author: radi961
'''
import os
import glob
import re
#from src import test
import argparse

def getHref(line):
    hRefPattern = re.compile(r'''<a\ href\="
        ([^"]+)
        ''', re.VERBOSE)
   
    if (hRefPattern.search(line) != None):
        return hRefPattern.search(line).groups()[0]
    else:
        raise ValueError('Line does not contain HRef')


def getImgHref(line):
    imgRefPattern = re.compile(r'''\ src\="
        ([^"]+)
        ''', re.VERBOSE)
   
    if (imgRefPattern.search(line) != None):
        return imgRefPattern.search(line).groups()[0]
    else:
        raise ValueError('Cannot find img reference')
    
def updateHref(line):
    return line.replace(getHref(line), getImgHref(line)).replace('/s400/', '/s0/')

def updateHrefInFile(inputFileName, outputFileName):
    with open(outputFileName, mode='w', encoding='utf-8') as outputFile:
        with open(inputFileName, encoding='utf-8') as inputFile:
            for line in inputFile:
                try:
                    outputFile.write(updateHref(line))
                except:
                    outputFile.write(line)

if __name__ == "__main__":
    #testMessage0 = '<a href="http://picasaweb.google.com/lh/photo/ByAio7_Xsly0zUn24d8xAg?feat=embedwebsite" target="_blank"><img class="aligncenter" style="border: 2px solid white;" src="http://lh6.ggpht.com/_FBUGsY3BqXU/SrphVd6u1BI/AAAAAAAAC2Y/LOw5_aCs6xI/s400/Bucuresti%20noaptea.%20Timpul%202.jpg" alt="Bucuresti. Noaptea. Timpul. Ceasul. Dambovita" width="400" height="311" /></a>'
    #testMessage1 = '<p style="text-align: justify;">Dambovita nu e o apa lina si cristalina. Are miros si nu e frumos mirositoare. Dupa atatea indiguiri si-a uitat cu siguranta amintirile izvorului. Cateodata insa <strong>timpul </strong>izvoraste din ea.</p><p style="text-align: center;"><a href="http://picasaweb.google.com/lh/photo/ByAio7_Xsly0zUn24d8xAg?feat=embedwebsite" target="_blank"><img class="aligncenter" style="border: 2px solid white;" src="http://lh6.ggpht.com/_FBUGsY3BqXU/SrphVd6u1BI/AAAAAAAAC2Y/LOw5_aCs6xI/s400/Bucuresti%20noaptea.%20Timpul%202.jpg" alt="Bucuresti. Noaptea. Timpul. Ceasul. Dambovita" width="400" height="311" /></a>'
    #testMessage2 = '<a href="http://picasaweb.google.com/lh/photo/I7g9wF0K0BLm9KPlnLicdg?feat=embedwebsite" target="_blank"><img class="aligncenter" style="border: 2px solid white;" src="http://lh3.ggpht.com/_FBUGsY3BqXU/SrphVVfTi4I/AAAAAAAAC2U/zr4L050UDtU/s400/Bucuresti%20noaptea.%20Timpul%201.jpg" alt="Bucuresti. Noaptea. Timpul. Ceasul. Dambovita" width="400" height="312" /></a></p><p style="text-align: justify;">P.S. Daca vi se pare ca am o anumita <em>stare</em>, apoi sa stiti ca intre un munte si celalalt impart doar 4 zile de Bucuresti! Iar muntele asta care vine nu e unul oarecare. E unul ce s-a lasat asteptat si bine-a facut. Acum sunt pregatita pentru el. Si am emotii, mai, am emotii! Ma gandeam ca nu voi putea dormi noaptea de dinainte, dar cred ca nu mai pot dormi de pe-acum... <em>Fagarasul </em>asta, cum sa va zic, simt ca ma asteapta :)</p>'
 
    #test.assert_true('/s0/' in getHref(updateHref(testMessage0)))
    #test.assert_true('/s0/' in getHref(updateHref(testMessage1)))
    #test.assert_true('/s0/' in getHref(updateHref(testMessage2)))
    
    parser = argparse.ArgumentParser(description="Replace hrefs in input file with img src and update resolution")
    parser.add_argument("-i", "--input", help="Name of the input file")
    parser.add_argument("-o", "--output", help="Name of the generated output file")
    
    args = parser.parse_args()
    updateHrefInFile(args.input, args.output)
    
    
    
    
    

    