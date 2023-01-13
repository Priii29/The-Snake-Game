from turtle import*
from time import sleep
from random import randint



tracer(0)

title("Mister Maker's Snake Game")
setup(width=700, height=600)

colormode(255)
bgcolor(0,0,0)
hideturtle()

player1 = Turtle()
player1.speed(0)
player1.shape("circle")
player1.pu()
player1.seth(90)
player1.goto(0,0)
player1.showturtle()

player2 = Turtle()
player2.speed(0)
player2.shape("circle")
player2.pu()
player2.seth(90)
player2.goto(0,0)
player2.showturtle()

food=Turtle()
food.hideturtle()
food.shape("triangle")
food.pu()
food.color(randint(1,254),randint(1,254),randint(1,254))
food.goto(100,100)
food.showturtle()
food.speed(0)

food2=Turtle()
food2.hideturtle()
food2.shape("triangle")
food2.pu()
food2.color(randint(1,254),randint(1,254),randint(1,254))
food2.goto(-100,100)
food2.showturtle()
food2.speed(0)

food3=Turtle()
food3.hideturtle()
food3.shape("triangle")
food3.pu()
food3.color(randint(1,254),randint(1,254),randint(1,254))
food3.goto(-100,-100)
food3.showturtle()
food3.speed(0)

food4=Turtle()
food4.hideturtle()
food4.shape("triangle")
food4.pu()
food4.color(randint(1,254),randint(1,254),randint(1,254))
food4.goto(100,-100)
food4.showturtle()
food4.speed(0)

scoreboard = Turtle()
scoreboard.hideturtle()
scoreboard.pu()
scoreboard.color(255,255,255)
scoreboard.goto(0,255)
scoreboard.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "normal"))

#variables
plyr1_score=0
plyr2_score=0
highScore=0

def updateScore():
    scoreboard.clear()
    scoreboard.write("Player 1: " + str(plyr1_score) + " Player 2: " + str(plyr2_score) + " High Score: "+ str(highScore), align="center", font=("Courier", 18, "normal"))

def plyr1_startOver():
    global plyr1_score
    global highScore
    
    player1.goto(0,0)
    player1.clearstamps()

    if plyr1_score > highScore:
       highScore=plyr1_score

    plyr1_score=0
    updateScore()

def plyr2_startOver():
    global plyr2_score
    global highScore
    
    player2.goto(0,0)
    player2.clearstamps()

    if plyr2_score > highScore:
       highScore=plyr2_score

    plyr2_score=0
    updateScore()
       
def checkForWall():
    if player1.xcor() > 350 or player1.xcor() < -350 or player1.ycor() > 300 or player1.ycor() < -300:
      plyr1_startOver()

    if player2.xcor() > 350 or player2.xcor() < -350 or player2.ycor() > 300 or player2.ycor() < -300:
      plyr2_startOver()
      
def checkForTail():
     # canvas use different coordinates than turtle
    y = player1.ycor() *-1
    x = player1.xcor()

    if player1.heading() == 0:
        x= x+5
    elif player1.heading() == 180:
        x= x-5
    elif player1.heading() == 90:
        y= y-5
    elif player1.heading() == 270:
        y= y+5

    canvas = getcanvas() # get access to tkinter.Canvas
    ids = canvas.find_overlapping(x, y, x, y) # find IDs of all objects in rectangle

    if ids:     # if found objects
        index = ids[-1]        # get ID of last object (top most)
        color = canvas.itemcget(index, "fill")        # get its color

        if color == '#0000ff':
            plyr1_startOver()

    y = player2.ycor() *-1
    x = player2.xcor()

    if player2.heading() == 0:
        x= x+5
    elif player2.heading() == 180:
        x= x-5
    elif player2.heading() == 90:
        y= y-5
    elif player2.heading() == 270:
        y= y+5

    canvas = getcanvas() # get access to tkinter.Canvas
    ids = canvas.find_overlapping(x, y, x, y) # find IDs of all objects in rectangle

    if ids:     # if found objects
        index = ids[-1]        # get ID of last object (top most)
        color = canvas.itemcget(index, "fill")        # get its color

        if color == '#0000ff':
            plyr2_startOver()

    
def KeyUp():
    if player1.heading() != 270:
      player1.seth(90)

def KeyLeft():
    if player1.heading() != 0:
      player1.seth(180)

def KeyRight():
    if player1.heading() != 180:
      player1.seth(0)

def KeyDown():
    if player1.heading() != 90:
      player1.seth(270)
      
def KeyUp2():
    if player2.heading() != 270:
      player2.seth(90)

def KeyLeft2():
    if player2.heading() != 0:
      player2.seth(180)

def KeyRight2():
    if player2.heading() != 180:
      player2.seth(0)

def KeyDown2():
    if player2.heading() != 90:
      player2.seth(270)
      
def ExitKey():
    bye()

onkeypress(KeyUp,"Up")
onkeypress(KeyLeft,"Left")
onkeypress(KeyRight,"Right")
onkeypress(KeyDown,"Down")

onkeypress(KeyUp2,"w")
onkeypress(KeyUp2,"W")
onkeypress(KeyLeft2,"a")
onkeypress(KeyLeft2,"A")
onkeypress(KeyRight2,"d")
onkeypress(KeyRight2,"D")
onkeypress(KeyDown2,"s")
onkeypress(KeyDown2,"S")

onkeypress(ExitKey,"x")

listen()

while True:
    update()
    player1.color(0,0,255)
    player1.stamp()
    player1.color(255,255,255)
    player1.fd(10)

    if player1.distance(food) < 20:
      food.hideturtle()
      food.goto(randint(-300,300),randint(-250,250))
      food.color(randint(1,254),randint(1,254),randint(1,254))
      food.showturtle()

    
      plyr1_score+=10
      updateScore()

    else:
        player1.clearstamps(1)

    if player1.distance(food2) < 20:
       player1.stamp()
       food2.hideturtle()
       food2.goto(randint(-300,300),randint(-250,250))
       food2.color(randint(1,254),randint(1,254),randint(1,254))
       food2.showturtle()

       plyr1_score+=10
       updateScore()
       
    if player1.distance(food3) < 20:
       player1.stamp()
       food3.hideturtle()
       food3.goto(randint(-300,300),randint(-250,250))
       food3.color(randint(1,254),randint(1,254),randint(1,254))
       food3.showturtle()

       plyr1_score+=10
       updateScore()

    if player1.distance(food4) < 20:
       player1.stamp()
       food4.hideturtle()
       food4.goto(randint(-300,300),randint(-250,250))
       food4.color(randint(1,254),randint(1,254),randint(1,254))
       food4.showturtle()

       plyr1_score+=10
       updateScore()

     
    player2.color(0,0,255)
    player2.stamp()
    player2.color(255,0,0)
    player2.fd(10)

    if player2.distance(food) < 20:
      player2.stamp()
      food.hideturtle()
      food.goto(randint(-300,300),randint(-250,250))
      food.color(randint(1,254),randint(1,254),randint(1,254))
      food.showturtle()


      plyr2_score+=10
      updateScore()

    else:
        player2.clearstamps(1)


    if player2.distance(food2) < 20:
       food2.hideturtle()
       food2.goto(randint(-300,300),randint(-250,250))
       food2.color(randint(1,254),randint(1,254),randint(1,254))
       food2.showturtle()

       plyr2_score+=10
       updateScore()
       
    if player2.distance(food3) < 20:
       food3.hideturtle()
       food3.goto(randint(-300,300),randint(-250,250))
       food3.color(randint(1,254),randint(1,254),randint(1,254))
       food3.showturtle()

       plyr2_score+=10
       updateScore()

    if player2.distance(food4) < 20:
       player2.stamp()
       food4.hideturtle()
       food4.goto(randint(-300,300),randint(-250,250))
       food4.color(randint(1,254),randint(1,254),randint(1,254))
       food4.showturtle()

       plyr2_score+=10
       updateScore()
    
    

    checkForWall()
    checkForTail()


    
    sleep(0.05)
