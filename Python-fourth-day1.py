invent = ['меч','щит','кольчуга','лук','стелы']
print('И так в нашем арсенале')
for item in invent:
	print(item)

print('Сейчас у нас ',len(invent),' предметов')

index = int(input('Введите индекс '))
print('Под номером ',index,'в арсенале хранится ',invent[index])


print('Вы обменяли лук на арбалет')
invent[3] = 'арбалет'

print('И так в нашем арсенале теперь есть: ')
for item in invent:
	print(item)