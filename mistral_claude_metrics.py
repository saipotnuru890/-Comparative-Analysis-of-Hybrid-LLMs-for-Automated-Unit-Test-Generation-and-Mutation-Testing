# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 21:47:47 2025

@author: HP
"""

import unittest
from copy import deepcopy
from credit_card import validate_credit_card

# Combined valid test cases
valid_cards = [
    "4532015112830366", "5425233430109903", "2223000048410010", "378282246310005",
    "6011111111111117", "3530111333300000", "6062821086773091", "3566002020360505",
     "6011601160116611303"
]

# Combined invalid test cases
invalid_cards = [
    "4532015112830367", "5425233430109904", "378282246310006", "4222222222224",
    "42", "123456789012", "12345678901234567890", "60116011601166113031",
    "4532015112830366a", "453201511283036!", "4532O15112830366", "5425233430109ABC",
    "", " ", "-", "    ", "4532--01511283--0366", "4532 0151  1283 0366"
]

# Formatted valid cards with spaces/dashes
formatted_valid_cards = [
    "4532 0151 1283 0366", "5425-2334-3010-9903", "3782 82246 31000 5", "6011-1111-1111-1117",
    "4532-0151-1283 0366", "5425 2334-3010-9903", " 4532015112830366 ", "\t5425233430109903\n"
]

# Mutation testing
mutations = [
    lambda x: x[:-1] + ("1" if x[-1] != "1" else "0"),
    lambda x: x[:1] + ("0" if x[1] != "0" else "1") + x[2:],
    lambda x: x.replace("4", "5", 1)
]

killed_mutants = 0
total_mutants = len(valid_cards) * len(mutations)

for card in valid_cards:
    for mutate in mutations:
        mutated_card = mutate(card)
        if validate_credit_card(mutated_card) == True:
            pass
        else:
            killed_mutants += 1

mutation_score = (killed_mutants / total_mutants) * 100 if total_mutants > 0 else 0

detected_faults = sum(not validate_credit_card(card) for card in invalid_cards)
fault_detection_rate = (detected_faults / len(invalid_cards)) * 100

test_effectiveness = (mutation_score + fault_detection_rate) / 2

unique_test_cases = set(valid_cards + invalid_cards + formatted_valid_cards)
test_redundancy_score = (1 - (len(unique_test_cases) / (len(valid_cards) + len(invalid_cards) + len(formatted_valid_cards)))) * 100

boundary_cases = ["4222222222223", "6011601160116611303", "42", "123456789012345678901"]
boundary_coverage = (sum(validate_credit_card(card) for card in boundary_cases if card in valid_cards) +
                     sum(not validate_credit_card(card) for card in boundary_cases if card in invalid_cards)) / len(boundary_cases) * 100

combined_test_strength_score = (mutation_score + fault_detection_rate + test_effectiveness + (100 - test_redundancy_score) + boundary_coverage) / 5

test_report = {
    "Mutation Score": mutation_score,
    "Fault Detection Rate": fault_detection_rate,
    "Test Effectiveness": test_effectiveness,
    "Test Redundancy Score": test_redundancy_score,
    "Boundary Value Coverage": boundary_coverage,
    "Combined Test Strength Score": combined_test_strength_score,
}

print(test_report)
