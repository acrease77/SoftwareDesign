def word_list():
    t = []
    worddoc = open('words.txt')
    for line in worddoc:
        word = line.strip()
        t.append(word)
    return t

def check_reverse(word1):
    t=word_list()
    for word2 in t:
        if word1[::-1]==word2:
            return True
    
def reverse_pair():
    t=word_list()
    reverses=[]
    for word in t:
        if check_reverse(word):
            print word, word[::-1]
            reverses.append(word)

reverse_pair()
    
