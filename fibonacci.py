n=int(input('Enter the number of terms in sequence'))
a=0
b=1
print('0\n1')
for i in range(2,n):
	c=a+b
	print(c)
	a=b
	b=c