def estimate_pi():
	import math
	sum=0
	k=0
	C=(2.0*(math.sqrt(2.0)))/9801.0
	while True:
		num=factorial(4.0*k)*(1103.0+26390.0*k)
		denom=(factorial(k)**4.)*(396.**(4.0*k))
		inpi=C*num/denom
		sum=inpi+sum
		if abs(inpi)<=10**-15:
			return 1/sum
			break
		else:
			k=k+1
		
print estimate_pi()
