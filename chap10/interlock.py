def word_list():
    t = []
    worddoc = open('words.txt')
    for line in worddoc:
        word = line.strip()
        t.append(word)
    return t

def interleave(word1,word2):
    worddoc=open('words.txt')    
    i=0
    interleaved=''   
    while i <= (len(word1)-1):
        interleaved=interleaved+word1[i]+word2[i]
        i+=1
    for word in worddoc:
        if interleaved==word:
            return True
        
def interlock1(word1):
    wordlist=word_list()    
    for word2 in wordlist:
        if interleave(word1,word2):
            return True

def interlock():
    wordlist=word_list()
    for firstword in wordlist:
        if interlock1(firstword):
            return word1, word2

print interlock()


    
