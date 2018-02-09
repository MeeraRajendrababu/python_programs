import random
a=random.randint(1,9)
n=int(input())
if n<a:
	print('Too low')
elif n>a:
	print('Too high')
elif n==a:
	print('exactly right')

