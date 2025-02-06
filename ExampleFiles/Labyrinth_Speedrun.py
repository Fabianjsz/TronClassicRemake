import time
import turtle
import math

Fenster = turtle.Screen()
Fenster.bgcolor("black")
Fenster.title("Labyrinth")
Fenster.setup(700, 700)

print("beende alle sechs level so schnell wie möglich!")
print("Deine Endzeit wird dir am Ende im Terminal ausgegeben.")
print("Viel Erfolg")
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
        self.gold = 0

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        if (move_to_x, move_to_y) not in Mauerliste:
            self.goto(move_to_x, move_to_y)
    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        if (move_to_x, move_to_y) not in Mauerliste:
            self.goto(move_to_x, move_to_y)
    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        if (move_to_x, move_to_y) not in Mauerliste:
            self.goto(move_to_x, move_to_y)
    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        if (move_to_x, move_to_y) not in Mauerliste:
            self.goto(move_to_x, move_to_y)

    def kollision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        return distance < 5

class Schatz(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

def Anzeige(x):
    turtle.clear()
    turtle.penup()
    turtle.goto(-290, 300)
    turtle.pendown()
    turtle.color("white")
    turtle.write("Player: " + str(x), font=("Verdana", 15, "normal"))

Levelliste = [""]

Level_1 = [
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

Level_2 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  T XXXXXXXXXXXXXXXXXXX",
"X     XXXXXXXXXXXXXXXXXXX",
"XXXXX   XXXXXXXXXXXXXXXXX",
"XXXXX   XXXXXXXXXXXXXXXXX",
"XXXXX T XXXXXXXXXXXXXXXXX",
"XXXXX   XXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

Level_3 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXX      T     T     XX",
"XXXXXX XXXXXXXXXXXXXXX XX",
"XXXXXX XX T   XXXXXXTX XX",
"XXXXXX XXXXXX        X XX",
"XXXXXX        XXXXXXXX XX",
"XXXXXXXXXXXXXXXXXXXXXX XX",
"XXXXXX P        T      XX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]
Level_4 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXX",
"X   T                 XXX",
"XXXXXXXXXXXXXXXXXXXXX XXX",
"XXXXXXXXXXXXXXXXXXXXX XXX",
"XXXXXXXXXXXXXX        XXX",
"XXXXXXXXXXXXXX XXXXXXXXXX",
"XXXXXXXXXXXXX  XXXXXXXXXX",
"XXXXXXXXXXXX  XXXXXXXXXXX",
"XXXXXXXXXXXX XXXXXXXXXXXX",
"XXXXXXXXXXXX XXXXXXXXXXXX",
"XXXXXXXXXXX TXXXXXXXXXXXX",
"XXXXXXXXXXX   XXXXXXXXXXX",
"X     T       XXXXXXXXXXX",
"X   XXXXXXXX  XXXXXXXXXXX",
"XX XX     XX  XXXXXXXXXXX",
"XX XX XXX  XX  XXXXXXXXXX",
"XX    XXXX XX  XXXXXXXXXX",
"XXXXXX     XXT XXXXXXXXXX",
"XXX    XXXXXX  XXXXXXXXXX",
"XXXTXXXX       XXXXXXXXXX",
"XXXXXXXXXXXXX  XXXXXXXXXX",
"XXXXXXXXXXXXXX      TXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

Level_5 = [
"XXXXXTTTTTTTTTXXXXXXXXXXX",
"XPTTTTXXXXXXXTXXXXXXXXXXX",
"XTTTTTXXXXXXTTTTTXXXXXXXX",
"XXXXXTTTTTTTTTTTTTXXXXXXX",
"XXXXXTTTXXXXTTTTTXXXXXXXX",
"XXXXXTTTXXXXTTTTTXXXXXXXX",
"XXXXXTTTTTTTTTTTTXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

Level_6 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXT                  X",
"X  XXXXXXXXX   XXXXXXXX X",
"X   T                 X X",
"XXXXXXXXXXXXXXXXXXXXX XTX",
"XXX       TXXXXX       XX",
"XXX XXXXXXXXXX   XXXXXXXX",
"XXX XXXXXXXXXX XX   T   X",
"XXX XXXXXXXXX  XX XXXXX X",
"XXX XXXXXXXX  XXX    XX X",
"XXX XXXXXXXX XXXXXXX XX X",
"XXX XXXXXXXX XXXXXX  XX X",
"XXX         TXXXXXX XT  X",
"XXXXXXXXXXX   XXXXX  XXXX",
"X     T       XXXXXX XXXX",
"X   XXXXXXXX  XTTTTTTTTTX",
"XX XX     XX  XXX     TXX",
"XX XX XXX  XX  XXTTTTTTXX",
"XX    XXXXTXX  XXXXTTXXXX",
"XXXXXXXXXXXXXT XXXXTTXXXX",
"XXX    XXXXXX  XXXXTTXXXX",
"XXX XX         XXXX  XXXX",
"XXX  XXXXXXXX       XXXXX",
"XXXX       TXX      TXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

alle_schaetze = []
Levelliste.extend([Level_1, Level_2, Level_3, Level_4, Level_5, Level_6])

alle_schätze = []

def Start(n):
    global alle_schaetze, Mauerliste
    alle_schaetze = []
    Mauerliste = []
    Stein.clearstamps()
    for y in range(len(n)):
        for x in range(len(n[y])):
            character = n[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Steine
            if character == "X":
                Stein.goto(screen_x, screen_y)
                Stein.stamp()
                Mauerliste.append((screen_x, screen_y))

            # Spieler
            if character == "P":
                player.goto(screen_x, screen_y)

            # Beute
            if character == "T":
                alle_schätze.append(Schatz(screen_x, screen_y))

def Naechstes_Level():
    global aktuelles_level
    aktuelles_level += 1
    if aktuelles_level < len(Levelliste):
        Start(Levelliste[aktuelles_level])
    else:
        endzeit = time.time()
        dauer = endzeit - aktuellezeit
        print("Du hast " + str(dauer) + " sekunden gebraucht um alle level zu schaffen")
        print("Herzlichen Glückwunsch! Du hast alle Level abgeschlossen!")
        Fenster.bye()

Stein = Mauer()
player = Spieler()

Mauerliste = []
aktuelles_level = 1
Start(Levelliste[aktuelles_level])

aktuellezeit = time.time()
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

Fenster.tracer(0)

while True:
    for schatz in alle_schätze:
        if player.kollision(schatz):
            player.gold += schatz.gold
            print("Player Gold: {}".format(player.gold))
            schatz.destroy()
            alle_schätze.remove(schatz)

    if not alle_schätze:
        Naechstes_Level()

    Anzeige(player.gold)
    Fenster.update()