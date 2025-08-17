
def validate_credit_card(card_number):
    card_number = card_number.replace(" ", "").replace("-", "")
    if not card_number.isdigit():
        return False
    if not (13 <= len(card_number) <= 19):
        return False
    sum_digits = 0
    card_num_reversed = card_number[::-1]
    for i, digit in enumerate(card_num_reversed):
        digit_value = int(digit)
        if i % 2 == 1:
            digit_value *= 2
            if digit_value > 9:
                digit_value -= 9
        sum_digits += digit_value
    return sum_digits % 10 == 0
"""
  Validates a credit card number using the Luhn algorithm.
  Args:
      card_number (str): The credit card number as a string, can contain spaces
  Returns:
      bool: True if the card number is valid, False otherwise
  """
