def startend(a):
	b=[]
	b.append(a[0])
	b.append(a[-1])
	return b
def main():
	b=[]
	a=[int(input()) for i in range(int(input()))]
	b=startend(a)
	print(b)
if __name__=='__main__':
	main()
	
