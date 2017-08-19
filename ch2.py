word = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

original = word
word = list(word)
word2 = word

def f(x):
    return {
        'a': 'c',
        'b': 'd',
        'c': 'e',
        'd': 'f',
        'e': 'g',
        'f': 'h',
        'g': 'i',
        'h': 'j',
        'i': 'k',
        'j': 'l',
        'k': 'm',
        'l': 'n',
        'm': 'o',
        'n': 'p',
        'o': 'q',
        'p': 'r',
        'q': 's',
        'r': 't',
        's': 'u',
        't': 'v',
        'u': 'w',
        'v': 'x',
        'w': 'y',
        'x': 'z',
        'y': 'a',
        'z': 'b',
    }[x]

word = (map(f, word))
print word

'''
print ''.join(word2)

word2 = ['m' if x=='k' else x for x in word2]
word2 = ['q' if x=='o' else x for x in word2]
word2 = ['g' if x=='e' else x for x in word2]

print 'k: ', original.count('k')
print 'o: ', original.count('o')
print 'e: ', original.count('e')
print 'm: ', original.count('m')
print 'q: ', original.count('q')
print 'g: ', original.count('g')
'''
