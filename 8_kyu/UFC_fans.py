"""
Reference: https://www.codewars.com//kata/582dafb611d576b745000b74
"""


def quote(fighter):
    if fighter.lower() == 'george saint pierre':
        return "I am not impressed by your performance."
    elif fighter.lower() == 'conor mcgregor':
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    else:
        return ""


if __name__ == '__main__':
    print(quote('george saint pierre'))
    print(quote('conor mcgregor'))
    print(quote('George Saint Pierre'))
    print(quote('Conor McGregor'))
