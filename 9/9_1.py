from sys import stdin
# Both the parts of the puzzle are in this file
def groups(s):
    n = len(s)
    i = 0
    garbage = False
    level = 0
    score = level

    while i<n:
        if not garbage:
            if s[i] == '{':
                level += 1
                score += level
            elif s[i] == '}':
                level -= 1
            elif s[i] == '<':
                garbage = True
        else:
            if s[i] == '!':
                i += 1
            elif s[i] == '>':
                garbage = False
        i += 1
    
    return score

def groups_no_garbage(s):
    n = len(s)
    i = 0
    garbage = False
    chars = 0

    while i<n:
        if not garbage:
            if s[i] == '<':
                garbage = True
        else:
            chars += 1
            if s[i] == '!':
                chars -= 1
                i += 1
            elif s[i] == '>':
                chars -= 1
                garbage = False

        i += 1
    
    return chars

for test in stdin:
    print(groups(test))
    print(groups_no_garbage(test))
