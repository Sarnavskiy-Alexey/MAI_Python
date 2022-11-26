"""
    Reference: https://www.codewars.com//kata/52d2e2be94d26fc622000735
"""


class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        self.key = key
        self.abc = abc
        
        # лямба-функции нахождения индекса
        self.ret_sum_indexes = lambda a, b: (self.abc.find(a) + self.abc.find(b))
        self.ret_dif_indexes = lambda a, b: (self.abc.find(a) - self.abc.find(b))
        self.mod_alph = lambda idx: self.abc[idx % len(self.abc)]
        # лямбда-функция для замены не буквоцифр на пустоту
        self.rep_not_alnum = lambda text: ''.join([el for el in text if el in self.abc])
    
    
    def encode(self, text):
        new_key = self.key + self.rep_not_alnum(text)
        whitespaces = 0
        res = []
        for i in range(len(text)):
            res += (self.mod_alph(self.ret_sum_indexes(text[i], new_key[i - whitespaces])) if text[i] in self.abc else text[i])
            whitespaces += 1 if text[i] not in self.abc else 0
        return ''.join(res)
    
    
    def decode(self, text):
        new_key = list(self.key)
        whitespaces = 0
        res = []
        for i in range(len(text)):
            if text[i] in self.abc:
                c = self.mod_alph(self.ret_dif_indexes(text[i], new_key[i - whitespaces]))
                res += c
                if c.isalnum:
                    new_key += c
            else:
                res += text[i]
                whitespaces += 1
        return ''.join(res)


def launch_test(abc:str, key: str, en: str, de: str):
    c = VigenereAutokeyCipher(key, abc)
    
    print(c.encode(en), de, sep='\n')
    print(c.decode(de), en, sep='\n')


if __name__ == '__main__':
    launch_test("abcdefghijklmnopqrstuvwxyz", "password", 'codewars', 'rovwsoiv')
    launch_test("abcdefghijklmnopqrstuvwxyz", "password", 'amazingly few discotheques provide jukeboxes', 'pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib')
    launch_test("abcdefghijklmnopqrstuvwxyz", "password", 'aaaaaaaapasswordaaaaaaaa', 'passwordpasswordpassword')
    launch_test("abcdefghijklmnopqrstuvwxyz", "password", "xt'k s ovzib vhhhwy!", "mt'c k kjqly orzvrx!")
    launch_test('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'PASSWORD', 'AAAAAAAAPASSWORDAAAAAAAA', 'PASSWORDPASSWORDPASSWORD')
    launch_test('アイウエオァィゥェォカキクケコサシスセソタチツッテトナニヌネノハヒフヘホマミムメモヤャユュヨョラリルレロワヲンー', 'カタカナ', 'ドモアリガトゴザイマス', 'ドレタウガロゴザヤマォ')
