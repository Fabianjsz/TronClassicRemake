import turtle
import math
import time
from functools import partial

playing = True

Fenster = turtle.Screen()
Fenster.bgcolor("black")
Fenster.title("TronRemake")
Fenster.setup(1800, 900)
#Fenster.addshape("wall.gif")



class Mauer(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Spieler(turtle.Turtle):
    def __init__(self, dir):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.lastDirecton = dir
        self.health = 3
        

    def move(self, lastDirection):
        if lastDirection == "up":
            move_to_x = player.xcor()
            move_to_y = player.ycor()+20
            if (move_to_x, move_to_y) not in Mauerliste:
                self.goto(move_to_x, move_to_y)
            
        if lastDirection == "right":
            move_to_x = player.xcor()+20
            move_to_y = player.ycor()
            if (move_to_x, move_to_y) not in Mauerliste:
                self.goto(move_to_x, move_to_y)

        if lastDirection == "down":
            move_to_x = player.xcor()
            move_to_y = player.ycor()-20
            if (move_to_x, move_to_y) not in Mauerliste:
                self.goto(move_to_x, move_to_y)

        if lastDirection == "left":
            move_to_x = player.xcor()-20
            move_to_y = player.ycor()
            if (move_to_x, move_to_y) not in Mauerliste:
                self.goto(move_to_x, move_to_y)

    def changeDir(self, dir):
        print(dir)
        self.lastDirection = dir

        




    def kollision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2)+(b**2))
        if distance < 10:
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
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
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



Stein = Mauer()
player = Spieler(None)

Mauerliste = []
Start(Levelliste[1])


turtle.listen()
turtle.onkey(player.changeDir("left"), "Left")
turtle.onkey(player.changeDir("right"), "Right")
turtle.onkey(player.changeDir("up"), "Up")
turtle.onkey(player.changeDir("down"), "Down")

Fenster.tracer(0)


while playing:
    player.move(player.lastDirection)
    time.sleep(0.5)
    Anzeige(player.health)
    Fenster.update()
    
Fenster.mainloop()
    


"""
while True:
    for Schatz in Schatzliste:
        if player.kollision(Schatz):
            player.gold = player.gold + Schatz.gold
            print("Player Gold: {}".format(player.gold))
            Schatz.destroy()
            Schatzliste.remove(Schatz)
    Anzeige(player.health)
    Fenster.update()
    

            
#Fenster.mainloop()
"""