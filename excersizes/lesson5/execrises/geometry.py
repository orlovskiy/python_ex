# -*- coding: utf-8 -*-

"""
Это пример небольшой программы для рисования кругов и квадратов.
Вам нужно на основе этой программы сделать небольшую "танцевальную" сценку с
использованием кругов, квардратов и треугольников. Сделать всё это нужно в
объектно ориентированном стиле.

Какие классы нужно реализовать:

-Многоугольник(на его основе сделать квадрат и правильный треугольник)
--класс должне уметь отрисовывать себя
--премещаться в некоторм направлении заданом координатами x, y
--увеличивать(необязательно)
--поворачивать(необязательно)

-Квардрат(наследуется от многоугольника)
--метод __init__ принимает координаты середины, ширину и цвет

-Треугольник(наследуется от многоугольника)
--метод __init__ принимает координаты середины, длинну грани и цвет

-Круг
--метод __init__ принимает координаты середины, радиус и цвет
--класс должне уметь отрисовывать себя
--премещаться в некоторм направлении заданом координатами x, y
--увеличивать(необязательно)

Также рекомендую создать вспомогательный сласс Vector для представления
точек на плоскости и различных операций с ними - сложение, умножение на число,
вычитаные.


Из получившихся классов нужно составить какую-нибудь динамическую сцену.
Смотрите пример example.gif
"""

import turtle
import time
import random
import math

class Figure(object):
    '''Базовый класс "Фигура"
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = self.__class__.__name__

    def move(self, x_end, y_end):
        self.x = self.x + x_end
        self.y = self.y + y_end
        x_start = self.x
        y_start = self.y

        #controls:
            #step
        x_shift = 1
        y_shift = 1
            #speed
        delay = 0.01
        print self.name + " is moving to coord's",
        time.sleep(delay)
        if x_end > y_end:
            check = x_start + x_end
            while self.x < check:
                if self.y < y_start + y_end:
                    y_shift = y_shift
                else:
                    y_shift = 0
                self.x = self.x + x_shift
                self.y = self.y + y_shift
                print "({0},{1})".format(self.x, self.y),
                time.sleep(delay)

        elif x_end < y_end:
            check = y_start + y_end
            while self.y < check:
                if self.x < x_start + x_end:
                    x_shift = x_shift
                else:
                    x_shift = 0
                self.x = self.x + x_shift
                self.y = self.y + y_shift
                print "({0},{1})".format(self.x, self.y),
                time.sleep(delay)

        else:
            check = x_start + x_end
            while self.x < check:
                if self.x < y_start + y_end:
                    y_shift = y_shift
                else:
                    y_shift = 0
                self.x = self.x + x_shift
                self.y = self.y + y_shift
                print "({0},{1})".format(self.x, self.y),
                time.sleep(delay)
        print "\r"

    def random_move(self, speed):
        self.x = self.x + random.randint(-speed, speed)
        self.y = self.y + random.randint(-speed, speed)


class Circle(Figure):
    '''Класс "Круг"
    '''
    def __init__(self,x, y, r):
        super(Circle, self).__init__(x, y)
        self.r = r

    def draw(self):
        ttl.color('black')
        ttl.penup()
        ttl.setpos(self.x, self.y - self.r)
        ttl.pendown()
        ttl.circle(self.r)



class Rectangle(Figure):
    '''Класс "Прямоугольник"
    '''
    def __init__(self, x, y, w, h):
        super(Rectangle, self).__init__(x, y)
        self.w = w
        self.h = h

    def draw(self):
        ttl.color('red')
        ttl.penup()
        ttl.setpos(self.x - self.w / 2, self.y - self.h / 2)
        ttl.pendown()
        ttl.goto(self.x + self.w / 2, self.y - self.h / 2)
        ttl.goto(self.x + self.w / 2, self.y + self.h / 2)
        ttl.goto(self.x - self.w / 2, self.y + self.h / 2)
        ttl.goto(self.x - self.w / 2, self.y - self.h / 2)




class Quadrangle(Rectangle):
    '''Класс "Квадрат"
    '''
    def __init__(self,x, y, w, h):
        super(Quadrangle, self).__init__(x, y, w, h)
        self.w = self.h


class Triangle(Figure):
    def __init__(self, x, y, a, b, c):
        super(Triangle, self).__init__(x, y)
        self.a = a
        self.b = b
        self.c = c

class EqualTriangle(Triangle, Figure):
    '''Класс Треугольник
    '''
    def __init__(self, x, y, a, b, c):
        super(EqualTriangle, self).__init__(x, y, a, b, c)

    def draw(self):
        ttl.color('green')
        ttl.penup()
        ttl.setpos(self.x, self.y + math.sqrt(0.75 * self.b ** 2)/2)
        ttl.pendown()
        ttl.goto(self.x - self.b/2, self.y - math.sqrt(0.75 * self.b ** 2)/2)
        ttl.goto(self.x + self.b/2, self.y - math.sqrt(0.75 * self.b ** 2)/2)
        ttl.goto(self.x, self.y + math.sqrt(0.75 * self.b ** 2)/2)



circle = Circle(30,30,40)
quadrangle = Quadrangle(30,30,50,50)
rectangle = Rectangle(30,30,40,30)
triangle = EqualTriangle(30,30,20,60,60)

# def draw_rect(ttl):
#     x = random.randint(-200, 200) #получаем случайные координаты
#     y = random.randint(-200, 200)

#     ttl.color('red') #устанавливаем цвет линии
#     ttl.penup() # убираем "ручку" от холста, чтобы переместить в нужное место
#     ttl.setpos(x, y) # перемещаем на первую вершину
#     ttl.pendown() #опускаем ручку обратно
#     ttl.goto(x + 50, y) #проводим линии для сторон четырёхугольника
#     ttl.goto(x + 50, y + 50)
#     ttl.goto(x, y + 50)
#     ttl.goto(x, y)

# def draw_circle(ttl):
#     x = random.randint(-200, 200) #получаем случайные координаты
#     y = random.randint(-200, 200)

#     ttl.color('violet') #устанавливаем цвет линии
#     ttl.penup() # убираем "ручку" от холста, чтобы переместить в нужное место
#     ttl.setpos(x, y) # перемещаем в "основание" - это будет самая низкая точка
#     ttl.pendown() #опускаем ручку обратно

#     ttl.circle(25) #рисуем круг радиуса 25



# def main():
turtle.tracer(0, 0) #устанавливаем все задержки в 0, чтобы рисовалось мгновенно
turtle.hideturtle() #убираем точку посередине

ttl = turtle.Turtle() #создаём объект черепашки для рисования
ttl.hideturtle() #делаем её невидимой

while True:
    time.sleep(0.2) #засыпаем на полсекунды, чтобы увидеть что нарисовали
    ttl.clear() #очищаем всё нарисованое ранее
    rectangle.draw()
    rectangle.random_move(100)
    triangle.draw()
    triangle.random_move(100)
    circle.draw()
    circle.random_move(20)
    quadrangle.draw()
    quadrangle.random_move(40)

    turtle.update() #т.к. мы сделали turtle.tracer(0, 0) нужно обновить экран, чтобы увидеть нарисованное

# if __name__ == '__main__':
#     main()
