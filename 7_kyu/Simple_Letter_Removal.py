"""
Reference: https://www.codewars.com//kata/5b728f801db5cec7320000c7
"""


def solve(st, k):
    letter = 'a'
    counter = st.count(letter)
    for n_del in range(k if k < len(st) else len(st)):
        while len(st) > 0 and counter == 0:
            letter = chr(ord(letter) + 1)
            counter += st.count(letter)
        st = st.replace(letter, '', 1)
        counter -= 1
    return st


print(solve('abracadabra', 1), '==', 'bracadabra')
print(solve('abracadabra', 2), '==', 'brcadabra')
print(solve('abracadabra', 6), '==', 'rcdbr')
print(solve('abracadabra', 8), '==', 'rdr')
print(solve('abracadabra', 50), '==', '')
