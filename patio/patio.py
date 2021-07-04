import numpy as np
import turtle
import logging

from BrickData import BrickCircle
from draw import DrawBrickCircle, point_up


def get_hypotenusa(co, ca):
    return np.sqrt((co ** 2) + (ca ** 2))


def cosine_law(a, b, c):
    num = (a ** 2) + (b ** 2) - (c ** 2)
    den = 2 * a * b
    return np.rad2deg(np.arccos(num / den))


def polygon_radius(length, number):
    return length / (2 * np.tan(np.pi / number))


def circle_is_larger(a, b, radius_margin=50):
    logger = logging.getLogger(__name__)
    logger.debug(f'radius : {a.radius:.02f} > {b.radius:.02f} + {radius_margin}')
    logger.debug(f'sides  : {a.sides} > {b.sides}')
    if (a.radius > b.radius + radius_margin) and (a.sides > b.sides):
        return True
    else:
        return False


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()

    # SETUP SCREEN
    screen = turtle.Screen()
    screen.setup(width=1000, height=1000)

    screen.tracer(0)

    # SETUP CANVAS SIZE
    canvas_side = 6000
    turtle.screensize(canvas_side, canvas_side)
    turtle.setworldcoordinates(- canvas_side / 2, - canvas_side / 2, canvas_side / 2, canvas_side / 2)

    # FIND BRICK CIRCLES
    brick_width = 110
    brick_height = 210

    brick_total = 0
    first_circle = BrickCircle(radius=0, sector=0, sides=0, brick=(brick_width, brick_height))
    last_circle = BrickCircle(radius=0, sector=0, sides=0, brick=(brick_width, brick_height))
    for n in range(18, 72):
        radius = polygon_radius(brick_height, number=n)

        elem = BrickCircle(
            radius=radius,
            sector=360 / n,
            sides=n,
            brick=(brick_width, brick_height)
        )

        if circle_is_larger(elem, last_circle, radius_margin=50 + brick_width):
            logger.info(f'radius {elem.radius:>6.1f} | '
                        f'sector: {elem.sector:>6.1f} | '
                        f'sides: {elem.sides:>6.1f} | '
                        f'brick: {elem.brick}')
            point_up()
            draw = DrawBrickCircle(elem)
            draw.move_to_radius()
            draw.draw_sides()

            if last_circle.radius == 0:
                first_circle = elem

            last_circle = elem
            brick_total += n

    print(f'Total number of bricks: {brick_total}')
    print(f'Inner diameter: {first_circle.radius:.02f}')
    print(f'Outer diameter: {last_circle.radius + 2 * brick_width:.02f}')

    # UPDATE SCREEN
    turtle.hideturtle()
    screen.update()
    screen.mainloop()


if __name__ == '__main__':
    main()
