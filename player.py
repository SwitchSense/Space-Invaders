# import turtle
#
#
# class Player:
#     def __init__(self):
#         """Initialization of the Player class with 7 attributes."""
#         self.icon = turtle.Turtle()
#         self.icon_speed = 25
#         self.icon_color = 'light blue'
#         self.laser = turtle.Turtle()
#         self.laser_speed = 40
#         self.laser_color = 'orange'
#         self.laser_status = 'ready'
#
#     def set_icon_position(self):
#         """Set initialize position of player icon and set appearance of the player."""
#         self.icon.shape('player.gif')
#         self.icon.penup()
#         self.icon.color(self.icon_color)
#         self.icon.speed(0)
#         self.icon.setposition(0, -250)
#         self.icon.setheading(90)
#
#     def set_laser_position(self):
#         """Set initialize position of laser icon and set appearance of the laser"""
#         self.laser.shape('square')
#         self.laser.shapesize(0.12, 0.4)
#         self.laser.penup()
#         self.laser.color(self.laser_color)
#         self.laser.hideturtle()
#         self.laser.speed(0)
#         self.laser.setheading(90)
#         self.laser.setposition(self.icon.xcor(), self.icon.ycor())
#
#     def move_left(self):
#         """Move player icon to the left."""
#         x_cor = self.icon.xcor()
#         if x_cor > -275:
#             x_cor -= self.icon_speed
#         self.icon.setx(x_cor)
#
#     def move_right(self):
#         """Move player icon to the right."""
#         x_cor = self.icon.xcor()
#         if x_cor < 275:
#             x_cor += self.icon_speed
#         self.icon.setx(x_cor)
#
#     def fire(self):
#         """Show the laser when fire laser."""
#         if self.laser_status == 'ready':
#             self.laser.hideturtle()
#             self.laser_status = 'fire'
#             self.laser.setposition(self.icon.xcor(), self.icon.ycor() + 10)
#             self.laser.showturtle()
#
#     def move_laser(self):
#         """Move the laser when started firing."""
#         if self.laser_status == 'fire':
#             y = self.laser.ycor()
#             y += self.laser_speed
#             self.laser.sety(y)
#
#     def is_laser_gone(self):
#         """Check if laser gone of the border. If gone, ready to fire next laser."""
#         if self.laser.ycor() > 275:
#             self.laser.hideturtle()
#             self.laser_status = 'ready'
