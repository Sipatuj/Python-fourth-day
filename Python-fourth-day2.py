scores = []
choise = None

while choise != "0" :
	print(
		'''
			Рекорды
			0 - Выйти
			1 - Показать рекорды
			2 - Добавить рекорд
			3 - Удалить рекорд
			4 - Сортировать список
			
		''')
	choise = input('Введите число ')
	if choise == '0':
		print('poka')
	elif choise == '1':
		print('Рекорды')
		for score in scores:
			print(score)
	elif choise == '2':
		score = int(input('Ведите свой рекорд'))
		scores.append(score)
	elif choise == '3':
		for score in scores:
			print(score)
		score = int(input('Выберите какой рекорд удалить?'))
		if score in scores:
			scores.remove(score)
		else:
			print('Такого значения ',score,' в списке рекордов нету')
	elif choise == '4':
		scores.sort(reverse=True)
	else:
		print('Непонятный выбор значения : ',choise )