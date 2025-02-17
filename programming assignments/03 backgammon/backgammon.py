from cs1graphics import *
from time import sleep

unit_size = 50
screen_size = (unit_size*15, unit_size*13)
canvas = Canvas(screen_size[0], screen_size[1])

#xcoord = screen_size - unit_size
#ycoord = unit_size
#width = unit_size

#vertical_border = Rectangle(unit_size, unit_size*11)
#vertical_border.move(unit_size*.5, unit_size*6.5)    
#vertical_border.setFillColor('burlywood4')
#canvas.add(vertical_border)

for n in range(3):
    vertical_border = Rectangle(unit_size, unit_size*11, Point((unit_size*.5), (unit_size*6.5)))
    vertical_border.setFillColor('burlywood4')
    vertical_border.setBorderColor('burlywood4')
    if n == 1:
        vertical_border.move((unit_size*7),0)
    elif n == 2:
        vertical_border.move(unit_size*14, 0)
    canvas.add(vertical_border)

for n in range(2):
    horizontal_border = Rectangle(screen_size[0], unit_size, Point(screen_size[0]*.5, unit_size*0.5))
    horizontal_border.setFillColor('burlywood4')
    horizontal_border.setBorderColor('burlywood4')
    if n == 1:
        horizontal_border.move(0,unit_size*12)
    canvas.add(horizontal_border)

for n in range (2):
    board = Rectangle(unit_size*6, unit_size*11, Point(unit_size*4, unit_size*6.5))  
    board.setFillColor('navajowhite')
    if n == 1:
        board.move(unit_size*7,0)
    canvas.add(board)  



