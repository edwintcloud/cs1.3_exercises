def perm(text1, text2):
    return sum(ord(c) for c in text1) == sum(ord(c) for c in text2)


# test
one = 'abc'
two = 'bcaa'
print(perm(one, two))
