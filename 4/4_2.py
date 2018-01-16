from sys import stdin

def valid(passphrase):
    tokens = passphrase.split()
    s = set()
    for token in tokens:
        v = ''.join(sorted(token))
        if v in s:
            return False
        s.add(v)
    return True

if __name__ == '__main__':
    s = 0
    for phrase in stdin:
        v = valid(phrase)
        s += (1 if v else 0)
    print(s)