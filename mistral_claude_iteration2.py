# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 21:26:33 2025

@author: HP
"""

import unittest
from credit_card import validate_credit_card

class TestCreditCardValidator(unittest.TestCase):
    
    def test_valid_cards(self):
        self.assertTrue(validate_credit_card("4532015112830366"))  # Visa
        self.assertTrue(validate_credit_card("5425233430109903"))  # Mastercard
        self.assertTrue(validate_credit_card("2223000048410010"))  # Mastercard (2-series)
        self.assertTrue(validate_credit_card("378282246310005"))   # American Express
        self.assertTrue(validate_credit_card("6011111111111117"))  # Discover
        self.assertTrue(validate_credit_card("3530111333300000"))  # JCB
        self.assertTrue(validate_credit_card("6062821086773091"))  # 16-digit valid card
        self.assertTrue(validate_credit_card("3566002020360505"))  # Another JCB

    def test_valid_cards_with_separators(self):
        self.assertTrue(validate_credit_card("4532 0151 1283 0366"))
        self.assertTrue(validate_credit_card("5425-2334-3010-9903"))
        self.assertTrue(validate_credit_card("3782 82246 31000 5"))
        self.assertTrue(validate_credit_card("6011-1111-1111-1117"))
    
    def test_boundary_length_cards(self):
        self.assertTrue(validate_credit_card("4222222222223"))     # 13 digits Visa (minimum valid length)
        self.assertTrue(validate_credit_card("6011601160116611303"))  # 19 digits Discover (maximum valid length)
        self.assertFalse(validate_credit_card("42"))  # Too short (2 digits)
        self.assertFalse(validate_credit_card("123456789012"))  # Too short (12 digits)
        self.assertFalse(validate_credit_card("123456789012345678901"))  # Too long (21 digits)
        self.assertFalse(validate_credit_card("60116011601166113031"))  # Too long (20 digits)

    def test_invalid_cards_checksum(self):
        self.assertFalse(validate_credit_card("4532015112830367"))
        self.assertFalse(validate_credit_card("5425233430109904"))
        self.assertFalse(validate_credit_card("378282246310006"))
        self.assertFalse(validate_credit_card("4222222222224"))

    def test_invalid_length(self):
        self.assertFalse(validate_credit_card(""))  # Empty string
        self.assertFalse(validate_credit_card(" "))  # Just space
        self.assertFalse(validate_credit_card("-"))  # Just dash
        self.assertFalse(validate_credit_card("    "))  # Multiple spaces
    
    def test_non_numeric_input(self):
        self.assertFalse(validate_credit_card("4532015112830366a"))
        self.assertFalse(validate_credit_card("453201511283036!"))
        self.assertFalse(validate_credit_card("4532O15112830366"))
        self.assertFalse(validate_credit_card("5425233430109ABC"))
    
    def test_formatting_edge_cases(self):
        self.assertTrue(validate_credit_card("4532-0151 1283-0366"))  # Mixed separators
        self.assertFalse(validate_credit_card("4532--01511283--0366"))
        self.assertFalse(validate_credit_card("4532 0151  1283 0366"))
    
    def test_leading_trailing_spaces(self):
        self.assertTrue(validate_credit_card(" 4532015112830366 "))
        self.assertTrue(validate_credit_card("\t5425233430109903\n"))
    
if __name__ == "__main__":
    unittest.main()
