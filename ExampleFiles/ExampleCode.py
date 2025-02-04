import turtle
import math

Fenster = turtle.Screen()
Fenster.bgcolor("black")
Fenster.title("Labyrinth")
Fenster.setup(700, 700)

class Mauer(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Spieler(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold=0

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor()+24
        if (move_to_x, move_to_y) not in Mauerliste:
            self.goto(move_to_x, move_to_y)
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor()-24
        if (move_to_x, move_to_y) not in Mauerliste:
            self.goto(move_to_x, move_to_y)
    def go_right(self):
        move_to_x = player.xcor()+24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in Mauerliste:
            self.goto(move_to_x, move_to_y)
    def go_left(self):
        move_to_x = player.xcor()-24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in Mauerliste:
            self.goto(move_to_x, move_to_y)

    def kollision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2)+(b**2))
        if distance < 5:
            return True
        else:
            return False


class Schatz(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()


def Anzeige(x):
    turtle.clear()
    turtle.penup()
    turtle.goto(-290, 300)
    turtle.pendown()
    turtle.color("white")
    turtle.write("Player: " + str(x), font=("Verdana",15, "normal"))
    


Levelliste = [""]

Level_1 =[
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXX",
"X   T   XXXXXXXXXXXXXXXXX",
"XXXXXX  XXXXXXXXXXXXXXXXX",
"XXXXXX  XXXXXXXXXXXXXXXXX",
"XXXXXX     XXXXXXXXXXXXXX",
"XXXXXXXXX  XXXXXXXXXXXXXX",
"XXXXXXXXX  XXXXXXXXXXXXXX",
"XXXXXXXXX  XXXXXXXXXXXXXX",
"XXXXXXXXX    XXXXXXXXXXXX",
"XXXXXXXXXXX     T XXXXXXX",
"XXXXXXXXXXX  XXXXXXXXXXXX",
"XXXXXXXXXXX   XXXXXXXXXXX",
"XXXXXXX       XXXXXXXXXXX",
"XXXXXXXXXXXX  XXXXXXXXXXX",
"XXXXXXXXXXXX  XXXXXXXXXXX",
"XXXXXXXXXXXXX  XXXXXXXXXX",
"XXXXXXXXXXXXX  XXXXXXXXXX",
"XXXXXXXXXXXXX  XXXXXXXXXX",
"XXXXXXXXXXXXX  XXXXXXXXXX",
"XXXXXXXX       XXXXXXXXXX",
"XXXXXXXXXXXXX  XXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

Schatzliste = []

Levelliste.append(Level_1)

def Start(n):
    for y in range(len(n)):
        for x in range(len(n[y])):
            character = n[y][x]
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)

            #Steine
            if character == "X":
                Stein.goto(screen_x, screen_y)
                Stein.stamp()
                Mauerliste.append((screen_x, screen_y))

            #Spieler
            if character == "P":
                player.goto(screen_x, screen_y)

            #Beute
            if character == "T":
                Schatzliste.append(Schatz(screen_x, screen_y))



Stein = Mauer()
player = Spieler()

Mauerliste = []
Start(Levelliste[1])


turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

Fenster.tracer(0)

while True:
    for Schatz in Schatzliste:
        if player.kollision(Schatz):
            player.gold = player.gold + Schatz.gold
            print("Player Gold: {}".format(player.gold))
            Schatz.destroy()
            Schatzliste.remove(Schatz)
    Anzeige(player.gold)
    Fenster.update()
    
            
Fenster.mainloop()
