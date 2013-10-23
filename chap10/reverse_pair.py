def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter
    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)

def rotate_word(word, n):
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res

def word_dictionary():
    d=dict()
    allwords=open('words.txt')
    for line in allwords:
        word=line.strip()
        d[word]=word
    return d

def rotate_pairs(word):
    dictionary=word_dictionary()
    for i in range(1,26):
        newword=rotate_word(word,i)
        

    
