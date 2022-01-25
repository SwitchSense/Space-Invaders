import turtle
import random


class Invader:
    def __init__(self):
        """Initialization of the Invader class with 2 attributes."""
        self.icon_speed = 2
        self.color = 'red'

    def set_invaders(self, mode_input):
        """
        Set initialize position of invader icons and set appearance of the invaders.
        :param mode_input
        :type mode_input: int
        """
        invaders = []
        for i in range(mode_input):
            invaders.append(turtle.Turtle())
        for invader in invaders:
            invader.shape('invader.gif')
            invader.color(self.color)
            invader.penup()
            invader.speed(0)
            x = random.randint(-250, 200)
            y = random.randint(100, 250)
            invader.setposition(x, y)
        return invaders

    def move(self, invader_army, invader):
        """
        Move the group of invaders to left, right and downward to player.
        :param invader_army
        :type invader_army: list
        :param invader
        :type invader: turtle.Turtle()
        """
        x = invader.xcor()
        x += self.icon_speed
        invader.setx(x)
        if invader.xcor() > 280:
            for i in invader_army:
                y = i.ycor()
                y -= 40
                i.sety(y)
            self.icon_speed *= -1
        if invader.xcor() < -280:
            for i in invader_army:
                y = i.ycor()
                y -= 40
                i.sety(y)
            self.icon_speed *= -1
