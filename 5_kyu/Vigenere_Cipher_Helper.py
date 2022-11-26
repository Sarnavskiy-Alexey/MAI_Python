"""
    Reference: https://www.codewars.com/kata/vigenere-cipher-helper
"""


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        
        # лямба-функции нахождения индекса
        self.ret_sum_indexes = lambda a, b: (self.alphabet.find(a) + self.alphabet.find(b))
        self.ret_dif_indexes = lambda a, b: (self.alphabet.find(a) - self.alphabet.find(b))
        self.mod_alph = lambda idx: self.alphabet[idx % len(self.alphabet)]
    
    
    def encode(self, text):
        res = [(self.mod_alph(self.ret_sum_indexes(text[i], self.key[i % len(self.key)])) if text[i] in self.alphabet else text[i]) for i in range(len(text))]
        return ''.join(res)
    
    
    def decode(self, text):
        res = [(self.mod_alph(self.ret_dif_indexes(text[i], self.key[i % len(self.key)])) if text[i] in self.alphabet else text[i]) for i in range(len(text))]
        return ''.join(res)


def launch_test(en: str, de: str):
    abc = "abcdefghijklmnopqrstuvwxyz"
    key = "password"
    c = VigenereCipher(key, abc)
    
    print(c.encode(en), de, sep='\n')
    print(c.decode(de), en, sep='\n')


if __name__ == '__main__':
    launch_test('codewars', 'rovwsoiv')
