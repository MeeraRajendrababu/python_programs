n=input()
l=len(n)
flag=0
b=[]
a=list(n)
for i in reversed(a):
	b.append(i)
for i,j in zip(a,b):
	if i==j:
		flag=1
	else:
		flag=0
if flag==1:
	print("{} is palindrome ".format(n))
else: 
	print("{} is not plaindrome " .format(n))	





