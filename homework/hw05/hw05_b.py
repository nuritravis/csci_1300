from cs1graphics import *

paper = Canvas(500, 300, 'lightgray', 'The Zoo')

body = Rectangle(200, 100)
body.setFillColor('white')
body.move(250, 200)
body.setBorderWidth(5)
body.setDepth(1)

head = Circle(50)
head.setFillColor('brown')
head.move(350, 150)
head.setDepth(0)


image = Layer()
image.add(head)
image.add(body)
image.move(-75, 150)
image.rotate(-30)
paper.add(image)