"""
Reference: https://www.codewars.com//kata/586430a5b3a675296a000395
"""

sizes = {
    "economy": 0,
    "medium": 10
}


def insurance(age, size, num_of_days):
    cost = 0
    if num_of_days >= 0:
        cost += (sizes.get(size) if size in sizes else 15) * num_of_days
        cost += 10 * num_of_days if age < 25 else 0
        cost += 50 * num_of_days
    return cost


print(insurance(18, "medium", 7), '==', 490)
print(insurance(30, "full-size", 30), '==', 1950)
print(insurance(21, "economy", -10), '==', 0)
print(insurance(42, "my custom car", 7), '==', 455)
