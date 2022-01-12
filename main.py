from turtle import Turtle, Screen
import random
# can use from turtle import * to import all modules, not often used because it is confusing
# can also "import [module] as [alias]", i.e. "import turtle as t" so you can write "spike = t.Turtle()" instead of "spike = turtle.Turtle()"


spike = Turtle()
screen = Screen()
spike.shape("arrow")
screen.colormode(255)
spike.color(116, 95, 217)      #Weird, RGB was supposed to be pencolor() not color()
#draw a square
# for _ in range(4):
#     spike.forward(100)
#     spike.right(90)
#draw a dotted line
# for _ in range(8):
#     spike.forward(10)
#     spike.pu()
#     spike.forward(10)
#     spike.pd()
#draw nested shapes in random colors
# for turn in range(4, 9):
#     angle = 360/turn
#     circle = 0
#     spike.color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
#     while circle < 360:
#         spike.forward(80)
#         spike.right(angle)
#         circle += angle
turns = 0
while turns < 5:
    spike.color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    spike.width(10)
    spike.right(90 * random.randint(0, 5))
    spike.right(360)
    spike.forward(30)








screen.exitonclick()

# class Bamboo:
#
#     def __init__(self, clumping, scientific_name):
#         self.clumping = clumping
#         self.scientific_name = scientific_name
#         self.min_zone = 9
#         self.in_stock = True
#
#     def sold_out(self):
#         self.in_stock = False
#
#
# black_bamboo = Bamboo(False, "Phyllostachys nigra")
# black_bamboo.sold_out()
#
# print(black_bamboo.scientific_name)
# if black_bamboo.in_stock == False:
#     print("Out of stock")


# from prettytable import PrettyTable
# table = PrettyTable()
#
# table.add_column("Common Name", ["Black Bamboo", "Angel Mist Bamboo", "Blue Chungii"])
# table.add_column("Scientific Name", ["Phyllostachys nigra", "Dendrocalamus minor Amoenus", "Bambusa chungii"])
# table.align = "r"
# table.title = "Bamboo"
# print(table)