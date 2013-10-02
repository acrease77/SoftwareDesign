def is_power(a,b):
	if a==0:
		return 'Not possible'
	elif b==0:
		return "It's 0!!"
	if a%b!=0:
		return False
	elif a/b==1 and a%b==0:
		return True
	else:
		return is_power(a/b,b)

def gcd(a,b):
	if not isinstance(a,int) or not isinstance(b,int):
		print 'Nope!'
		return None
	if a%b==0 or a==b:
		return b
	elif b%a==0:
		return a
	else:
		if a>=b:
			r=a%b
		else:
			r=b%a
	return gcd(b,r)
