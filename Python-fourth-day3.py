scores = []
choise = None

while choise != "0" :
	print(
		'''
			Рекорды
			0 - Выйти
			1 - Показать рекорды
			2 - Добавить рекорд
		''')
	choise = input('Введите число ')
	if choise == '0':
		print('poka')
	elif choise == '1':
		print('Рекорды')
		print('ИМЯ\t Рекорд')
		for entry in scores:
			score,name = entry
			print(name,'\t',score)
	elif choise == '2':
		name = input('Ведите имя учасника ')
		score = int(input('Ведите  рекорд учасника '))
		entry = (score,name)
		scores.append(entry)
		scores.sort(reverse=True)
	else:
		print('Непонятный выбор значения : ',choise )