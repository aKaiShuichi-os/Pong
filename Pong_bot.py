import turtle
import time
import random
import pygame


#seeting up screen
window = turtle.Screen()
window.title("PONG @Vinayak")
window.bgpic("wallhaven-83xzzk_800x600.png")
window.setup(width = 800,height = 600)
window.tracer(0)

#Collision Sound

pygame.mixer.init()
Pongsound = pygame.mixer.Sound("salamisound-3924547-shock-impact-metallic (online-audio-converter.com).wav")

#score
score_a = 0
score_b = 0
player_b = turtle.textinput(" ",f"Enter Your Name:")

# paddle_a

paddle_a = turtle.Turtle()
paddle_a.speed(5)
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
i_d = [-1,1]

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
pen.write(f"PyBot score {score_a} && {player_b} score {score_b}", align = "center" ,font=("Courier", 15, "normal"))


#Another turtle

con = turtle.Turtle()
con.speed(0)
con.color("white")
con.shape("circle")

con.hideturtle()
con.penup()
con.goto(0,-200)

#functions

#levels of game

is_easy = False
is_medium = False
is_hard = False

def Game_level():
    
    global is_easy
    global is_medium
    global is_hard
    
    game_level = turtle.textinput("Game Level",f"Select The level of game \n 1.Easy\n 2.Medium\n 3.Hard")
    
    if game_level.lower() in ['e','easy']:
        is_easy = True
        is_medium = False
        is_hard = False
        ball.dx = 1.5
        ball.dy = 1.5
        
    if game_level.lower() in ['m','medium']:
        is_medium = True
        is_easy = False
        is_hard = False
        ball.dx = 1.5
        ball.dy = 1.5
    if game_level.lower() in ['h','hard']:
        is_hard = True
        is_easy = False
        is_medium = False
        ball.dx = 2
        ball.dy = 2

#1.Controlling functions 

def paddle_b_Up():
    if not is_pause:
        if paddle_b.ycor() < 250:
            y = paddle_b.ycor()
            y += 25
            paddle_b.sety(y)
        else:
            paddle_b.sety(248)

def paddle_b_Down():
    if not is_pause:
        if paddle_b.ycor() > -250:
            y = paddle_b.ycor()
            y -= 25
            paddle_b.sety(y)
        else:
            paddle_b.sety(-248)

def paddle_a_Up(vel):
    if paddle_a.ycor() < 260:
        y = paddle_a.ycor()
        y += vel
        paddle_a.sety(y)
    else:
        paddle_a_Down(2)

def paddle_a_Down(vel):
    if paddle_a.ycor() > -260:
        y = paddle_a.ycor()
        y -= vel
        paddle_a.sety(y)
    else:
        paddle_a_Up(2)

        
#bot(paddle_a) movement
def paddle_a_movements(m_f):
    if ball.dx <= -1:
                    
        if paddle_a.ycor() > 250:
            paddle_a_Down(3)
        if paddle_a.ycor() < -250:
            paddle_a_Up(3)

        if abs(ball.xcor()-paddle_a.xcor()) < 200 and abs(ball.ycor()-paddle_a.ycor()) in range(0,50):
            if ball.dy >= 1:
                paddle_a_Up(1)
            else:
                paddle_a_Down(1)
        else:
            if is_easy:
                
                if ball.ycor() > paddle_a.ycor():
                    if paddle_a.ycor() > 250:
                        paddle_a_Down(3)
                    paddle_a_Up(abs(ball.ycor()-paddle_a.ycor())*.029)
                if ball.ycor() < paddle_a.ycor():
                    if paddle_a.ycor() < -250:
                        paddle_a_Up(3)
                    paddle_a_Down(abs(ball.ycor()-paddle_a.ycor())*.029)
            elif is_medium:
                if ball.ycor() > paddle_a.ycor():
                    if paddle_a.ycor() > 250:
                        paddle_a_Down(3)
                    paddle_a_Up(abs(ball.ycor()-paddle_a.ycor())*.03)
                if ball.ycor() < paddle_a.ycor():
                    if paddle_a.ycor() < -250:
                        paddle_a_Up(3)
                    paddle_a_Down(abs(ball.ycor()-paddle_a.ycor())*.03)
                    
            else:
                paddle_a.sety(ball.ycor())
                

#collission functions 

def ball_boundary_Collision():
    
    
    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy*= -1
        Pongsound.play()


    if ball.ycor() < -300:
        ball.sety(-300)
        ball.dy*= -1
        Pongsound.play()
        

        
def ball_paddle_Coliision():
    
    
    if ball.xcor() < -380 and ball.xcor() > -390 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-380)
        ball.dx *= -1
        Pongsound.play()

    if ball.xcor() > 370 and ball.xcor() < 380 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(370)
        ball.dx *= -1
        Pongsound.play()
        

        
def miss_Ball():
    
    global score_a
    global score_b
    global no_of_tries
    
    if ball.xcor() > 380:
        score_a += 5
        pen.clear()
        pen.write(f"PyBot score {score_a} && {player_b} score {score_b}", align = "center" ,font=("Courier", 15, "normal"))
        time.sleep(1)
        ball.goto(0,0)
        #ball.setheading(int(random.choice([0,180,270,90])))
        ball.dx *= random.choice(i_d)
        no_of_tries +=1


    if ball.xcor() < -390:
        score_b += 5
        pen.clear()
        pen.write(f"PyBot score {score_a} && {player_b} score {score_b}", align = "center" ,font=("Courier", 15, "normal"))
        time.sleep(1)
        ball.goto(0,0)
        #ball.setheading(int(random.choice([0,180,270,90])))
        ball.dx *= random.choice(i_d)
        no_of_tries += 1
                                      
    
#2. pause function

is_pause = False

def toggle_pause():
    global is_pause
    
    if is_pause == True:
        is_pause = False
    else:
        is_pause = True
        
#3.End finction
def End_game():
    
    no_of_tries = no_of_rounds
    time.sleep(1)
    window.bye()

#4.winner funtion

def Winnner():
    
    global to_address
    
    if score_a > score_b:
        con.write("PyBot WIN", align = "center" ,font=("Courier", 30, "normal"))
        
    
    elif score_a == score_b: 
        con.write("DRAW!!!", align = "center" ,font=("Courier", 40, "normal"))
       
                
    else:
        con.write(f"{player_b} WIN", align = "center" ,font=("Courier", 30, "normal"))


        
#Game inputs



no_of_rounds =  int(turtle.numinput("NO OF ROUNDS","How many rounds do you want play?(1-20)",default = 5,minval = 1,maxval = 20))
m_f = Game_level()
start = turtle.textinput("(yes/no)",f"\t\t\tRULES OF THE GAME\n\n\n1.There will be {no_of_rounds} rounds exactly\n2.Player with the highest score will be declared winner\n\n\t\t\tDo you want to start!!! type yes or no")

    
#keyboard bindings

window.listen()
window.onkeypress(paddle_b_Up,"Up")
window.onkeypress(paddle_b_Down,"Down")
window.onkeypress(toggle_pause,"space")
window.onkeypress(End_game,"e")

#GAME
#Starts here


if start in ['yes','yeah','y','ye','yup','']:
    
    no_of_tries = 0
    running = True
    
    while running:
        
        time.sleep(1)
        while no_of_tries < no_of_rounds:
            
            if not is_pause:
                window.update()

                ball.setx(ball.xcor() + ball.dx )
                ball.sety(ball.ycor() + ball.dy)
                
                paddle_a_movements(m_f)
               
                ball_boundary_Collision()
                   
                miss_Ball()

                ball_paddle_Coliision()
                        
                            
            else:
                window.update()

        #Announcing Winners

        Winnner()

        #Asking to play again

        choice = turtle.textinput("yes/no","Do you wanna play again")

        if choice in ['yes','ye','y','yeah','yup','']:

            #continue the game   
            #for that ......      

            #setting the variables again

            m_f = Game_level()
            no_of_rounds =  int(turtle.numinput("NO OF ROUNDS","How many rounds do you want play?(1-20)",default = 5,minval = 1,maxval = 20))
            no_of_tries = 0
            score_a = 0
            score_b = 0
            con.clear()
            pen.clear()
            pen.write(f"PyBot score {score_a} && {player_b} score {score_b}", align = "center" ,font=("Courier", 15, "normal"))

            #setting listen method again for 2nd round
            
            window.listen()
            window.onkeypress(paddle_b_Up,"Up")
            window.onkeypress(paddle_b_Down,"Down")
            window.onkeypress(toggle_pause,"space")
            window.onkeypress(End_game,"e")
            
            continue                                   

        else:               
            break                            #break through the Gaming loop

    #clear previous texts 

    
    pen.clear()
    con.clear()
    pen.goto(0,0)

    #Display a goodbye message

    pen.write("Please Visit Again!!!\n\nThANK YOU!!!", align = "center" ,font=("Courier", 20, "normal"))
    time.sleep(2)
    window.bye()


else:

    pen.clear()
    pen.goto(0,0)
    pen.write("Come Any At Any Time When You Want To Play\n\nThANK YOU!!!", align = "center" ,font=("Courier", 20, "normal"))
    time.sleep(3)
    window.bye()
