from cs1graphics import *
from time import sleep

canvas = Canvas(1000,1000, title="Bees in Spring")
canvas.setBackgroundColor('lightblue')

sun = Circle(200)
sun.setFillColor('yellow')
sun.setBorderColor('yellow')
sun.move(1000, 0)

grass = Ellipse(500, 2000, Point(500,1000))
grass.rotate(90)
grass.setFillColor('green')

beehive = Polygon(Point(500, 360), Point(540, 380), Point(540, 420), 
                  Point(500, 440), Point(460, 420), Point(460, 380))

beehive.setFillColor('goldenrod')
beehive.setBorderColor('saddlebrown')
beehive.setBorderWidth(4)
beehive.move(-250, 60)
beehive.scale(1.25)

# Constructing tree 
tree_trunk = Rectangle(75, 600, Point(500, 500))
tree_trunk.setFillColor('brown')

tree_leaves = Circle(150, Point(500, 300))
tree_leaves.setFillColor('darkgreen')

tree = Layer()
tree.add(tree_trunk)
tree.add(tree_leaves)
tree.move(-300, 0)

# Constructing flowers
flower_center = Circle(25, Point(750, 600))
flower_center.setFillColor('yellow')
flower_center.setBorderColor('pink')

petal1 = Ellipse(150, 40, Point(750, 600))
petal1.setFillColor('red')
petal1.setBorderColor('red')

petal2 = petal1.clone()
petal2.rotate(45)

petal3 = petal2.clone()
petal3.rotate(45)

petal4 = petal3.clone()
petal4.rotate(45)

flower_stem = Rectangle(10, 200, Point(750, 700))
flower_stem.setFillColor('darkgreen')

flower_texture1 = Path(Point(750, 580), Point(770, 590), 
                       Point(750, 600), Point(770, 610), 
                       Point(750, 620))

flower_texture1.setBorderWidth(5)
flower_texture1.setBorderColor("gold")

flower_texture2 = flower_texture1.clone()
flower_texture2.flip()

flower1 = Layer()
flower1.add(flower_stem)
flower1.add(petal1)
flower1.add(petal2)
flower1.add(petal3)
flower1.add(petal4)
flower1.add(flower_center)
flower1.add(flower_texture1)
flower1.add(flower_texture2)

flower2 = flower1.clone()
flower2.scale(0.75)
flower2.move(250, 250)

flower3 = flower1.clone()
flower3.scale(0.85)
flower3.move(250, 120)

# Constructing bee
bee_body = Rectangle(100, 80,  Point(500, 500))
bee_body.setFillColor('gold')

bee_stripe1 = Rectangle(20, 80, Point(460, 500))
bee_stripe1.setFillColor('brown')

bee_stripe2 = Rectangle(10, 80, Point(480, 500))
bee_stripe2.setFillColor('brown')

bee_stripe3 = Rectangle(10, 80, Point(500, 500))
bee_stripe3.setFillColor('brown')

bee_wing = Ellipse(50, 30, Point(480, 450))
bee_wing.rotate(30)
bee_wing.setBorderWidth(3)
bee_wing.setBorderColor('grey')
bee_wing.setFillColor('white')

bee_eye = Rectangle(10, 25, Point(545, 480))
bee_eye.setFillColor('transparent')
bee_eye.setBorderWidth(8)

bee1 = Layer()
bee1.add(bee_body)
bee1.add(bee_stripe1)
bee1.add(bee_stripe2)
bee1.add(bee_stripe3)
bee1.add(bee_eye)
bee1.add(bee_wing)

bee2 = bee1.clone()
bee2.scale(0.9)

buzz = Text("Bzzz!", 30)
buzz.moveTo(800, 450)


backdrop = Layer()
backdrop.add(sun)
backdrop.add(grass)
backdrop.add(flower1)
backdrop.add(flower2)
backdrop.add(flower3)
backdrop.add(tree)
backdrop.add(beehive)

canvas.add(backdrop)

# Animation
sleep(1)
canvas.add(bee1)
sleep(0.75)

i = 0
while i < 7:
    bee1.move(20, 10)
    sleep(0.25)
    i += 1

i = 0
while i < 3:
    bee1.move(20, 0)
    sleep(0.25)
    i += 1

canvas.add(buzz)
sleep(0.75)
canvas.remove(buzz)

i = 0
while i < 15:
    bee1.move(20, 0)
    sleep(0.25)
    i += 1

canvas.remove(bee1)
sleep(0.75)

bee2.move(-200, 100)
canvas.add(bee2)
sleep(0.25)

i = 0
while i < 2:
    bee2.move(20, 10)
    sleep(0.25)
    i += 1

i = 0
while i < 19:
    bee2.move(20, 0)
    sleep(0.25)
    i += 1

canvas.add(buzz)
sleep(0.75)
canvas.remove(buzz)

i = 0
while i < 15:
    bee2.move(20, 0)
    sleep(0.25)
    i += 1

canvas.remove(bee2)










