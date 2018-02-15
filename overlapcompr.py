a=[int(input()) for i in range(int(input()))]
b=[int(input()) for i in range(int(input()))]
c=[i for i in set(a) if i in set(b)]
print(c)