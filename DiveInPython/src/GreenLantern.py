'''
Created on 28 dec. 2016

@author: radi961
'''
from src import test
from _functools import reduce

def yellow_be_gone(color_name_or_code):
    #creating a dictionary for colors
    
    colorMapYellows = {'Gold' : 'ForestGreen',
        'Khaki' : 'LimeGreen',
        'LemonChiffon' : 'PaleGreen',
        'LightGoldenRodYellow' : 'SpringGreen',
        'LightYellow' : 'MintCream',
        'PaleGoldenRod' : 'LightGreen',
        'Yellow' : 'Lime' }
    
    colorMapLowerCase = {k.lower():v for (k,v) in colorMapYellows.items()}
    
    inputString = str(color_name_or_code)
    if (color_name_or_code[0] == '#'):
        #doing color code processing
        red = (int(color_name_or_code[1:3], 16), color_name_or_code[1:3])
        green = (int(color_name_or_code[3:5], 16), color_name_or_code[3:5])
        blue = (int(color_name_or_code[5:7], 16), color_name_or_code[5:7])
        
        if (red > blue and green > blue ):
            #initial list
            colorList = [red , green, blue]
            orderedColorList = sorted(colorList, key=lambda color: color[0])
            return('#' + orderedColorList[0][1] + orderedColorList[2][1] + orderedColorList[1][1])
        else:
            return color_name_or_code
    else:
        if (inputString.lower() in colorMapLowerCase.keys()):
            return colorMapLowerCase[inputString.lower()]
        else:
             return color_name_or_code
    

if __name__ == "__main__":
    test.describe("Basic HTML color names tests")
    test.it("A yellow color name in all lower case")   
    test.assert_equals(yellow_be_gone("lemonchiffon"), "PaleGreen")
    test.it("A yellow color name in all upper case")   
    test.assert_equals(yellow_be_gone("GOLD"), "ForestGreen")
    test.it("A yellow color name in mixed case")   
    test.assert_equals(yellow_be_gone("pAlEgOlDeNrOd"), "LightGreen")
    test.it("A non-yellow color name")   
    test.assert_equals(yellow_be_gone("BlueViolet"), "BlueViolet")

    test.describe("Some hex color codes tests")
    test.it("R, G, and B are all equal")   
    test.assert_equals(yellow_be_gone("#000000"), "#000000")
    test.it("R and G are both greater than B, and the alpha hex characters are in lower case")   
    test.assert_equals(yellow_be_gone("#b8860b"), "#0bb886")
    test.it("G is greater than R and B, which are equal")   
    test.assert_equals(yellow_be_gone("#8FBC8F"), "#8FBC8F")
    test.it("R is greater than B, and B is greater than G")   
    test.assert_equals(yellow_be_gone("#C71585"), "#C71585")