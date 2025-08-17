# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 23:22:35 2025

@author: HP
"""

# Simulated output from ChatGPT-4 + DeepSeek analysis

import unittest
from credit_card import validate_credit_card

class TestCreditCardValidator(unittest.TestCase):
    # Original test cases remain...
    
    def test_specific_card_types(self):
        """Test specific card types with their characteristic prefixes"""
        # Visa (starts with 4, 13-16 digits)
        self.assertTrue(validate_credit_card("4111111111111111"))  # 16 digits
        
        # Mastercard (starts with 51-55 or 2221-2720, 16 digits)
        self.assertTrue(validate_credit_card("5555555555554444"))
        self.assertTrue(validate_credit_card("2221000000000009"))
        
        # Amex (starts with 34 or 37, 15 digits)
        self.assertTrue(validate_credit_card("371449635398431"))
        
        # Discover (starts with 6011, 65, 644-649, 16-19 digits)
        self.assertTrue(validate_credit_card("6011000000000004"))
        
    def test_boundary_cases_for_length(self):
        """Test specifically at the boundaries of valid card lengths"""
        # 12 digits (just below minimum)
        self.assertFalse(validate_credit_card("411111111111"))
        
        # 13 digits (minimum valid)
        self.assertTrue(validate_credit_card("4222222222223"))
        
        # 19 digits (maximum valid)
        self.assertTrue(validate_credit_card("6011601160116611303"))
        
        # 20 digits (just above maximum)
        self.assertFalse(validate_credit_card("60116011601166113031"))
        
    def test_luhn_specific_cases(self):
        """Test edge cases specific to the Luhn algorithm"""
        # Test cases that specifically exercise the "subtract 9" branch
        # This card number has digits that, when doubled, exceed 9
        self.assertTrue(validate_credit_card("4916994977638754"))
        
        # This number would validate if we forget to subtract 9
        self.assertFalse(validate_credit_card("4916994977638755"))
        
    def test_formatting_edge_cases(self):
        """Test various formatting patterns"""
        # Mixed spaces and dashes
        self.assertTrue(validate_credit_card("4532-0151 1283-0366"))
        
        # Uneven spacing
        self.assertTrue(validate_credit_card("4532 01511 2830366"))
        
        # Leading/trailing spaces
        self.assertTrue(validate_credit_card(" 4532015112830366 "))