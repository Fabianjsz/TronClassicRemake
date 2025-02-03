import turtle
import math
import time

#

Fenster = turtle.Screen()
Fenster.bgcolor("black")
Fenster.title("Labyrinth")
Fenster.setup(1800, 900)



class Mauer(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.penup()
        self.speed(0)


# Relevant
class Essen(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Tail(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.past_x=0
        self.past_y=0

class Spieler(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.penup()
        self.speed(0)
        self.gold = 0
        self.hp = 100
        self.past_x=0
        self.past_y=0
        self.status = "alive"
        self.restart = False

    def go_up(self):
        self.past_x = player.xcor()
        self.past_y = player.ycor()
        move_to_x = player.xcor()
        move_to_y = player.ycor()+20
        self.face=0
        k=0
        if (move_to_x, move_to_y) not in Mauerliste and player.status == "alive" :
            self.goto(move_to_x, move_to_y)
            for Frucht in Essenliste:
                if player.kollision(Frucht):
                    k = 1
                    if len(Tailliste) == 0:
                        Teil=Tail(player.past_x,player.past_y)
                        Tailliste.append(Teil)
                        Frucht.destroy()
                        Essenliste.remove(Frucht)
                    else:
                        i = len(Tailliste)
                        Teil = Tail(Tailliste[i-1].past_x,Tailliste[i-1].past_y)
                        Tailliste.append(Teil)
                        Frucht.destroy()
                        Essenliste.remove(Frucht)
            if len(Tailliste) > 0:
                    Tailliste[0].past_x = Tailliste[0].xcor()
                    Tailliste[0].past_y = Tailliste[0].ycor()
                    x = self.past_x
                    y = self.past_y
                    Tailliste[0].goto(x, y)
                    for i in range(len(Tailliste)-1):
                        Tailliste[i+1].past_x = Tailliste[i+1].xcor()
                        Tailliste[i+1].past_y = Tailliste[i+1].ycor()
                        x = Tailliste[i].past_x
                        y = Tailliste[i].past_y
                        Tailliste[i+1].goto(x, y)
                    

                
    def go_down(self):
        self.past_x = player.xcor()
        self.past_y = player.ycor()
        move_to_x = player.xcor()
        move_to_y = player.ycor()-20
        self.face=180
        k=0
        if (move_to_x, move_to_y) not in Mauerliste and player.status == "alive" :
            self.goto(move_to_x, move_to_y)
            for Frucht in Essenliste:
                if player.kollision(Frucht):
                    k = 1
                    if len(Tailliste) == 0:
                        Teil=Tail(player.past_x,player.past_y)
                        Tailliste.append(Teil)
                        Frucht.destroy()
                        Essenliste.remove(Frucht)
                    else:
                        i = len(Tailliste)
                        Teil = Tail(Tailliste[i-1].past_x,Tailliste[i-1].past_y)
                        Tailliste.append(Teil)
                        Frucht.destroy()
                        Essenliste.remove(Frucht)
                    
            if len(Tailliste) > 0:
                    Tailliste[0].past_x = Tailliste[0].xcor()
                    Tailliste[0].past_y = Tailliste[0].ycor()
                    x = self.past_x
                    y = self.past_y
                    Tailliste[0].goto(x, y)
                    for i in range(len(Tailliste)-1):
                        Tailliste[i+1].past_x = Tailliste[i+1].xcor()
                        Tailliste[i+1].past_y = Tailliste[i+1].ycor()
                        x = Tailliste[i].past_x
                        y = Tailliste[i].past_y
                        Tailliste[i+1].goto(x, y)
                
    def go_right(self):
        self.past_x = player.xcor()
        self.past_y = player.ycor()
        move_to_x = player.xcor()+20
        move_to_y = player.ycor()
        self.face=90
        k=0
        if (move_to_x, move_to_y) not in Mauerliste and player.status == "alive" :
            self.goto(move_to_x, move_to_y)
            for Frucht in Essenliste:
                if player.kollision(Frucht):
                    k = 1
                    if len(Tailliste) == 0:
                        Teil=Tail(player.past_x,player.past_y)
                        Tailliste.append(Teil)
                        Frucht.destroy()
                        Essenliste.remove(Frucht)
                    else:
                        i = len(Tailliste)
                        Teil = Tail(Tailliste[i-1].past_x,Tailliste[i-1].past_y)
                        Tailliste.append(Teil)
                        Frucht.destroy()
                        Essenliste.remove(Frucht)
                    
            if len(Tailliste) > 0:
                    Tailliste[0].past_x = Tailliste[0].xcor()
                    Tailliste[0].past_y = Tailliste[0].ycor()
                    x = self.past_x
                    y = self.past_y
                    Tailliste[0].goto(x, y)
                    for i in range(len(Tailliste)-1):
                        Tailliste[i+1].past_x = Tailliste[i+1].xcor()
                        Tailliste[i+1].past_y = Tailliste[i+1].ycor()
                        x = Tailliste[i].past_x
                        y = Tailliste[i].past_y
                        Tailliste[i+1].goto(x, y)
                
    def go_left(self):
        self.past_x = player.xcor()
        self.past_y = player.ycor()
        move_to_x = player.xcor()-20
        move_to_y = player.ycor()
        self.face=270
        k=0
        if (move_to_x, move_to_y) not in Mauerliste and player.status == "alive" :
            self.goto(move_to_x, move_to_y)
            for Frucht in Essenliste:
                if player.kollision(Frucht):
                    k = 1
                    if len(Tailliste) == 0:
                        Teil=Tail(player.past_x,player.past_y)
                        Tailliste.append(Teil)
                        Frucht.destroy()
                        Essenliste.remove(Frucht)
                    else:
                        i = len(Tailliste)
                        Teil = Tail(Tailliste[i-1].past_x,Tailliste[i-1].past_y)
                        Tailliste.append(Teil)
                        Frucht.destroy()
                        Essenliste.remove(Frucht)
                    
            if len(Tailliste) > 0:
                    Tailliste[0].past_x = Tailliste[0].xcor()
                    Tailliste[0].past_y = Tailliste[0].ycor()
                    x = self.past_x
                    y = self.past_y
                    Tailliste[0].goto(x, y)
                    for i in range(len(Tailliste)-1):
                        Tailliste[i+1].past_x = Tailliste[i+1].xcor()
                        Tailliste[i+1].past_y = Tailliste[i+1].ycor()
                        x = Tailliste[i].past_x
                        y = Tailliste[i].past_y
                        Tailliste[i+1].goto(x, y)
                

        
    def kollision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2)+(b**2))
        if distance < 5:
            return True
        else:
            return False

# Weitere Formen in Turtle: arrow, circle, classic, square, triangle, turtle.
# Was macht left(90)?
class Schatz(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("gold.gif")
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
    turtle.write(str(x), font=("Verdana",15, "normal"))
    turtle.hideturtle()

def Anzeige2(x):
    turtle.penup()
    turtle.goto(-290, 330)
    turtle.pendown()
    turtle.color("white")
    turtle.write(str(x), font=("Verdana",15, "normal"))
    turtle.hideturtle()
def Inv():
    turtle.penup()
    turtle.goto(350, 200)
    turtle.color("white")
    turtle.write("Inventory", font=("Verdana",15, "normal"))
    turtle.hideturtle()

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

Levelliste.append(Level_1)
Schatzliste = []
Mauerliste = []
Keyliste = []
Emenyliste = []
Doorliste = []
Lanzeliste = []
SBliste = []
Fliste = []
Tailliste = []
Essenliste = []
def Start(n):
    for y in range(len(n)):
        for x in range(len(n[y])):
            character = n[y][x]
            screen_x = -288 + (x*20)
            screen_y = 288 - (y*20)

            #Steine
            if character == "X":
                Stein.goto(screen_x, screen_y)
                Stein.stamp()
                Mauerliste.append((screen_x, screen_y))
            #Essen
            if character == "F":
                Frucht = Essen(screen_x, screen_y)
                Essenliste.append(Frucht)
            #Spieler
            if character == "P":
                player.goto(screen_x, screen_y)



Stein = Mauer()
player = Spieler()
L1 = True

Start(Levelliste[1])
def restart():
    player.restart = True

turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")
turtle.onkey(restart, "Return")
Fenster.tracer(0)

while L1 == True:
#asdddaaaaaaaaaa#############################################################


    for n in Tailliste:
        if player.kollision(n):
            player.status="dead"
    if player.restart:
        turtle.clearscreen()
        with open("Lab (part3).py") as file:
            exec(file.read())
    if player.status == "alive":
        Anzeige("Gold: "+ str(player.gold))
        Anzeige2("Hp: "+ str(player.hp))
        Inv()
    else:
        Anzeige("Dead")
        Anzeige2("Press Enter to restart")
    Fenster.update()
    if len(Essenliste) == 0:
        turtle.clearscreen()
Fenster.mainloop()
