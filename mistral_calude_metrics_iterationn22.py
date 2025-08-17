# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 21:28:28 2025

@author: HP
"""

import unittest
from copy import deepcopy
from credit_card import validate_credit_card

# Test cases
valid_cards = [
    "4532015112830366",  # Visa
    "5425233430109903",  # Mastercard
    "2223000048410010",  # Mastercard (2-series)
    "378282246310005",   # American Express
    "6011111111111117",  # Discover
    "3530111333300000",  # JCB
    "6062821086773091",  # Another 16-digit valid card
    "4222222222223",     # 13-digit Visa (boundary case)
    "6011601160116611303"  # 19-digit Discover (boundary case)
]

invalid_cards = [
    "4532015112830367",  # Invalid checksum
    "5425233430109904",  # Invalid checksum
    "42",                # Too short
    "12345678901234567890", # Too long
    "4532015112830366a",  # Non-numeric character
    "",                   # Empty input
    "-----",              # Only dashes
    "0000000000000000",   # All zeros
    "4916994977638754",   # Random invalid number
]

formatted_valid_cards = [
    "4532 0151 1283 0366",  # With spaces
    "5425-2334-3010-9903",  # With dashes
    "4532-0151 1283-0366",  # Mixed separators
    " 4532015112830366 ",   # Leading/trailing spaces
]

# Mutation testing mutations
mutations = [
    lambda x: x[:-1] + ("1" if x[-1] != "1" else "0"),  # Change last digit
    lambda x: x[:1] + ("0" if x[1] != "0" else "1") + x[2:],  # Change second digit
    lambda x: x.replace("4", "5", 1),  # Replace first 4 with 5
]

# Perform mutation testing
killed_mutants = 0
total_mutants = len(valid_cards) * len(mutations)

for card in valid_cards:
    for mutate in mutations:
        mutated_card = mutate(card)
        if validate_credit_card(mutated_card) == False:
            killed_mutants += 1

mutation_score = (killed_mutants / total_mutants) * 100 if total_mutants > 0 else 0

# Compute Fault Detection Rate
detected_faults = sum(not validate_credit_card(card) for card in invalid_cards)
fault_detection_rate = (detected_faults / len(invalid_cards)) * 100

# Compute Test Effectiveness
test_effectiveness = (mutation_score + fault_detection_rate) / 2

# Compute Redundancy Score
unique_test_cases = set(valid_cards + invalid_cards + formatted_valid_cards)
test_redundancy_score = (1 - (len(unique_test_cases) / (len(valid_cards) + len(invalid_cards) + len(formatted_valid_cards)))) * 100

# Compute Boundary Value Coverage
boundary_cases = ["4222222222223", "6011601160116611303", "42", "12345678901234567890"]
boundary_coverage = (sum(validate_credit_card(card) for card in boundary_cases if card in valid_cards) +
                     sum(not validate_credit_card(card) for card in boundary_cases if card in invalid_cards)) / len(boundary_cases) * 100

# Compute Combined Test Strength Score
combined_test_strength_score = (mutation_score + fault_detection_rate + test_effectiveness + (100 - test_redundancy_score) + boundary_coverage) / 5

# Prepare the report
test_report = {
    "Mutation Score": mutation_score,
    "Fault Detection Rate": fault_detection_rate,
    "Test Effectiveness": test_effectiveness,
    "Test Redundancy Score": test_redundancy_score,
    "Boundary Value Coverage": boundary_coverage,
    "Combined Test Strength Score": combined_test_strength_score,
}

print(test_report)
