import turtle
import math
import time
from functools import partial

playing = True

Fenster = turtle.Screen()
Fenster.bgcolor("black")
Fenster.title("TronRemake")
Fenster.setup(1800, 900)




class Mauer(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Feld(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Tail(turtle.Turtle):
    def __init__(self,x,y, cl):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color(cl)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.past_x=0
        self.past_y=0

    def move(self, new_x, new_y):
        self.goto(new_x, new_y)

class Spieler(turtle.Turtle):
    def __init__(self, dir, color):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color(color)
        self.penup()
        self.speed(0)
        self.lastDirection = dir
        self.health = 3
        self.gold = 0
        self.tail = []

    def getColor(self):
        return self.color
    
    def move(self, color):
        global Tailliste
        current_x = self.xcor()
        current_y = self.ycor()

        if self.lastDirection == "up":
            move_to_x = current_x
            move_to_y = current_y + 20
            if (move_to_x, move_to_y) not in Mauerliste:
                self.goto(move_to_x, move_to_y)

        if self.lastDirection == "right":
            move_to_x = current_x + 20
            move_to_y = current_y
            if (move_to_x, move_to_y) not in Mauerliste:
                self.goto(move_to_x, move_to_y)

        if self.lastDirection == "down":
            move_to_x = current_x
            move_to_y = current_y - 20
            if (move_to_x, move_to_y) not in Mauerliste:
                self.goto(move_to_x, move_to_y)

        if self.lastDirection == "left":
            move_to_x = current_x - 20
            move_to_y = current_y
            if (move_to_x, move_to_y) not in Mauerliste:
                self.goto(move_to_x, move_to_y)
        
        self.tail.append(Tail(current_x, current_y, color))
        temp = current_x, current_y
        Tailliste.append(temp)

    def changeDir(self, dir):
        if self.lastDirection == "right" and dir == "left":
            pass
        elif self.lastDirection == "left" and dir == "right":
            pass
        elif self.lastDirection == "up" and dir == "down":
            pass
        elif self.lastDirection == "down" and dir == "up":
            pass
        else:
            self.lastDirection = dir

    def kollision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2) + (b**2))
        if distance < 5:
            return True
        else:
            return False
        
    def tailKollision(self):
        for temp in Tailliste:
            a = self.xcor() - temp[0]
            b = self.ycor() - temp[1]
            distance = math.sqrt((a**2) + (b**2))
            if distance < 5:
                return True
        return False



    def get_tail_position(self):
        return[(Tailliste[0], Tailliste[1]) for tail in Tailliste]
    
    def check_tail_collision(self):
        if (self.xcor(), self.ycor()) in self.get_tail_position():
            return True
        return False

class Schatz(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.gold = 100

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()






Levelliste = [""]
Level_1 =[
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
"XFFFFPFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFGFFFFFFX",
"XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
"XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
"XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
"XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
"XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
"XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
"XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
"XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
"XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
"XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
"XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]
Levelliste.append(Level_1)



Schatzliste = []
Mauerliste = []
Tailliste = []
Feldliste = []

def Start(n):
    for y in range(len(n)):
        for x in range(len(n[y])):
            character = n[y][x]
            screen_x = -800 + (x * 20)
            screen_y = 400 - (y * 20)

            if character == "X":
                Stein.goto(screen_x, screen_y)
                Stein.stamp()
                Mauerliste.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "G":
                enemy.goto(screen_x, screen_y)

            if character == "F":
                temp = str(screen_x) + ", " + str(screen_y)
                feld.goto(screen_x ,screen_y)
                feld.stamp()
                Schatzliste.append(temp)

Stein = Mauer()
player = Spieler("right", "blue")
enemy = Spieler("left", "red")
feld = Schatz()


Start(Levelliste[1])


antwort = str(input("Drücke Enter um zu starten"))

Gamestart = True



    
    

turtle.listen()
turtle.onkey(partial(player.changeDir, "up"), "w")
turtle.onkey(partial(player.changeDir, "left"), "a")
turtle.onkey(partial(player.changeDir, "down"), "s")
turtle.onkey(partial(player.changeDir, "right"), "d")

turtle.onkey(partial(enemy.changeDir, "left"), "Left")
turtle.onkey(partial(enemy.changeDir, "right"), "Right")
turtle.onkey(partial(enemy.changeDir, "up"), "Up")
turtle.onkey(partial(enemy.changeDir, "down"), "Down")

Fenster.tracer(0)

while playing and Gamestart:
    player.move("darkblue")
    enemy.move("darkred")

    # Überprüfe, ob der Spieler mit einem Schatz kollidiert
    for schatz in Feldliste[:]:
        if player.kollision(schatz):
            schatz.destroy()  # Zerstöre den Schatz
            Schatzliste.remove(schatz)  # Entferne den Schatz aus der Liste
        elif enemy.kollision(schatz):
            schatz.destroy()
            Schatzliste.remove(schatz)
    # In the main loop, checking tail collisions
    for schwanz in Tailliste[:]:
        if player.tailKollision():
            turtle.penup()
            turtle.goto(-100, -450)
            turtle.color("white")
            turtle.write("Rot hat Gewonnen!",font=("Verdana",15, "normal"))
            turtle.hideturtle()
            playing = False
        elif enemy.tailKollision():
            turtle.penup()
            turtle.goto(-100, -250)
            turtle.color("white")
            turtle.write("Blau hat Gewonnen!",font=("Verdana",15, "normal"))
            turtle.hideturtle()
            playing = False

    """
    if player.check_tail_collision():
        print("kollision mit Schwanz. Spiel vorbei")
        playing = False
    elif enemy.check_tail_collision():
        print("kolision mit schwnaz, spiel vorbei")
        playing = False
"""
    time.sleep(0.05)
    Fenster.update()

    

Fenster.mainloop()
