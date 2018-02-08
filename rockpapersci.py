a={'player1':'', 'player2':''}
n='Y'
while(n=='Y'):
	a['player1']=input('Play Player1 !')
	a['player2']=input('Play player 2!')
	if a['player1']==a['player2']:
		print('Nobody wins')
	elif a['player1']=='rock' and a['player2']=='scissors':
		print('Congrats player1')
	elif  a['player1']=='rock' and a['player2']=='paper':
		print('Congrats player2')
	elif  a['player1']=='scissors' and a['player2']=='rock':
		print('Congrats player2')
	elif  a['player1']=='scissors' and a['player2']=='paper':
		print('Congrats player1')
	elif  a['player1']=='paper' and a['player2']=='scissors':
		print('Congrats player2')
	elif  a['player1']=='paper' and a['player2']=='rock':
		print('Congrats player1')

	print('do you want to continue? (Y/N)')
	n=input()