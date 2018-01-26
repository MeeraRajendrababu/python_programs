n=int(input())
a=[]
b=[]
for i in range(n):
	a.append(int(input()))
print(a)
for i in a:
	if i<5:
		b.append(i)
print(b)
