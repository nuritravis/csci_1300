from cs1graphics import *

w = 1000

paper = Canvas(w, w*0.6, 'lightgray', 'The Zoo')

body = Rectangle(w*0.4, w*0.2)

body.setFillColor('white')
body.move(w*0.5, w*0.4)
body.setBorderWidth(5)
paper.add(body)

head = Circle(w*0.1)
head.setFillColor('brown') 
head.move(w*0.7, w*0.3)
paper.add(head)




