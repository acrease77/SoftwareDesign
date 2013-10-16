def consecutive_double_letters(word):
    i=0
    while i<=len(word)-1:
        if i+6>len(word):
            return False    
        elif word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
            return True
        else:
            i=i+1
    return False
        
def find_words(function):
    wordlist = open('words.txt')
    for line in wordlist:
        word = line.strip()
        if function(word):
            print word

#find_words(consecutive_double_letters)

def palinum(number,first,last):
    word=str(number)
    cutword=word[first:last]
    return cutword==cutword[::-1]

def odometer_palindrome(number):
    if palinum(number+3,0,6) and palinum(number+2,1,5) and palinum(number+1,1,6) and palinum(number,2,6):
        return True
    else:
        return False

def full_odometer_check():
    i=100000
    while i<=999999:
        if odometer_palindrome(i):
            print i
        i=i+1

full_odometer_check()



    




    

