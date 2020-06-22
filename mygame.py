import turtle
import time
import random

delay = 0.1

#we have to set up the screen
a = turtle.Screen()
a.title("snake game by SRAVAN")
a.bgcolor("black")
a.setup(width=600,height=600)
a.tracer(0) #it will stop the screen update

#we have to create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#we have to create food for snake 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#fuctions to move the snake head
def go_up():
    head.direction = "up"
    
def go_down():
    head.direction = "down"
    
def go_left():
    head.direction = "left"
    
def go_right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#controls to move snake head
a.listen()
a.onkeypress(go_up,"w")
a.onkeypress(go_down,"s")
a.onkeypress(go_left,"a")
a.onkeypress(go_right,"d")

#it is the main loop
while True:
    a.update() #it will update the screen
    
    #it will stop the game if snake head touch the ends of the screen 
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
    
    if head.distance(food) < 20:
        x = random.randint(-290 , 290)
        y = random.randint(-290 , 290)
        food.goto(x , y)
        
        b = turtle.Turtle()
        b.shape("square")
        b.color("white")
        b.penup()
        segments.append(b)
        
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x , y)
    
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x , y)
        
    
    move()
    
    time.sleep(delay)
    
a.mainloop()
