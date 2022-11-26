"""
    Reference: https://www.codewars.com//kata/5964d7e633b908e172000046
"""

const_alph = {"EORZ": 0, "ENO": 1, "OTW": 2, "EEHRT": 3, "FORU": 4, "EFIV": 5, "ISX": 6, "EENSV": 7, "EGHIT": 8, "EINN": 9}

def recover(st):
    res = ""
    for i in range(len(st) - 2):
        res += str(const_alph.get("".join(sorted(list(st[i:i + 3]))), str(const_alph.get("".join(sorted(list(st[i:i + 4]))), str(const_alph.get("".join(sorted(list(st[i:i + 5]))), ""))))))

    return res if len(res) else "No digits found"


if __name__ == '__main__':
    print(recover("NEO"), "1")
    print(recover("ONETWO"), "12")
    print(recover("TWWTONE"), "21")
    print(recover("ZYX"), "No digits found")
    print(recover("ONENO"), "11")
    print(recover("NEOTWONEINEIGHTOWSVEEN"), "12219827")
