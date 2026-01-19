import random

three_digit_code_number1 = random.randint(0, 9)
three_digit_code_number2 = random.randint(0, 9)
three_digit_code_number3 = random.randint(0, 9)

three_digits_code = f"{three_digit_code_number1}{three_digit_code_number2}{three_digit_code_number3}"
four_digits_code = random.randint(1111, 6666)

print("Generated three-digit code:", three_digits_code)
print("Generated Four-digit code:", four_digits_code)