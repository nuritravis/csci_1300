from cs1graphics import *

unit_size = 50
num_levels = 8
num_squares = num_levels
screen_size = unit_size * (num_levels+1)
canvas = Canvas(screen_size, screen_size)

xcoord = screen_size - unit_size
ycoord = unit_size
width = unit_size 

for i in range(num_levels, 0, -1): 
    xcoord = unit_size
    for n in range(i):
        block = Square(width)
        block.move(xcoord, ycoord)
        block.setFillColor('gray')
        canvas.add(block)
        xcoord += unit_size
    ycoord += unit_size


