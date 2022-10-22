"""
Reference: https://www.codewars.com//kata/56d49587df52101de70011e4
"""


def leo(oscar):
    if oscar == 88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of wallstreet?!"
    elif oscar > 88:
        return "Leo got one already!"
    else:
        return "When will you give Leo an Oscar?"


if __name__ == '__main__':
    print(leo(85))
    print(leo(86))
    print(leo(87))
    print(leo(88))
    print(leo(89))
    print(leo(90))
