"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import string
import random

prefix_suffix={}
prefix=()


def process_file(filename, skip_header=True):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = file(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        process_line(line, hist)
		for word in line.rstrip().split():
			make_prefix_things(word)
    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_line(line, hist):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """
    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    
    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1


def most_common(hist):
    """Makes a list of the key-value pairs from a histogram and
    sorts them in descending order by frequency.

    hist: map from word to the number of times it appears

    returns: list of (word, frequency) pairs, sorted by frequency
    """
    t = []
    for key, value in hist.items():
		t.append((value, key))
	t.sort()
	t.reverse()
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    
    hist: histogram (map from word to frequency
    num: number of words to print
    """
    t = most_common(hist)
    print 'The most common words are:'
    for freq, word in t[:num]:
        print word, '\t', freq


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries

    returns: new dictionary
    """
    res = {}
    for key in d1:
		if key not in d2:
			res[key]=None
    return res


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    t=[]
	for word,freq in hist.items():
		i=0
		while i < freq:
			t.append(word)
			i+=1
	return random.choice(t)

def make_prefix_things(word):
	global prefix
	if len(prefix)<2:
		prefix=word,prefix
		return
	else:
		prefixmap[prefix]=[word]
	prefix=t[1:]+(word,)		
	

def make_gibberish():
	start=random_word(hist)
	i=0
	global prefix_suffix
	while i<100:
		suffixes=prefix_suffix.get(start,None)
		if suffixes==None:
			make_gibberish(n-i)
			i+=1
			return
		else:
			word=random.choice(suffixes)
			print word,
			start=start[1:]+(word,)
		


if __name__ == '__main__':
    hist = process_file('emma.txt', skip_header=True)
    print make_gibberish()

