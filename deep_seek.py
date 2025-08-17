# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 10:32:46 2025

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 21:43:25 2025

@author: HP
"""

import unittest
from credit_card import validate_credit_card

class TestCreditCardValidator(unittest.TestCase):
    
    def test_valid_credit_cards(self):
        """Test various valid credit card numbers."""
        self.assertTrue(validate_credit_card("4532015112830366"))  # Visa
        self.assertTrue(validate_credit_card("5425233430109903"))  # Mastercard
        self.assertTrue(validate_credit_card("2223000048410010"))  # Mastercard (2-series)
        self.assertTrue(validate_credit_card("378282246310005"))   # American Express
        self.assertTrue(validate_credit_card("6011111111111117"))  # Discover
        self.assertTrue(validate_credit_card("3530111333300000"))  # JCB
        self.assertTrue(validate_credit_card("6062821086773091"))  # Another 16-digit valid card
        self.assertTrue(validate_credit_card("4222222222223"))     # 13-digit Visa
        self.assertTrue(validate_credit_card("6011601160116611303"))  # 19-digit Discover

    def test_valid_credit_cards_with_spaces(self):
        """Test valid credit card numbers with spaces."""
        self.assertTrue(validate_credit_card("4532 0151 1283 0366"))
        self.assertTrue(validate_credit_card("5425 2334 3010 9903"))
        self.assertTrue(validate_credit_card("2223 0000 4841 0010"))
        self.assertTrue(validate_credit_card("3782 822463 10005"))
        self.assertTrue(validate_credit_card("6011 1111 1111 1117"))

    def test_valid_credit_cards_with_dashes(self):
        """Test valid credit card numbers with dashes."""
        self.assertTrue(validate_credit_card("4532-0151-1283-0366"))
        self.assertTrue(validate_credit_card("5425-2334-3010-9903"))
        self.assertTrue(validate_credit_card("2223-0000-4841-0010"))
        self.assertTrue(validate_credit_card("3782-822463-10005"))
        self.assertTrue(validate_credit_card("6011-1111-1111-1117"))

    def test_invalid_credit_cards(self):
        """Test credit card numbers with invalid checksums."""
        self.assertFalse(validate_credit_card("4532015112830367"))  # Last digit changed
        self.assertFalse(validate_credit_card("5425233430109904"))  # Last digit changed
        self.assertFalse(validate_credit_card("2223000048410011"))  # Last digit changed
        self.assertFalse(validate_credit_card("378282246310006"))   # Last digit changed
        self.assertFalse(validate_credit_card("6011111111111118"))  # Last digit changed

    def test_invalid_length(self):
        """Test credit card numbers with invalid lengths."""
        self.assertFalse(validate_credit_card("42"))                 # Too short
        self.assertFalse(validate_credit_card("12345678901234567890")) # Too long
        self.assertFalse(validate_credit_card("123456789012"))        # 12 digits
        self.assertFalse(validate_credit_card("1234567890123456789")) # 19 digits but invalid

    def test_non_numeric_input(self):
        """Test credit card numbers with non-numeric characters."""
        self.assertFalse(validate_credit_card("4532015112830366a"))  # Contains a letter
        self.assertFalse(validate_credit_card("453201511283036!"))   # Contains a special character
        self.assertFalse(validate_credit_card("4532-0151-1283-036a"))  # Contains a letter
        self.assertFalse(validate_credit_card("4532 0151 1283 036!"))   # Contains a special character

    def test_empty_input(self):
        """Test with empty input."""
        self.assertFalse(validate_credit_card(""))

    def test_edge_cases(self):
        """Test edge cases for minimum and maximum valid lengths."""
        self.assertTrue(validate_credit_card("4222222222223"))     # 13 digits Visa
        self.assertTrue(validate_credit_card("6011601160116611303"))  # 19 digits Discover
        self.assertFalse(validate_credit_card("422222222222"))      # 12 digits (invalid)
        self.assertFalse(validate_credit_card("60116011601166113030"))  # 20 digits (invalid)

if __name__ == "__main__":
    unittest.main()