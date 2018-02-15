bool=0
n=int(input())
for i in range(2,int(n/2)):
	if n%i==0:
		bool=1
if bool==0:
	print('{} is a prime number'.format(n))
else:
	print('{} is not a prime number'.format(n))