"""Module that provides is_palindrome.

Author of is_palindrome: you
"""

def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]


def is_palindrome(word):
    """Returns True if word is a palindrome and False if not
        
    word: string

    returns: Boolean
    """

    if len(word)==0:
		return 'Not a word!'
	lf=word[0]
	ll=word[-1]
	lm=word[1:-1]
	if lf!=ll:
		return False
	elif lf==ll and ''==lm:
		return True
	else:
		return is_palindrome(word[1:-1])
