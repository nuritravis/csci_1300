from cs1graphics import *

unit_size = 50
num_squares = 8
screen_size = unit_size * (num_squares+1)
canvas = Canvas(screen_size, screen_size)

xcoord = screen_size - unit_size
ycoord = unit_size
width = unit_size 

for n in range(num_squares):
    block = Square(width)
    block.move(xcoord, ycoord)
    block.setFillColor('gray')
    canvas.add(block)

    xcoord -= unit_size
    ycoord += unit_size

