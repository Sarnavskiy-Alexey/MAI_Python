"""
Reference: https://www.codewars.com//kata/56b8903933dbe5831e000c76
"""


def spoonerize(words):
    l = words.split(' ')
    letter_1 = l[0][0]
    letter_2 = l[-1][0]
    l[0] = l[0].replace(letter_1, letter_2, 1)
    l[-1] = l[-1].replace(letter_2, letter_1, 1)
    return " ".join(l)


print(spoonerize("nit picking"), '==', "pit nicking")
print(spoonerize("wedding bells"), '==', "bedding wells")
print(spoonerize("jelly beans"), '==', "belly jeans")
print(spoonerize("pop corn"), '==', "cop porn")
