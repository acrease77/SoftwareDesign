def rotate_word(word,rotation):
	for letter in word:
		if 90>=ord(letter)>=65:
			numcode=((ord(letter)-65+rotation)%26)+65
        elif 122>=ord(letter)>=97:
			numcode=((ord(letter)-97+rotation)%26)+97
        else:
			numcode=ord(letter)
		print chr(numcode),

rotate_word('cheer',7)
