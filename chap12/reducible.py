def word_dictionary():
    d = dict()
    words = open('words.txt')
    for line in words:
        word = line.strip().lower()
        d[word] = word
    d['a']='a'
    d['i']='i'
    d['']=''
    return d
def word_dictionary():
    d=dict()
    allwords=open('words.txt')
    for line in allwords:
        word=line.strip()
        d[word]=word
    return d

def is_reducible(word):
    memo={}
    reducers=[]
    memo['']=['']
    if word in memo:
        return memo[word]
    for reduced in reducers(word):
        shorter=is_reducible(reduced)
        if shorter:
            res.append(reduced)
    memo[word]=reducers
    return reducers
        

def reducers(word):
    dic=word_dictionary()
    reducedwords=[]
    for i in range(len(word)):
        reduceword=word[:1]+word[i+1:]
        if reduceword in dic:
            reducedwords.append(reduceword)
    return reducedwords

def check_all():
    dic=word_dictionary()
    reducablelist=[]
    for word in dic:
        reducing=is_reducible(word)
        if reducing!=[]:
            reducablelist.append(word)
    return res            
    
def all_words_list(word):
    if len(word)==0:
        return
    print word,
    shorter=is_reducible(word)
    all_words_list(shorter[0])

def longest():
    allwords=word_dictionary()
    reducelong=[]
    for word in allwords:
        reducelong.append((len(word),word))
    reducelong.sort()
    all_words_list(reducelong[-1:])
        
      
    
  
                


