"""
    Reference: https://www.codewars.com//kata/546d15cebed2e10334000ed9
"""


def beat_on_list(s):
    res = []
    word = ''
    for i in range(len(s)):
        if s[i] not in ('+', '-', '*', '='):
            word += s[i]
        else:
            res += [word]
            word = ''
            res += [s[i]]
    res += [word]
    while '' in res:
        empty_idx = res.index('')
        res.pop(empty_idx)
        res.pop(empty_idx)
        res[empty_idx] = '-' + res[empty_idx]
    return res


def get_result_from_list(lst):
    for oper in ('*', '-', '+'):
        while oper in lst:
            oper_idx = lst.index(oper)
            if oper == '*': lst[oper_idx - 1] = lst[oper_idx - 1] * lst[oper_idx + 1]
            if oper == '-': lst[oper_idx - 1] = lst[oper_idx - 1] - lst[oper_idx + 1]
            if oper == '+': lst[oper_idx - 1] = lst[oper_idx - 1] + lst[oper_idx + 1]
            lst.pop(oper_idx)
            lst.pop(oper_idx)
    return lst


def solve_runes(runes):
    print(runes)
    lst = beat_on_list(runes)
    found_digits = set()
    not_found_digits = []
    for el in lst:
        for digit in el:
            if digit.isdigit():
                found_digits.add(digit)

    for c in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        if c not in found_digits:
            not_found_digits += c

    for el in lst:
        first_q = el.find('?')
        if not_found_digits[0] == '0' and (first_q == 0 or len(el) > 1 and (el[0] == '-' and first_q == 1)) and len(
                el) > 1:
            not_found_digits.pop(0)
            break

    for c in not_found_digits:
        work_copy_of_list = lst.copy()
        for i in range(len(work_copy_of_list)):
            work_copy_of_list[i] = work_copy_of_list[i].replace('?', c)
            if work_copy_of_list[i] not in ('*', '-', '+', '='):
                work_copy_of_list[i] = int(work_copy_of_list[i])
        if get_result_from_list(work_copy_of_list)[0] == work_copy_of_list[-1]:
            return int(c)

    return -1
