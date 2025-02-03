import tkinter as tk
import math
import time

class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("TronRemake (Tkinter Version)")
        self.geometry("1800x900")
        self.configure(bg="black")

        # Canvas for game rendering
        self.canvas = tk.Canvas(self, width=1600, height=800, bg="black")
        self.canvas.pack()

        # Game state variables
        self.playing = True
        self.cell_size = 20
        self.maze_offset_x = 100  # Offset to center the maze
        self.maze_offset_y = 50
        self.Mauerliste = []
        self.Schatzliste = []

        # Player and Enemy
        self.player = Spieler(self.canvas, "blue", 200, 200, "right")
        self.enemy = Spieler(self.canvas, "red", 400, 400, "left")

        # Label for stats
        self.stats_label = tk.Label(self, text="Player Health: 3 | Gold: 0", fg="white", bg="black", font=("Verdana", 15))
        self.stats_label.pack()

        # Create level
        self.load_level(Level_1)

        # Bind keys for movement
        self.bind("<w>", lambda e: self.player.changeDir("up"))
        self.bind("<a>", lambda e: self.player.changeDir("left"))
        self.bind("<s>", lambda e: self.player.changeDir("down"))
        self.bind("<d>", lambda e: self.player.changeDir("right"))
        self.bind("<Up>", lambda e: self.enemy.changeDir("up"))
        self.bind("<Left>", lambda e: self.enemy.changeDir("left"))
        self.bind("<Down>", lambda e: self.enemy.changeDir("down"))
        self.bind("<Right>", lambda e: self.enemy.changeDir("right"))

        # Start game loop
        self.game_loop()

    def load_level(self, level):
        """Loads the level and creates walls, player, enemy, and treasures."""
        for y, row in enumerate(level):
            for x, cell in enumerate(row):
                screen_x = self.maze_offset_x + (x * self.cell_size)
                screen_y = self.maze_offset_y + (y * self.cell_size)

                if cell == "X":
                    self.Mauerliste.append((screen_x, screen_y))
                    self.canvas.create_rectangle(screen_x, screen_y, screen_x + 20, screen_y + 20, fill="white")

                elif cell == "P":
                    self.player.move(screen_x, screen_y)

                elif cell == "G":
                    self.enemy.move(screen_x, screen_y)

                elif cell == "F":
                    schatz = Schatz(self.canvas, screen_x, screen_y)
                    self.Schatzliste.append(schatz)

    def game_loop(self):
        """Main game loop that moves players, checks collisions, and updates UI."""
        if self.playing:
            self.player.move()
            self.enemy.move()

            # Check for treasure collection
            for schatz in self.Schatzliste[:]:
                if self.player.kollision(schatz):
                    schatz.destroy()
                    self.Schatzliste.remove(schatz)
                elif self.enemy.kollision(schatz):
                    schatz.destroy()
                    self.Schatzliste.remove(schatz)

            # Check for collisions
            if self.player.check_tail_collision():
                print("Player collided with tail. Game Over!")
                self.playing = False
            elif self.enemy.check_tail_collision():
                print("Enemy collided with tail. Game Over!")
                self.playing = False

            # Update stats label
            self.stats_label.config(text=f"Player Health: {self.player.health} | Gold: {self.player.gold}")

            self.after(50, self.game_loop)  # Run loop every 50ms

class Spieler:
    def __init__(self, canvas, color, x, y, direction):
        self.canvas = canvas
        self.color = color
        self.body = canvas.create_rectangle(x, y, x+20, y+20, fill=color)
        self.x = x
        self.y = y
        self.lastDirection = direction
        self.health = 3
        self.gold = 0
        self.tail = []

    def move(self, new_x=None, new_y=None):
        """Moves the player in the current direction."""
        if new_x is not None and new_y is not None:
            self.x, self.y = new_x, new_y
            self.canvas.coords(self.body, new_x, new_y, new_x + 20, new_y + 20)
            return

        # Store previous position
        old_x, old_y = self.x, self.y

        if self.lastDirection == "up":
            self.y -= 20
        elif self.lastDirection == "down":
            self.y += 20
        elif self.lastDirection == "left":
            self.x -= 20
        elif self.lastDirection == "right":
            self.x += 20

        # Check collision with walls
        if (self.x, self.y) not in game.Mauerliste:
            self.canvas.coords(self.body, self.x, self.y, self.x + 20, self.y + 20)
            self.tail.append(Tail(self.canvas, old_x, old_y))

    def changeDir(self, dir):
        self.lastDirection = dir

    def kollision(self, other):
        """Checks if the player collides with another object."""
        return self.x == other.x and self.y == other.y

    def check_tail_collision(self):
        return (self.x, self.y) in [(t.x, t.y) for t in self.tail]

class Tail:
    """Represents the player's trail."""
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.body = canvas.create_rectangle(x, y, x+20, y+20, fill="gray")

class Schatz:
    """Represents a collectible treasure."""
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.body = canvas.create_rectangle(x, y, x+20, y+20, fill="green")

    def destroy(self):
        self.canvas.delete(self.body)

# Level data
Level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XTFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XPFFFFFFFFFFFFFFFFFFFFFFFFFFFFGFX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Start the game
game = Game()
game.mainloop()