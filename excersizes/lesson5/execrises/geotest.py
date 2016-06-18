# -*- coding: utf-8 -*-

import sys
import time

x_coord = 1
y_coord = 5
start_x_coord = 1
start_y_coord = 5
x_end  = 25
y_end  = 25

x_shift = 1
y_shift = 1

if x_end > y_end:
	check = start_x_coord + x_end
	while x_coord < check:
		if y_coord < start_y_coord + y_end:
			y_shift = 1
		else:
			y_shift = 0
		x_coord = x_coord + x_shift
		y_coord = y_coord + y_shift
		print x_coord, y_coord
		time.sleep(0.6)

elif x_end < y_end:
	check = start_y_coord + y_end
	while y_coord < check:
		if x_coord < start_x_coord + x_end:
			x_shift = 1
		else:
			x_shift = 0
		x_coord = x_coord + x_shift
		y_coord = y_coord + y_shift
		print x_coord, y_coord
		time.sleep(0.6)
else:
	check = start_x_coord + x_end
	while x_coord < check:
		if y_coord < start_y_coord + y_end:
			y_shift = 1
		else:
			y_shift = 0
		x_coord = x_coord + x_shift
		y_coord = y_coord + y_shift
		print x_coord, y_coord
		time.sleep(0.6)




