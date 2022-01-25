import turtle


class Border:
    def __init__(self):
        """Initialization of the Border class with 5 attributes."""
        self.color = 'white'
        self.ign = turtle.Turtle()
        self.score = 0
        self.score_pen = turtle.Turtle()
        self.border_pen = turtle.Turtle()

    def draw(self):
        """Draw the white frame called border."""
        self.border_pen.penup()
        self.border_pen.speed(0)
        self.border_pen.color(self.color)
        self.border_pen.setposition(-300, -300)
        self.border_pen.pendown()
        self.border_pen.pensize(3)
        for side in range(4):
            self.border_pen.fd(600)
            self.border_pen.lt(90)
        self.border_pen.hideturtle()

    def game_score(self, player_name):
        """Write initialize game score and player name."""
        player_name = f'Player Name: {player_name}'
        game_score = 'Score: %s' % self.score
        self.ign.penup()
        self.score_pen.penup()
        self.ign.speed(0)
        self.score_pen.speed(0)
        self.ign.color(self.color)
        self.score_pen.color(self.color)
        self.ign.setposition(290, 273)
        self.score_pen.setposition(-290, 273)
        self.ign.write(player_name, False, align='right', font=('Mono', 14, 'bold'))
        self.score_pen.write(game_score, False, align='left', font=('Mono', 14, 'bold'))
        self.ign.hideturtle()
        self.score_pen.hideturtle()
