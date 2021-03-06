from src import romanRefactoring
import unittest

class KnownValues(unittest.TestCase):
    known_values = ( (1, 'I'),
                     (2, 'II'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V'),
                     (6, 'VI'),
                     (7, 'VII'),
                     (8, 'VIII'),
                     (9, 'IX'),
                     (10, 'X'),
                     (50, 'L'),
                     (100, 'C'),
                     (500, 'D'),
                     (1000, 'M'),
                     (31, 'XXXI'),
                     (148, 'CXLVIII'),
                     (294, 'CCXCIV'),
                     (312, 'CCCXII'),
                     (421, 'CDXXI'),
                     (528, 'DXXVIII'),
                     (621, 'DCXXI'),
                     (782, 'DCCLXXXII'),
                     (870, 'DCCCLXX'),
                     (941, 'CMXLI'),
                     (1043, 'MXLIII'),
                     (1110, 'MCX'),
                     (1226, 'MCCXXVI'),
                     (1301, 'MCCCI'),
                     (1485, 'MCDLXXXV'),
                     (1509, 'MDIX'),
                     (1607, 'MDCVII'),
                     (1754, 'MDCCLIV'),
                     (1832, 'MDCCCXXXII'),
                     (1993, 'MCMXCIII'),
                     (2074, 'MMLXXIV'),
                     (2152, 'MMCLII'),
                     (2212, 'MMCCXII'),
                     (2343, 'MMCCCXLIII'),
                     (2499, 'MMCDXCIX'),
                     (2574, 'MMDLXXIV'),
                     (2646, 'MMDCXLVI'),
                     (2723, 'MMDCCXXIII'),
                     (2892, 'MMDCCCXCII'),
                     (2975, 'MMCMLXXV'),
                     (3051, 'MMMLI'),
                     (3185, 'MMMCLXXXV'),
                     (3250, 'MMMCCL'),
                     (3313, 'MMMCCCXIII'),
                     (3408, 'MMMCDVIII'),
                     (3501, 'MMMDI'),
                     (3610, 'MMMDCX'),
                     (3743, 'MMMDCCXLIII'),
                     (3844, 'MMMDCCCXLIV'),
                     (3888, 'MMMDCCCLXXXVIII'),
                     (3940, 'MMMCMXL'),
                     (3999, 'MMMCMXCIX'),
                     (4000, 'MMMM'),
                     (4500, 'MMMMD'),
                     (4888, 'MMMMDCCCLXXXVIII'),
                     (4999, 'MMMMCMXCIX'))

    def test_to_roman_known_values(self):
        '''to_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = romanRefactoring.to_roman(integer)
            self.assertEqual(numeral, result)

    def test_to_roman_out_of_range(self):
        '''to_roman should give known result with known input'''
        self.assertRaises(romanRefactoring.OutOfRangeError, romanRefactoring.to_roman, 5000)
        self.assertRaises(romanRefactoring.OutOfRangeError, romanRefactoring.to_roman, -1)
        self.assertRaises(romanRefactoring.OutOfRangeError, romanRefactoring.to_roman, 0)

    def test_to_roman_non_integers(self):
        '''to_roman should give known result with known input'''
        self.assertRaises(romanRefactoring.NonIntegerError, romanRefactoring.to_roman, 0.5)
        self.assertRaises(romanRefactoring.NonIntegerError, romanRefactoring.to_roman, 1.0)


    def test_roman_to_numeral(self):
        for integer, numeral in self.known_values:
            result = romanRefactoring.roman_to_numeral(numeral)
            self.assertEqual(integer, result)
            
    def test_roman_to_numeral_invalid_values(self):
        self.assertRaises(romanRefactoring.NonValidRomanValueError, romanRefactoring.roman_to_numeral, 'MMMMM')
        self.assertRaises(romanRefactoring.NonValidRomanValueError, romanRefactoring.roman_to_numeral, '')

    def test_roundtrip(self):
        for i in range(1,5000):
            romanValue = romanRefactoring.to_roman(i)
            self.assertEqual(i, romanRefactoring.roman_to_numeral(romanValue), 'Roundtrip failure for {0}'.format(i))

if __name__ == '__main__':
    unittest.main()