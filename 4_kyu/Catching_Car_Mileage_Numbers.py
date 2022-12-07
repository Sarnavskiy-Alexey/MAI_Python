"""
    Reference: https://www.codewars.com//kata/52c4dd683bfd3b434c000292
"""


def check_palindrome(str_number):
    for i in range(len(str_number) // 2):
        if str_number[i] != str_number[len(str_number) - 1 - i]:
            return False
    return True


def check_all_equal(str_number):
    for idx, val in enumerate(str_number):
        if val != str_number[idx - 1]:
            return False
    return True


def check_incr_seq(str_number):
    for i in range(1, len(str_number)):
        if not((ord(str_number[i]) - ord(str_number[i - 1]) == 1 and str_number[i - 1] != '0') or (str_number[i - 1] == '9' and str_number[i] == '0')):
            return False
    return True


def check_decr_seq(str_number):
    for i in range(1, len(str_number)):
        if not((ord(str_number[i - 1]) - ord(str_number[i]) == 1 and str_number[i - 1] != '0') or (str_number[i - 1] == '1' and str_number[i] == '0')):
            return False
    return True


def real_check(number, awesome_phrases):
    str_number = str(number)
    if str_number[0] != '0' and int(str_number[1:]) == 0:
        return True
    elif check_all_equal(str_number) or check_incr_seq(str_number) or check_decr_seq(str_number) or check_palindrome(str_number) or number in awesome_phrases:
        return True
    else:
        return False


def is_interesting(number, awesome_phrases):
    if number > 99:
        if real_check(number, awesome_phrases):
            return 2
        for x in range(number - 2, number + 3):
            if x != number and real_check(x, awesome_phrases):
                return 1
        return 0
    else:
        return 1 if number in [98, 99] else 0
