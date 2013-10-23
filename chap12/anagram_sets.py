def anagrams(wordlist):
    d={}
    allwords=open(wordlist)
    for line in allwords:
        word=line.strip().lower()
        t=list(word)
        t.sort()
        anagram=''.join(t)
        if anagram not in wordlist:
            d[t]=[word]
        else:
            d[t].append(word)
    return d

def length_anagram(d,n):
    res={}
    for word, otherwords in d.iteritems():
        if len(word)==n:
            res[word]=anagrams
    return res


