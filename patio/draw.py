import turtle

from BrickData import BrickCircle


class DrawBrickCircle:
    def __init__(self, data: BrickCircle):
        self.radius = data.radius
        self.sector = data.sector
        self.sides = int(data.sides)
        self.brick_width = data.brick[0]
        self.brick_heigth = data.brick[1]

    def move_to_radius(self):
        turtle.penup()
        turtle.goto(0, self.radius)
        turtle.pendown()

    def draw_brick(self):
        turtle.forward(distance=self.brick_heigth)
        turtle.left(angle=90)
        turtle.forward(distance=self.brick_width)
        turtle.left(angle=90)
        turtle.forward(distance=self.brick_heigth)
        turtle.left(angle=90)
        turtle.forward(distance=self.brick_width)
        turtle.left(angle=90)

    def draw_sides(self):
        for _ in range(self.sides):
            self.draw_brick()
            turtle.forward(distance=self.brick_heigth)
            turtle.right(angle=self.sector)


def point_up():
    turtle.setheading(0)


if __name__ == '__main__':
    point_up()

    t = DrawBrickCircle(BrickCircle(radius=55, sector=20, sides=int(360 / 20), brick=(10, 20)))
    t.move_to_radius()
    t.draw_sides()

    point_up()

    t = DrawBrickCircle(BrickCircle(radius=110, sector=10, sides=int(360 / 10), brick=(10, 20)))
    t.move_to_radius()
    t.draw_sides()
