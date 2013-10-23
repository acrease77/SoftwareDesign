from pronounce import read_dictionary

def word_dictionary():
    d = dict()
    words = open('words.txt')
    for line in words:
        word = line.strip().lower()
        d[word] = word
    return d

def homophone(w1,w2,phone):
    if phone[a]==phone[b]:
        return True
    else:
        return False

reduced_homophones_check(word):
    dic=word_dictionary()
    phones=read_dictionary
    reduced1word=word[1:]
    reduced2word=word[0]+word[2:]
    if reduced1word in dic and reduced2word in dic and homophones(word,reduced1word,phones) and homophones(word,reduced2word,phones):
        return True
    else:
        return False

reduced_homophones():
    dic=word_dictionary()
    for word in dic:
        if reduced_hoophones_check(word):
            print word, word[1:], wprd[0]+word[2:]
    
