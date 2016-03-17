geek = {"404": "Не знать. не владеть информацией. От сообщения об ошибке 404 'Страницане найдена'.",
		"Googling": "'Гугление·. nоиск в Сети сведений о ком-либо.",
		"Keyboard Pl aque" : "Мусор. который скапливается в клавиатуре компьютера.",
		"Link Rot" : "Процесс устаревания гиперссылок на веб-страницах . " ,
		"Percussive Maintenance" : "О ситуации. когда кто-либо бьет по корпусу не-исправного электронного прибора в надежде восстановить его работу.",
		"Uninstalled" : "Об увольнении кого-либо. Особенно популярно на рубеже 1990-2000-х годов . "}

choise = None

while choise != "0" :
	print(
		'''
			Рекорды
			0 - Выйти
			1 - Найти толкование термина
			2 - Добавить термин
			3 - Изменить толкование
			4 - Удалить толкование
			
		''')
	choise = input('Введите число ')
	if choise == '0':
		print('poka')
	elif choise == '1':
		temp = input('Что найти? ')
		if temp in geek:
			defin = geek[temp]
			print(temp,' означает ',defin)
		else:
			print('Извини мы не нашли ',temp)
	elif choise == '2':
		term = input("Kaкoй термин гикского языка вы хотите добавить? ")
		if term not in geek:
			definition = input("\nВпишите ваше толкование: ")
			geek[term] = definition
			print("\nTepмин ",term, " добавлен в словарь.")
		else:
			print("\nTaкoй термин уже есть! Попробуйте изменить его толкование.")
	elif choise == '3':
		term = input("Kaкoй термин вы хотите переопределить? ")
		if term in geek:
			definition = input("\nВпишите ваше толкование: ")
			geek[term] = definition
			print("\nTepмин ",term," переопределен.")
		else:
			print("\nTaкoгo термина пока нет! Попробуйте добавить его в словарь.")
	elif choise == '4':
		term = input("Kaкoй термин вы хотите переопределить? ")
		if term in geek:
			del geek[term]
			print("\nTepмин ",term," удален.")
		else:
			print("\nHичeм не могу помочь. Термина",term,"нет в словаре.")
	else:
		print('Непонятный выбор значения : ',choise )