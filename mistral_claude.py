# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 20:34:29 2025

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 19:19:28 2025

@author: HP
"""

import unittest
from credit_card import validate_credit_card

class TestCreditCardValidator(unittest.TestCase):
    
    def test_valid_cards(self):
        # Test various valid credit card numbers from different providers
        self.assertTrue(validate_credit_card("4532015112830366"))  # Visa
        self.assertTrue(validate_credit_card("5425233430109903"))  # Mastercard
        self.assertTrue(validate_credit_card("2223000048410010"))  # Mastercard (2-series)
        self.assertTrue(validate_credit_card("378282246310005"))   # American Express
        self.assertTrue(validate_credit_card("6011111111111117"))  # Discover
        self.assertTrue(validate_credit_card("3530111333300000"))  # JCB
        self.assertTrue(validate_credit_card("6062821086773091"))  # 16-digit valid card
        self.assertTrue(validate_credit_card("3566002020360505"))  # Another JCB
    
    def test_valid_cards_with_separators(self):
        # Test valid cards with spaces and dashes
        self.assertTrue(validate_credit_card("4532 0151 1283 0366"))
        self.assertTrue(validate_credit_card("5425-2334-3010-9903"))
        self.assertTrue(validate_credit_card("3782 82246 31000 5"))
        self.assertTrue(validate_credit_card("6011-1111-1111-1117"))
        self.assertTrue(validate_credit_card("4532-0151-1283 0366"))
        self.assertTrue(validate_credit_card("5425 2334-3010-9903"))
    
    def test_boundary_length_cards(self):
        # Test boundary cases (13 and 19 digits)
        self.assertTrue(validate_credit_card("4222222222223"))     # 13 digits Visa
        self.assertTrue(validate_credit_card("6011601160116611303"))  # 19 digits Discover
    
    def test_invalid_cards_checksum(self):
        # Test cards with invalid checksums
        self.assertFalse(validate_credit_card("4532015112830367"))
        self.assertFalse(validate_credit_card("5425233430109904"))
        self.assertFalse(validate_credit_card("378282246310006"))
        self.assertFalse(validate_credit_card("4222222222224"))
    
    def test_invalid_length(self):
        # Test cards with invalid lengths
        self.assertFalse(validate_credit_card("42"))
        self.assertFalse(validate_credit_card("123456789012"))
        self.assertFalse(validate_credit_card("12345678901234567890"))
        self.assertFalse(validate_credit_card("60116011601166113031"))
    
    def test_non_numeric_input(self):
        # Test with non-numeric input
        self.assertFalse(validate_credit_card("4532015112830366a"))
        self.assertFalse(validate_credit_card("453201511283036!"))
        self.assertFalse(validate_credit_card("4532O15112830366"))
        self.assertFalse(validate_credit_card("5425233430109ABC"))
        self.assertFalse(validate_credit_card("4532@0151#1283$0366"))
    
    def test_special_inputs(self):
        # Test with empty and special inputs
        self.assertFalse(validate_credit_card(""))
        self.assertFalse(validate_credit_card(" "))
        self.assertFalse(validate_credit_card("     "))
        self.assertFalse(validate_credit_card("-"))
        self.assertFalse(validate_credit_card("-----"))
        self.assertFalse(validate_credit_card("4532--01511283--0366"))
        self.assertFalse(validate_credit_card("4532 0151  1283 0366"))
    
    def test_formatting_edge_cases(self):
        # Test various formatting edge cases
        self.assertTrue(validate_credit_card("4532-0151 1283-0366"))
        self.assertTrue(validate_credit_card(" 4532015112830366 "))
        self.assertTrue(validate_credit_card("\t5425233430109903\n"))
    
    def test_leading_zeros(self):
        # Test cards with leading zeros
        self.assertTrue(validate_credit_card("00004532015112830366"))
        self.assertFalse(validate_credit_card("0000000000000000"))  # All zeros

if __name__ == "__main__":
    unittest.main()
