from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepPink")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
#
# table.add_column("Common Name", ["Black Bamboo", "Angel Mist Bamboo", "Blue Chungii"])
# table.add_column("Scientific Name", ["Phyllostachys nigra", "Dendrocalamus minor Amoenus", "Bambusa chungii"])
# table.align = "r"
# table.title = "Bamboo"
# print(table)

spike = Turtle()
screen = Screen()
spike.shape("arrow")
screen.colormode(255)
spike.color(116, 95, 217)      #Weird, RGB was supposed to be pencolor() not color()
spike.forward(100)









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