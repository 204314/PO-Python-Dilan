from tkinter import *
import random

# Spelinstellingen
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 70
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "yellow green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

class Snake:
    # Slang aanmaken
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        
        # Slang startpositie
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
            
        # Slang tekenen
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)
            
class Food:
    # Eten aanmaken
    def __init__(self, snake):
        while True: 
            x = random.randint(0, GAME_WIDTH / SPACE_SIZE-1) * SPACE_SIZE
            y = random.randint(0, GAME_HEIGHT / SPACE_SIZE-1) * SPACE_SIZE
            
            if (x, y) not in snake.coordinates:
                break
        
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE,  fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    # Beweging bepalen
    x, y = snake.coordinates[0]
    
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
        
    # Hoofdpositie updaten
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    #https://www.youtube.com/watch?v=QFvqStqPCRU&t=9s
    
    # Check of slang eten raakt
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food(snake)
    else:
        # Staart verwijderen
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
        
    # Botsing controleren
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)
                 
def change_direction(new_direction):
    # Richting veranderen
    global direction
    
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction
#https://www.youtube.com/watch?v=idZj9NWtqGE
    
def check_collisions(snake):
    # Botsing controleren
    x, y = snake.coordinates[0]
    
    # Botsing met de rand
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    
    # Botsing met zichzelf
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
        
    return False

def game_over():
    # Spel stoppen
    canvas.delete("all")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

    # Opnieuw spelen knop
    restart_button = Button(window, text="Play Again", font=('consolas', 20), command=restart_game)
    restart_button.place(x=GAME_WIDTH/2 - 80, y=GAME_HEIGHT/2 + 110)
    window.restart_button = restart_button
    # https://www.youtube.com/watch?v=x5AHtW9UuVo&t=23s
    
def restart_game():
    # Spel opnieuw starten
    global score, direction, snake, food
    
    if hasattr(window, 'restart_button'):
        window.restart_button.destroy()
        
    canvas.delete("all")
    
    score = 0
    direction = 'down'
    
    label.config(text="Score:{}".format(score))
    
    snake = Snake()
    food = Food(snake)
    
    next_turn(snake, food)
    
# Venster aanmaken
window = Tk()
window.title("Snake game")

score = 0
direction = 'down'

# Score label
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

# Speelveld aanmaken
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Venster centreren
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
#https://www.youtube.com/watch?v=Uq_GxIQWiVM

# Besturing koppelen
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
#https://www.geeksforgeeks.org/how-to-bind-the-enter-key-to-a-tkinter-window/?

# Spel starten
snake = Snake()
food = Food(snake)
next_turn(snake, food)

window.mainloop() 

#https://www.youtube.com/watch?v=lyoyTlltFVU&list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T
