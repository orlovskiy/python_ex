#!/usr/bin/python
#coding:utf-8

__author__ = 'Daniil Orlovskiy'

""" Ремонт в квартире 

Есть квартира (2 комнаты и кухня). В квартире планируется ремонт: нужно 
поклеить обои, покрасить потолки и положить пол.

Необходимо рассчитать стоимость материалов для ремонта.

Из описания следуют следующие классы:
= Строительные материалы
  = Обои
  = Потолочная краска
  = Ламинат
= Комната
= Квартира

Подробнее, с методами (+) и атрибутами (-):
= Строительные материалы
  - площадь (кв. м)
  - цена за единицу (рулон, банку, упаковку)
  = Обои
    - ширина рулона
    - длина рулона
  = Потолочная краска
    - вес банки
    - расход краски
  = Ламинат
    - длина доски
    - ширина доски
    - кол-во досок в упаковке
= Комната
  - ширина
  - высота
  - длина
  - ширина окна
  - ширина двери
  + поклеить обои
  + покрасить потолок
  + положить пол
  + посчитать смету на комнату
  + при создании комнаты сразу передавать все атрибуты в конструктор __init__()
= Квартира
  - комнаты
  + добавить комнату
  + удалить комнату
  + посчитать смету на всю квартиру
  + при создании можно передать сразу все комнаты в конструктор

Необходимо создать стройматериалы, назначить им цены и размеры.
Создать комнаты, поклеить, покрасить и положить все на свои места.
Cоздать квартиру, присвоить ей комнаты и посчитать общую смету.

Подсказка: для округления вверх и вниз используйте:
import math
math.ceil(4.2)  # 5
math.floor(4.2) # 4

Примечание: Для простоты, будем считать, что обои над окном и над дверью 
не наклеиваются.
----------------

Дополнительно:
Сделать у объекта квартиры метод, выводящий результат в виде сметы:

[Комната: ширина: 3 м, длина: 5 м, высота: 2.4 м]
Обои        400x6=2400 руб.
Краска     1000x1=1000 руб.
Ламинат     800x8=6400 руб.
[Комната: ширина: 3 м, длина: 4 м, высота: 2.4 м]
Обои        400x5=2000 руб.
Краска     1000x1=1000 руб.
Ламинат     800x7=5600 руб.
[Кухня: ширина: 3 м, длина: 3 м, высота: 2.4 м]
Обои        400x4=1600 руб.
Краска     1000x1=1000 руб.
Ламинат     800x5=4000 руб.
---------------------------
Итого: 25000 руб.

"""

import sys
import __main__
import math


purposes = {'1':'пол', '2':'стены', '3':'потолок'}
materials = {}
materials_needed = {}
rooms = {}
room_id = 1
class Materials(object):#не знаю пока зачем он нужен мне тут
	'''Строительные материалы
	'''

	def __init__(self, name = '', purpose = 0, length = 0, width = 0, pack_quantity = 0, pack_price = 0, usage = 0, quantity = 0):
		self.name = name
		self.purpose = purpose
		self.length = length
		self.width = width
		self.pack_quantity = pack_quantity
		self.pack_price = pack_price
		self.usage = usage
		self.quantity = quantity

	def __str__(self):
		return '''{0} 
		Назначение: {1}
		Размеры: {2}см х {3}см ({4} шт в упаковке)
		Цена за упаковку: {5} руб.
		Расход: {6} кг/м2
		Покрытие: {7} м2/уп'''.format(self.name, purposes[self.purpose], self.length, self.width, self.pack_quantity, self.pack_price, self.usage, self.coverage)

	@staticmethod
	def new():
		name = str(raw_input('Наименование материала, фирма - изготовитель: ') or 'Не указано')
		purpose = str(raw_input('Назначение. 1 - пол, 2 - стены, 3 - потолок: '))
		length = float(raw_input('Длина, см: ') or 0)
		width = float(raw_input('Ширина, см: ') or 0)
		quantity = float(raw_input('Количество в упаковке, шт (кг для красок): ') or 0)
		price = int(raw_input('Цена за упаковку, руб: ') or 0)
		usage = float(raw_input('Расход краски, кг/м2: ') or 0)
		
		return Materials(name, purpose, length, width, quantity, price, usage)

	@property	
	def coverage(self):
		if self.length ==0 and self.width ==0:
			return self.pack_quantity / self.usage
		else:
			return self.length * self.width * self.pack_quantity/10000








class Flat(object):
	'''
	'''
	def __init__(self,rooms = 0):
		self.rooms = rooms

	def __str__(self):
		return "flat 1"

	# def square(self):

	# def checkout(self):

	@staticmethod
	def add_room():
		global room_id
		name = str(raw_input('Наименование комнаты: ') or 'Не указано')
		length = float(raw_input('Длина, м: ') or 0)
		width = float(raw_input('Ширина, м: ') or 0)
		height = float(raw_input('Высота, м: ') or 0)
		window_width = float(raw_input('Ширина окна, м: ') or 0)
		window_height = float(raw_input('Высота окна, м: ') or 0)
		windows = float(raw_input('Количество окон, м: ') or 0)
		door_width = float(raw_input('Ширина двери, м: ') or 0)
		door_height = float(raw_input('Высота двери, м: ') or 0)
		doors = float(raw_input('Количество дверей, м: ') or 0)
		return Room(name, length, width, height, window_width, window_height, windows, door_width, door_height, doors, room_id)

	@staticmethod
	def del_room(target):
		global room_id
		for room in rooms.values():
			if rooms[target].room_id < room.room_id:
				room.room_id = int(room.room_id) - 1
		del rooms[target]
		room_id -= 1
		
		return rooms

	def checkout(self):
		total_flat_price = 0
		for name, room in rooms.items():
			total_room_price = room.checkout()
			total_flat_price += total_room_price
		print '''



		ИТОГО: {0} рублей'''.format(total_flat_price)


class Room(Flat):
	'''
	'''
	def __init__(self, name, length, width, height, window_width, window_height, windows, door_width, door_height , doors, initial_id):
		self.name = name
		self.length = length
		self.width = width
		self.height = height
		self.window_width = window_width
		self.window_height = window_height
		self.windows = windows
		self.door_width = door_width
		self.door_height = door_height
		self.doors = doors
		self.room_id = initial_id
		global room_id
		room_id +=1
		materials_needed[self.name] = {}

	def __str__(self):
		return '''id: {0}
Наименование комнаты: {1}
Площадь: {2} м2 
Площадь стен: {3} м2
Дверей: {4}
Окон {5}


'''.format(self.room_id, self.name, self.floor_square, self.walls_square, self.doors, self.windows)

	@property
	def walls_square(self):
		return (self.width * self.height * 2 + self.length * self.height * 2 ) - (self.window_width * self.window_height * self.windows + self.door_width * self.door_height * self.doors)

	@property
	def floor_square(self):
		return self.length * self.width
	
	def attach_floor(self):
		for material in materials.values():
			if material.purpose == '1':
				packs_needed = math.ceil(self.floor_square / material.coverage)
				packs_price = int(packs_needed * material.pack_price)
				materials_needed[self.name][material.name] = {1:packs_needed, 2:packs_price}
		print '''

Сделано!


				'''

	def attach_wallpaper(self):
		for material in materials.values():
			if material.purpose == '2':
				packs_needed = math.ceil(self.walls_square / material.coverage)
				packs_price = int(packs_needed * material.pack_price)
				materials_needed[self.name][material.name] = {1:packs_needed, 2:packs_price}
		print '''

Сделано!


				'''

	def paint_top(self):
		for material in materials.values():
			if material.purpose == '3':
				packs_needed = math.ceil(self.floor_square / material.coverage)
				packs_price = int(packs_needed * material.pack_price)
				materials_needed[self.name][material.name] = {1:packs_needed, 2:packs_price}
		print '''

Сделано!


				'''

	def checkout(self):

		total_room_price = 0
		print '''
{0:-^50}
Длина:{1}м, Ширина:{2}м, Высота:{3}м'''.format(self.name, str(int(self.length)), str(int(self.width)), str(int(self.height)))
		for material_name, material_data in sorted(materials_needed[self.name].items()):
			total_room_price += material_data[2]
			room_data = self.name + str(int(self.length))+ str(int(self.width))+ str(int(self.height))
			print'''{0} {1}x{2} = {3} рублей'''.format(material_name, int(materials[material_name].pack_price), int(material_data[1]), material_data[2])
		print '''Итого: {0:_>10}  рублей

		'''.format(total_room_price)
		return total_room_price
def flat_menu():
	choice = 0
	while choice != '':
		choice = flat_menu_pick()
		if choice ==  1:
			new_room = Flat.add_room()
			rooms[new_room.name] = new_room

		elif choice == 2:
			room_list()
			del_id = int(raw_input("Введите id комнаты, которую хотите удалить >>> "))
			for room in rooms.values():
				if room.room_id == del_id:
					target = room.name
			Flat.del_room(target)

		elif choice == 3:
			flat.checkout()

		elif choice == 4:
			room_list()
			raw_input('>>> ')

		elif choice == 5:
			room_list()
			desired_room_id = int(raw_input("Введите id нужной комнаты >>> "))
			room = room_pick(desired_room_id)
			room_menu(room)

		elif choice == 6:
			sys.exit(1)
		else:
			flat_menu_pick()
	sys.exit(1)



def flat_menu_pick():
	return	int(raw_input('''{1}{0:-^50}
{1}1 - добавить комнату
{1}2 - удалить комнату
{1}3 - посчитать смету на всю квартиру
{1}4 - получить список комнат
{1}5 - войти в меню комнаты
{1}6 - завершить программу
>>> '''.format('МЕНЮ КВАРТИРЫ',' ' * 50)) or 0 )

def room_menu(room):
	choice = 0
	while choice != '':
		choice = room_menu_pick(room)
		if choice ==  1:
			room.attach_floor()

		elif choice == 2:
			room.attach_wallpaper()

		elif choice == 3:
			room.paint_top()

		elif choice == 4:
			room.checkout()

		elif choice == 5:
			break
		else:
			room_menu_pick()

def room_menu_pick(room):
	return int(raw_input('''{0:-^50}
{1:-^20}
1 - положить пол
2 - поклеить обои
3 - покрасить потолок
4 - посчитать смету на комнату
5 - вернуться в меню квартиры
>>> '''.format('МЕНЮ КОМНАТЫ', room.name)) or 0)

def room_pick(desired_room_id):
	for room in rooms.values():
		if room.room_id == desired_room_id:
			return room

def room_list():
	for room in sorted(rooms.values()):
		print '''{0:_^30}
{1:-^20}
{2:_^10}'''.format(room.name, room, '_')

print "{:-^100}".format('Ремонт v1')

while raw_input('''Нажмите Ввод для перехода к вводу данных о материалах.
	Введите 'done' для перехода к слудующему этапу ремонта
	>>> ''') != 'done':
	new_material = Materials.new()
	materials[new_material.name] = new_material
	print "{:*^100}".format('Введены данные о материалах:')
	for material in materials.values():
		print material

print "{:-^100}".format('Данные квартиры')
flat = Flat(0)
print flat

flat_menu()



# class Figure(object):
# 	'''Документация по кдассу 'Фигуры'
# 	'''
# 	def __init__(self, x = 0, y = 0):
# 		self.x = x
# 		self.y = y

# 	def __str__(self):
# 		return "I'm a Figure my coord's is: x:{0}, y:{1}".format(self.x, self.y)
	




# class Rectangle(Figure):
# 	'''Документация по Фигуре: Прямоугольник
# 	'''
# 	def __init__(self, x = 0, y = 0, w = 0, h = 0):
# 		super(Rectangle,self).__init__(x,y)
# 		self.w = w
# 		self.h = h

# 	def __str__(self):
# 		base =	super(Rectangle).__str__()
# 		res =  base + " also I'm a Rectangle object and my dimensions is: w:{0}, h:{1}".format(self.w, self.h)
# 		return res

# 	@staticmethod
# 	def new():
# 		x = int(raw_input('x: ') or 0)
# 		y = int(raw_input('y: ') or 0)
# 		w = int(raw_input('w: ') or 0)
# 		h = int(raw_input('h: ') or 0)
# 		return Rectangle(x, y, w, h)

# rects = []
# rectangle_quantity = raw_input('Cколько прямоугольников?') or 0
# for i in range(int(rectangle_quantity)):
# 	rects.append(Rectangle.new())


# print rects
# print type(rects[1])
