# import turtle
# import random
# import math
# import json
# from border import Border
# from player import Player
# from invader import Invader
#
#
# # User input player name and difficulty level.
# player_name_input = turtle.textinput('Enter player name: ', 'Your name:')
# while True:
#     level_input = turtle.textinput('Choose difficulty',  '(Easy, Normal, Hard):')
#     if level_input.upper() == 'EASY':
#         mode_input = 10
#         break
#     elif level_input.upper() == 'NORMAL':
#         mode_input = 15
#         Player().laser_speed = 80
#         break
#     elif level_input.upper() == 'HARD':
#         mode_input = 20
#         Player().laser_speed = 120
#         break
#     else:
#         print('Please Try again.')
#
# border_obj = Border()
# player_obj = Player()
# invader_obj = Invader()
#
# # Register shapes to turtle.
# turtle.register_shape("player.gif")
# turtle.register_shape("invader.gif")
#
# # Set up screen.
# game = turtle.Screen()
# game.title('Space Invaders')
# game.bgcolor('black')
# game.bgpic('background.gif')
# game.tracer(1)
#
# # Set up border, write game score.
# border_obj.draw()
# border_obj.game_score(player_name_input)
#
# # Set position of player, laser and group of invaders.
# player_obj.set_icon_position()
# player_obj.set_laser_position()
# invader_army = list(invader_obj.set_invaders(mode_input))
#
# # Binding key to control player icon and firing option.
# turtle.listen()
# turtle.onkey(player_obj.move_left, "Left")
# turtle.onkey(player_obj.move_right, "Right")
# turtle.onkey(player_obj.fire, "space")
#
#
# def collision_check(p1, p2):
#     distance = math.sqrt(math.pow(p1.xcor() - p2.xcor(), 2) + math.pow(p1.ycor() - p2.ycor(), 2))
#     if distance < 30:
#         return True
#     else:
#         return False
#
#
# # Main game loop
# while True:
#     game.update()
#     for invader in invader_army:
#         invader_obj.move(invader_army, invader)
#         # Check if collision between laser and invader.
#         if collision_check(player_obj.laser, invader):
#             border_obj.score += 10
#             game_score = "Score: %s" % border_obj.score
#             border_obj.score_pen.clear()
#             border_obj.score_pen.write(game_score, False, align="left", font=("Mono", 14, "bold"))
#             # Reset laser position and status.
#             player_obj.laser.hideturtle()
#             player_obj.laser_status = "ready"
#             player_obj.laser.setposition(player_obj.icon.xcor(), player_obj.icon.ycor())
#             # Reset invader position.
#             x = random.randint(-250, 200)
#             y = random.randint(100, 250)
#             invader.setposition(x, y)
#         # Check if collision between player icon and invader.
#         if collision_check(player_obj.icon, invader):
#             player_obj.icon.hideturtle()
#             invader.hideturtle()
#             # Write save data file as json file
#             save_slot = {
#                 'data_slot': {
#                     'Player name': player_name_input.upper(),
#                     'Difficulty': level_input.upper(),
#                     'Score': border_obj.score
#                 }
#             }
#             with open('leaderboard.json', 'a') as leaderboard_file:
#                 json.dump(save_slot, leaderboard_file, indent=4)
#             game_over = turtle.textinput('Game Over!', 'Press any key to close game.')
#             game.bye()
#             break
#     player_obj.move_laser()
#     player_obj.is_laser_gone()
