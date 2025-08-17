# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 10:32:46 2025

@author: HP
"""

import unittest
import time
from copy import deepcopy
from credit_card import validate_credit_card

# Valid credit card test cases
valid_cards = [
    "4532015112830366",  # Visa
    "5425233430109903",  # Mastercard
    "2223000048410010",  # Mastercard (2-series)
    "378282246310005",   # American Express
    "6011111111111117",  # Discover
    "3530111333300000",  # JCB
    "6062821086773091",  # 16-digit valid card
    "4222222222223",     # 13-digit Visa (minimum length)
    "6011601160116611303"  # 19-digit Discover (maximum length)
]

# Invalid credit card test cases
invalid_cards = [
    "4532015112830367",  # Changed last digit (invalid checksum)
    "5425233430109904",  # Changed last digit (invalid checksum)
    "2223000048410011",  # Changed last digit (invalid checksum)
    "378282246310006",   # Changed last digit (invalid checksum)
    "6011111111111118",  # Changed last digit (invalid checksum)
    "42",                # Too short
    "12345678901234567890", # Too long
    "123456789012",       # 12 digits (invalid)
    "1234567890123456789", # 19 digits but invalid
    "4532015112830366a",  # Contains a letter
    "453201511283036!",   # Contains a special character
    "",                   # Empty input
    "422222222222",       # 12 digits (invalid)
    "60116011601166113030"  # 20 digits (invalid)
]

# Track execution time
start_time = time.time()

# Run tests and track passed/failed cases
passed_tests = 0
failed_tests = 0
assertions_run = 0

for card in valid_cards:
    assertions_run += 1
    if validate_credit_card(card):
        passed_tests += 1
    else:
        failed_tests += 1

for card in invalid_cards:
    assertions_run += 1
    if not validate_credit_card(card):
        passed_tests += 1
    else:
        failed_tests += 1

# Compute execution time
test_execution_time = time.time() - start_time

# Mutations for mutation testing
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
        if validate_credit_card(mutated_card) == True:
            pass
        else:
            killed_mutants += 1

mutation_score = (killed_mutants / total_mutants) * 100 if total_mutants > 0 else 0

# Compute Code Coverage (Dummy Values for Example Purpose)
code_coverage = 85.0  # Replace with actual tool-based measurement
branch_coverage = 80.0  # Replace with actual measurement
statement_coverage = 90.0  # Replace with actual measurement
function_coverage = 95.0  # Replace with actual measurement

# Prepare the report
test_report = {
    "Total Test Cases": len(valid_cards) + len(invalid_cards),
    "Passed Test Cases": passed_tests,
    "Failed Test Cases": failed_tests,
    "Test Execution Time (s)": test_execution_time,
    "Assertions Run": assertions_run,
    "Code Coverage (%)": code_coverage,
    "Branch Coverage (%)": branch_coverage,
    "Statement Coverage (%)": statement_coverage,
    "Function Coverage (%)": function_coverage,
    "Mutation Score (%)": mutation_score,
}

print(test_report)
