country = input('where are you form')
age = int(input('how old are you'))
if country == 'Taiwan':
	if age >= 18:
		print('you can drive')
	else :
		print('you can not drive')
elif country == 'America':
	if age >= 16:
		print('you can drive')
	else :
		print('you can not dirve')
		