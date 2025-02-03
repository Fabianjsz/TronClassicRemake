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
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("darkblue")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.past_x = 0
        self.past_y = 0

    def move(self, new_x, new_y):
        self.goto(new_x, new_y)

class Spieler(turtle.Turtle):
    def __init__(self, dir="right"):  # Standardmäßig nach "right" setzen
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.lastDirection = dir
        self.health = 3
        self.gold = 0
        self.tail = []  # Liste für den Schwanz

    def move(self):
        # Speicher die aktuelle Position des Spielers
        current_x = self.xcor()
        current_y = self.ycor()

        # Bewege den Spieler basierend auf der letzten Richtung
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

        # Fügt einen neuen Tail hinzu, der die alte Position des Spielers ist
        self.tail.append(Tail(current_x, current_y))

    def changeDir(self, dir):
        self.lastDirection = dir

    def kollision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2) + (b**2))
        if distance < 5:
            return True
        else:
            return False

    def get_tail_positions(self):
        """Gibt eine Liste der Positionen des Schwanzes zurück."""
        return [(tail.xcor(), tail.ycor()) for tail in self.tail]

    def check_tail_collision(self):
        """Überprüft, ob der Spieler mit seinem eigenen Schwanz kollidiert."""
        if (self.xcor(), self.ycor()) in self.get_tail_positions():
            return True
        return False

class Schatz(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

def Anzeige(health, gold):
    turtle.clear()
    turtle.penup()
    turtle.goto(-290, 300)
    turtle.pendown()
    turtle.color("white")

Levelliste = [""]
Level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XTFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XTFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XPFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
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

            if character == "T":
                feld.goto(screen_x, screen_y)
                feld.stamp()
                Feldliste.append((screen_x, screen_y))

            if character == "F":
                Schatzliste.append(Schatz(screen_x, screen_y))

Stein = Mauer()
player = Spieler("right")  # Stelle sicher, dass der Spieler mit der Richtung "right" startet.
feld = Feld()

Start(Levelliste[1])

# Sofortige Bewegung des Spielers nach rechts
player.move()  # Automatische Bewegung nach rechts, nachdem das Spielfeld geladen wurde

turtle.listen()
turtle.onkey(partial(player.changeDir, "left"), "Left")
turtle.onkey(partial(player.changeDir, "right"), "Right")
turtle.onkey(partial(player.changeDir, "up"), "Up")
turtle.onkey(partial(player.changeDir, "down"), "Down")

Fenster.tracer(0)

while playing:
    player.move()

    # Überprüfe, ob der Spieler mit einem Schatz kollidiert
    for schatz in Schatzliste[:]:
        if player.kollision(schatz):
            schatz.destroy()  # Zerstöre den Schatz
            Schatzliste.remove(schatz)  # Entferne den Schatz aus der Liste
            player.gold += 1  # Erhöhe das Gold, was auch die Schwanzlänge bestimmt

    if player.check_tail_collision():
        print("Kollision mit dem eigenen Schwanz! Spiel vorbei!")
        playing = False  # Beende das Spiel bei Kollision mit dem eigenen Schwanz

    time.sleep(0.05)
    Anzeige(player.health, player.gold)  # Zeige Health und Gold des Spielers an
    Fenster.update()

Fenster.mainloop()