from sys import stdin

def valid(passphrase):
    tokens = passphrase.split()
    s = set() 
    for token in tokens:
        if token in s:
            return False
        s.add(token)
    return True

if __name__ == '__main__':
    s = 0
    for phrase in stdin:
        v = valid(phrase)
        if v:
            s += 1
    print(s)