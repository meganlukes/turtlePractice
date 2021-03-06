from turtle import Turtle, Screen
import random
import colorgram
# can use from turtle import * to import all modules, not often used because it is confusing
# can also "import [module] as [alias]", i.e. "import turtle as t" so you can write "spike = t.Turtle()" instead of "spike = turtle.Turtle()"


# spike = Turtle()
# spike.penup()
screen = Screen()
colors = ["pink", "purple", "blue", "green", "brown"]
all_turtles = []
# spike.shape("turtle")
# screen.colormode(255)
# spike.color("pink")      #Weird, RGB was supposed to be pencolor() not color()

#Turtle Race
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your pick", prompt="Which turtle will win the race? Pick a color: ")
for number in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[number])
    new_turtle.penup()
    new_turtle.goto(x=-225, y=((50 * number) - 100))
    all_turtles.append(new_turtle)

is_race_on = False
if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 200:
            is_race_on = False
            print(f"{turtle.pencolor()} is the winner!")
            if user_choice.lower() == turtle.pencolor():
                print("You won :D")
            else:
                print("You lost :(")
# spike.goto(x=-225, y=-100)

screen.exitonclick()

#etch-a-sketch game
# def move_forwards():
#     spike.forward(10)
# def move_backwards():
#     spike.backward(10)
# def move_counterclockwise():
#     spike.left(10)
# def move_clockwise():
#     spike.right(10)
# def clear_drawing():
#     spike.clear()
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=move_counterclockwise)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="c", fun=clear_drawing)
# screen.exitonclick()

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
#draw random path
# turns = 0
# while turns < 5:
#     spike.color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
#     spike.width(10)
#     spike.right(90 * random.randint(0, 5))
#     spike.right(360)
#     spike.forward(30)

#draw spirograph
# for num in range(15):
#     spike.color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
#     spike.setheading(num * 24)
#     spike.circle(50)

#Make a hirst painting
#Extract colors
# colors = colorgram.extract('hirst.jpg', 10)
# color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85)]

#draw 10 x 10 rows of dots
# spike.pu()
# spike.sety(-300)
# for dot in range(10):
#     spike.setx(-300)
#     for num in range(10):
#         spike.dot(20, color_list[random.randint(0, 9)])
#         spike.fd(50)
#     spike.sety((50 * (dot + 1)) - 300)
# screen.exitonclick()

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