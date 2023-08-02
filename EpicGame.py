import turtle
import EnemyBlocks
import random as rd


#Screen
screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=1.00, height=1.00,startx=None, starty=None)
screen.tracer(0)

#Intro Text on the screen
intro = turtle.Turtle()
intro.hideturtle()
intro.penup()
intro.color('white')
intro.setposition(0,250)
intro.write('Use W A S D Keys to Move \n The Borders are your friend',font=['Courier',30],align='center')
screen.ontimer(intro.clear(),t=2500)


#The actual cube
cubey=turtle.Turtle()
cubey.shape('square')
cubey.color('white')
cubey.showturtle()
size = 1
cubey.shapesize(size)
cubey.penup()
speed = 1.5
width =screen.window_width()
height = screen.window_height()


#Controls
def move_right():
    cubey.setheading(0)

def move_left():
    cubey.setheading(180)
            

def move_up():
    cubey.setheading(90)

def move_down():
    cubey.setheading(270)
    
     
#Controls 
screen.listen()
screen.onkeypress(move_right,'d')
screen.onkey(move_left, 'a')
screen.onkey(move_up, 'w')
screen.onkey(move_down, 's')

#Enemy
#enemy =EnemyBlocks.Enemy(1,2,1.2)
#enemy.spawn([-250,40])


enemies =[]
elength =2
espeed = 1.3
enemies.append(EnemyBlocks.Enemy(elength,espeed))
enemies[0].spawn([rd.randint(int(-width/2),int(width/2)), rd.randint(int(-height/2),int(height/2))])

#Pen for score
score =0
pen =turtle.Turtle()
pen.penup()
pen.ht()
pen.goto(0,410)
pen.color('white')
pen.write("Score: {}".format(score),font=['Courier', 12], align='center')



#Highscore
highscore =0
highpen=turtle.Turtle()
highpen.penup()
highpen.hideturtle()
highpen.goto(110,410)
highpen.color('white')
highpen.write("High Score: {}".format(highscore), font=['Courier', 12], align='center')

#Update the score
def score_update():
    global score
    score+=1
    pen.clear()
    pen.write("Score: {}".format(score),font=['Courier', 12], align='center')



#Spawns berries
def spawn_berry(pos,size):
    berry =turtle.Turtle()
    berry.shape('circle')
    berry.color('red')
    berry.penup()
    berry.shapesize(size)
    berry.goto(pos)
    berry.hideturtle()
    return berry
berry_size =1.2
berry = spawn_berry([rd.randint(int(-width/2+berry_size),int(width/2-berry_size)), rd.randint(int(-height/2+berry_size),int(height/2-berry_size))],berry_size)
berry.showturtle()

#Reset score
def reset_score():
    global score
    score=0
    pen.clear()
    pen.write("Score: {}".format(score),font=['Courier', 12], align='center')

#Update hig score
def update_high_score():
    global score
    highpen.clear()
    highpen.write("High Score: {}".format(score),font=['Courier', 12], align='center')




#Mainloop
while True:
    for enemy in enemies:
        enemy.attack(cubey.xcor(), cubey.ycor())
    cubey.forward(speed)
    #Boundaries
    if cubey.ycor()<=-height/2:
        cubey.sety(height/2)
    elif cubey.ycor() >=height/2:
        cubey.sety(-height/2)
    if cubey.xcor()<= (-width/2):
        cubey.setx(width/2)
    elif cubey.xcor()>=width/2:
        cubey.setx(-width/2) 

    #Enemy Collision
    for enemy in enemies:
        if ((cubey.xcor()-size*10<= enemy.get_xcor()+enemy.length*10 and cubey.xcor()+size*10 >= enemy.get_xcor()-enemy.length*10) and (cubey.ycor()-size*10 <= enemy.get_ycor()+ enemy.length/2*10) and (cubey.ycor()+size*10 >= enemy.get_ycor()-enemy.length/2*10)):       
            for e in enemies[:-1]:
                e.hide()
                enemies.remove(e)
            cubey.goto(0,0)
            enemies[0].speed=1.3
            enemies[0].length =2
            enemy.goto([rd.randint(int(-width/2),int(width/2)), rd.randint(int(-height/2),int(height/2))])
            berry.goto([rd.randint(int(-width/2),int(width/2)), rd.randint(int(-height/2),int(height/2))])
            speed =1.5
            elength =2
            espeed = 1.3
            update_high_score()
            reset_score()
      
        

    #Berry Collision
    if ((cubey.xcor()-size*10<= berry.xcor()+berry_size*10 and cubey.xcor()+size*10 >= berry.xcor()-berry_size*10) and (cubey.ycor()-size*10 <= berry.ycor()+ berry_size*10) and (cubey.ycor()+size*10 >= berry.ycor()-berry_size*10)):
        score_update()
        berry.goto([rd.randint(int(-width/2),int(width/2)), rd.randint(int(-height/2),int(height/2))])
        speed+=.25
        espeed +=.25
        enemies.append(EnemyBlocks.Enemy(elength,espeed))
        enemies[-1].spawn([rd.randint(int(-width/2),int(width/2)), rd.randint(int(-height/2),int(height/2))])

        
    screen.update()


