"""
    Reference: https://www.codewars.com//kata/52ea928a1ef5cfec800003ee
"""


def ip_to_int32(ip):
    n1 = int(ip[:ip.find('.')])
    n4 = int(ip[ip.rfind('.') + 1:])
    n2 = ip[ip.find('.') + 1:]
    n3 = n2[n2.find('.') + 1:]
    n2 = int(n2[:n2.find('.')])
    n3 = int(n3[:n3.find('.')])
    return n1 * (256 ** 3) + n2 * (256 ** 2) + n3 * 256 + n4
