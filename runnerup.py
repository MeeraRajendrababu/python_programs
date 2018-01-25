n=int(input())
s=input()
a=s.split()
sett=set(a)
lis=list(sett)
x=[int(i) for i in lis]
x.remove(max(x))
print(max(x))

