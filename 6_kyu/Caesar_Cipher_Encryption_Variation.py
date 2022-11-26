"""
    Reference: https://www.codewars.com//kata/55ec55323c89fc5fbd000019
"""

def caesar_encode(phrase, shift):
    s = ""
    sh = shift
    for i in phrase:
        if i != ' ':
            s += chr(((ord(i) + sh % 26) - 97) % 26 + 97)
        else:
            s += i
            sh += 1
    return s

if __name__ == '__main__':
    print(caesar_encode("alea iacta est", 3) == "dohd megxe jxy")
    print(caesar_encode("conquer et impera", 13) == "pbadhre sh xbetgp")
    print(caesar_encode("fere libenter homines id quod volunt credunt", 7) == "mlyl tqjmvbmz qxvrwnb sn bfzo haxgzf perqhag")
    print(caesar_encode("horum omnium fortissimi sunt belgae", 0) == "horum pnojvn hqtvkuukok vxqw fipkei")
