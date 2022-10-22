"""
Reference: https://www.codewars.com//kata/58545549b45c01ccab00058c
"""


def calculate_total(subtotal, tax, tip):
    return round(subtotal * (1 + (tax + tip) / 100), 2)


print(calculate_total(5.00, 5, 10), '==', 5.75)
print(calculate_total(36.97, 7, 15), '==', 45.10)
print(calculate_total(0.00, 6, 18), '==', 0.00)
print(calculate_total(80.94, 0, 20), '==', 97.13)
print(calculate_total(54.96, 8, 0), '==', 59.36)
