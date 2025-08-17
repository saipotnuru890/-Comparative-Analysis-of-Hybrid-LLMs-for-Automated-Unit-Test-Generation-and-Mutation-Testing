# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 23:22:35 2025

@author: HP
"""

# Simulated output from ChatGPT-4 + DeepSeek analysis

import unittest
from credit_card import validate_credit_card

class TestCreditCardValidator(unittest.TestCase):
    
    def test_valid_cards(self):
        # Test various valid credit card numbers
        self.assertTrue(validate_credit_card("4532015112830366"))  # Visa
        self.assertTrue(validate_credit_card("5425233430109903"))  # Mastercard
        self.assertTrue(validate_credit_card("2223000048410010"))  # Mastercard (2-series)
        self.assertTrue(validate_credit_card("378282246310005"))   # American Express
        self.assertTrue(validate_credit_card("6011111111111117"))  # Discover
        
    def test_valid_cards_with_spaces(self):
        # Test valid cards with spaces
        self.assertTrue(validate_credit_card("4532 0151 1283 0366"))
        self.assertTrue(validate_credit_card("5425 2334 3010 9903"))
        
    def test_valid_cards_with_dashes(self):
        # Test valid cards with dashes
        self.assertTrue(validate_credit_card("4532-0151-1283-0366"))
        
    def test_invalid_cards(self):
        # Test cards with invalid checksums
        self.assertFalse(validate_credit_card("4532015112830367"))  # Last digit changed
        self.assertFalse(validate_credit_card("5425233430109904"))  # Last digit changed
        
    def test_invalid_length(self):
        # Test cards with invalid lengths
        self.assertFalse(validate_credit_card("42"))                 # Too short
        self.assertFalse(validate_credit_card("12345678901234567890")) # Too long
        
    def test_non_numeric_input(self):
        # Test with non-numeric input
        self.assertFalse(validate_credit_card("4532015112830366a"))  # Contains a letter
        self.assertFalse(validate_credit_card("453201511283036!"))   # Contains a special character
        
    def test_empty_input(self):
        # Test with empty input
        self.assertFalse(validate_credit_card(""))
        
    def test_edge_cases(self):
        # Edge cases for minimum and maximum valid lengths
        self.assertTrue(validate_credit_card("3530111333300000"))  # 16 digits JCB
        self.assertTrue(validate_credit_card("6062821086773091"))  # Another 16 digit valid card
        
        # Test boundary cases (13 and 19 digits)
        self.assertTrue(validate_credit_card("4222222222223"))     # 13 digits Visa
        self.assertTrue(validate_credit_card("6011601160116611303"))  # 19 digits Discover
    
    # Original test cases remain...
    def test_property_based_cases(self):
        """Test properties that should hold for any valid implementation"""
        # Property: Adding a valid digit at the end should make a valid card invalid
        valid_card = "4532015112830366"
        self.assertTrue(validate_credit_card(valid_card))
        
        for digit in "0123456789":
            if digit != "6":  # The last digit that would make it valid
                self.assertFalse(validate_credit_card(valid_card + digit))
        
        # Property: A card with all zeros should be valid (mod 10 = 0)
        self.assertTrue(validate_credit_card("0000000000000000"))
        
    
    
    
    def test_failure_modes(self):
        
        """Test various ways the validation could fail"""
        # Test each failure mode specifically
        
        # 1. Non-digit characters
        self.assertFalse(validate_credit_card("411111111111111a"))
        self.assertFalse(validate_credit_card("4111-1111-1111-111a"))
        
        # 2. Length check failures
        self.assertFalse(validate_credit_card("41111"))
        self.assertFalse(validate_credit_card("41111111111111111111"))
        
        # 3. Luhn algorithm failures
        # Change one digit to make the checksum fail
        valid_card = "4532015112830366"
        
        for i in range(len(valid_card)):
            for d in "0123456789":
                if d != valid_card[i]:
                    modified_card = valid_card[:i] + d + valid_card[i+1:]
                    # Some modifications might still pass the Luhn check by coincidence
                    # But most should fail
                    if int(d) != (int(valid_card[i]) + 5) % 10:
                        self.assertFalse(validate_credit_card(modified_card))
                        
        def test_unicode_digits(self):
            """Test with Unicode digits which should be rejected"""
            # Unicode digits like ０１２３４５６７８９ should be rejected
            self.assertFalse(validate_credit_card("４５３２０１５１１２８３０３６６"))
    



    
   