a=[]
b=[]
c=[]
n=int(input("size of first list"))
m=int(input("size of second list"))
for i in range(n):
	a.append(int(input()))
for i in range(m):
	b.append(int(input()))
print(a)
print(b)
a=set(a)
b=set(b)
a=list(a)
b=list(b)
for i in a:
	for j in b:
		if i==j:
			c.append(j)
print(c)


