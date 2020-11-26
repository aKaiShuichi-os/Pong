import turtle
import pygame


#seeting up screen
window = turtle.Screen()
window.title("PONG @Vinayak")
window.bgcolor(.5,0,.5)
window.setup(width = 800,height = 600)
window.tracer(0)

#sounds 
pygame.mixer.init()
Pongsound = pygame.mixer.Sound("salamisound-3924547-shock-impact-metallic (online-audio-converter.com).wav")

#score
score_a = 0
score_b = 0

# paddle_a

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-390,0)

#paddle_b

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(380,0)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1



#pen

pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.shape("circle")

pen.hideturtle()
pen.penup()
pen.goto(0,260)
pen.write(f"Player_a score {score_a} && Player_b score {score_b}", align = "center" ,font=("Courier", 15, "normal"))

#functions

def paddle_a_Up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_Down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_Up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_Down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
#keyboard bindings

window.listen()
window.onkeypress(paddle_a_Up,"w")
window.onkeypress(paddle_a_Down,"s")
window.onkeypress(paddle_b_Up,"Up")
window.onkeypress(paddle_b_Down,"Down")




running = True

#start = turtle.textinput("Do you want to play!!!","(yes/no)")

while running:
    window.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy*= -1
        Pongsound.play()
        
        
    if ball.ycor() < -300:
        ball.sety(-300)
        ball.dy*= -1
        Pongsound.play()
    
    if ball.xcor() > 380:
        score_a += 5
        pen.clear()
        pen.write(f"Player_a score {score_a} && Player_b score {score_b}", align = "center" ,font=("Courier", 15, "normal"))
        ball.goto(0,0)
        ball.dx *= -1
        
    if ball.xcor() < -390:
        score_b += 5
        pen.clear()
        pen.write(f"Player_a score {score_a} && Player_b score {score_b}", align = "center" ,font=("Courier", 15, "normal"))
        ball.goto(0,0)
        ball.dx *= -1
        
    if ball.xcor() < -380 and ball.xcor() > -390 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.setx(-380)
            ball.dx *= -1
            Pongsound.play()
        
    if ball.xcor() > 370 and ball.xcor() < 380 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.setx(370)
            ball.dx *= -1
            Pongsound.play()

    
    

