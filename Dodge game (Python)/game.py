import turtle
import random
import time
n=0
bullets =[]
#screen
screen = turtle.Screen()
screen.setup(800,700)
screen.tracer(0,0)
screen.bgpic("Dodge game (Python)/space3_c.png")
screen.addshape("Dodge game (Python)/guete_resized (1).gif")
screen.addshape("Dodge game (Python)/estrela_updated_resized-_1_.gif")

#spawn bullet
def spawn():
    global n,bullets
    bullets.append(turtle.Turtle())
    bullets[n].shape("Dodge game (Python)/estrela_updated_resized-_1_.gif")
    bullets[n].penup()
    bullets[n].goto(random.randint(-350,350),350)
    n+=1
t=0
person = turtle.Turtle()
person.penup()
person.shape("Dodge game (Python)/guete_resized (1).gif")
person.turtlesize(100,111,111)
person.color("red")
person.goto(0,-300)
def move_left():
    global person
    if person.xcor()>-370:
        person.goto(person.xcor()-10,person.ycor())
def move_right():
    global person
    if person.xcor() < 370:
        person.goto(person.xcor()+10,person.ycor())    
screen.listen()    
screen.onkeypress(move_left,"Left")    
screen.onkeypress(move_right,"Right")  
k=10 
level = 1
lvl = turtle.Turtle()
lvl.penup()
lvl.hideturtle()
lvl.goto(-300,250)
lvl.color("white")
lvl.write("Level: {}".format(level),align="center",font=("arial",24,"bold"))
minute =0
second =0
inicio = time.time()
times = turtle.Turtle()
times.penup()
times.hideturtle()
times.goto(-230,200)
times.color("white")
times.write("Tempo: {}:{}".format(minute,second),align="center",font=("arial",20,"bold"))
while True:
    screen.update()
    if len(bullets)>0 and bullets[0].ycor()-person.ycor()<60 and (bullets[0].xcor()-person.xcor()<15 and bullets[0].xcor()-person.xcor()>-15):
        fim = turtle.Turtle()
        fim.penup()
        fim.hideturtle()
        fim.goto(0,0)
        fim.color("red")
        fim.write("PERDEU!",align="center",font=("arial",60,"bold"))
        screen.exitonclick()
    if t%k==0:
        spawn() 
    for i in range(0,n):
        if bullets[i].ycor()>-320:
            bullets[i].goto(bullets[i].xcor(),bullets[i].ycor()-30)
        else:
            bullets[i].hideturtle() 
            bullets.pop(i)
            n-=1 
            break
    if t%200==0 and k>0 and t>0:
        k-=1
        level += 1
        lvl.clear()
        lvl.write("Level: {}".format(level),align="center",font=("arial",24,"bold"))
    times.clear()
    times.write("Tempo: {} segundos".format(round(time.time()-inicio,2)),align="center",font=("arial",20,"bold"))    
    if time.time()-inicio > 150:
        win = turtle.Turtle()
        win.penup()
        win.hideturtle()
        win.goto(0,0)
        win.color("green")
        win.write("GANHOU!",align="center",font=("arial",60,"bold"))
        screen.exitonclick()
    time.sleep(0.05)
    t+=1
