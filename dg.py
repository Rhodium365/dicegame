import turtle
import random
import tkinter as tk
from tkinter import *
from tkinter import font

tut = turtle.Screen()
tut.bgcolor("saddlebrown")
tut.title("dice game")
Die = turtle.Turtle()
Die.ht()
Die.speed(0)
tex = turtle.Turtle()
tex.ht()
tex.up()
tex.speed(3)
turtle.colormode(cmode=255)



def rolP1():
    global P1total
    dice3=0
    Die.goto(-50,-200)
    diedelete()
    Die.up()
    Die.goto(-260,-200)
    Die.seth(0)
    dice1 = random.randint(1,6)
    if dice1==1:
        reddieone()
    elif dice1 == 2:
        reddietwo()
    elif dice1 == 3:
        reddiethree()
    elif dice1 == 4:
        reddiefour()
    elif dice1 == 5:
        reddiefive()
    else:
        reddiesix()
    dice2 = random.randint(1,6)
    Die.goto(160,-200)
    Die.seth(0)
    if dice2==1:
        reddieone()
    elif dice2 == 2:
        reddietwo()
    elif dice2 == 3:
        reddiethree()
    elif dice2 == 4:
        reddiefour()
    elif dice2 == 5:
        reddiefive()
    else:
        reddiesix()
    print(dice1,"and",dice2)
    if (dice1 + dice2)%2 ==0:
        P1total=P1total+10
        print("EVEN! an additional 10 points!")
        tex.goto(0,-50)
        tex.write(("EVEN!(+10)"), True, align="center",font=("Small Fonts",20,"normal"))
    else:
        P1total=P1total-5
        print("ODD! you loose 5 points!")
        tex.goto(0,-50)
        tex.write(("ODD!(-5)"), True, align="center",font=("Small Fonts",20,"normal"))
    if dice1 ==  dice2:
        print("EQUAL! get an extra dice!")
        tex.goto(0,-100)
        tex.write(("EQUAL!(3rd dice)"), True, align="center",font=("Small Fonts",20,"normal"))
        Die.goto(-50,-200)
        Die.seth(0)
        dice3 = random.randint(1,6)
        if dice3==1:
            reddieone()
        elif dice3 == 2:
            reddietwo()
        elif dice3 == 3:
            reddiethree()
        elif dice3 == 4:
            reddiefour()
        elif dice3 == 5:
            reddiefive()
        else:
            reddiesix()
        print(dice3)
    
    P1total = P1total + (dice1+dice2+dice3)
    if P1total < 0:
        P1total = P1total - P1total
    print("P1 total =",P1total)


def rolP2():
    global P2total
    dice3 = 0
    Die.up
    Die.goto(-50,200)
    diedelete()
    Die.goto(-260,200)
    Die.seth(0)
    dice1 = random.randint(1,6)
    if dice1==1:
        bluedieone()
    elif dice1 == 2:
        bluedietwo()
    elif dice1 == 3:
        bluediethree()
    elif dice1 == 4:
        bluediefour()
    elif dice1 == 5:
        bluediefive()
    else:
        bluediesix()
    dice2 = random.randint(1,6)
    Die.goto(160,200)
    Die.seth(0)
    if dice2==1:
        bluedieone()
    elif dice2 == 2:
        bluedietwo()
    elif dice2 == 3:
        bluediethree()
    elif dice2 == 4:
        bluediefour()
    elif dice2 == 5:
        bluediefive()
    else:
        bluediesix()
    print(dice1,"and",dice2)
    if (dice1 + dice2)%2 ==0:
        P2total=P2total+10
        print("EVEN! an additional 10 points!")
        tex.goto(0,100)
        tex.write(("EVEN!(+10)"), True, align="center",font=("Small Fonts",20,"normal"))
    else:
        P2total=P2total-5
        print("ODD! you loose 5 points!")
        tex.goto(0,100)
        tex.write(("ODD!(-5)"), True, align="center",font=("Small Fonts",20,"normal"))
    if dice1 ==  dice2:
        print("EQUAL! get an extra dice!")
        tex.goto(0,150)
        tex.write(("EQUAL!(3rd dice)"), True, align="center",font=("Small Fonts",20,"normal"))
        Die.goto(-50,200)
        Die.seth(0)
        dice3 = random.randint(1,6)
        if dice3==1:
            bluedieone()
        elif dice3 == 2:
            bluedietwo()
        elif dice3 == 3:
            bluediethree()
        elif dice3 == 4:
            bluediefour()
        elif dice3 == 5:
            bluediefive()
        else:
            bluediesix()
        print(dice3)
    P2total = P2total + (dice1+dice2)
    if P2total < 0:
        P2total = P2total - P2total
    print("p2 total =",P2total)



def diedelete():
    Die.up()
    Die.color(tut.bgcolor(),tut.bgcolor())
    Die.down()
    Die.begin_fill()
    for i in range(4):
        Die.fd(100)
        Die.lt(90)
    Die.end_fill()
    Die.seth(0)
    Die.home()

def reddieone():
    Die.up()
    Die.color("black",p1col)
    Die.down()
    Die.begin_fill()
    for i in range(4):
        Die.fd(100)
        Die.lt(90)
    Die.end_fill()
    Die.up()
    Die.fd(50)
    Die.lt(90)
    Die.fd(50)
    Die.dot(20,"white")
    Die.seth(0)
    Die.home()

def reddietwo():
    Die.up()
    Die.color("black",p1col)
    Die.down()
    Die.begin_fill()
    for i in range(4):
        Die.fd(100)
        Die.lt(90)
    Die.end_fill()
    Die.up()
    Die.fd(25)
    Die.lt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.fd(50)
    Die.rt(90)
    Die.fd(50)
    Die.dot(20,"white")
    Die.seth(0)
    Die.home()

def reddiethree():
    Die.up()
    Die.color("black",p1col)
    Die.down()
    Die.begin_fill()
    for i in range(4):
        Die.fd(100)
        Die.lt(90)
    Die.end_fill()
    Die.up()
    Die.fd(25)
    Die.lt(90)
    Die.fd(75)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(25)
    Die.rt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.lt(90)
    Die.fd(25)
    Die.rt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.seth(0)
    Die.home()

def reddiefour():
    Die.up()
    Die.color("black",p1col)
    Die.down()
    Die.begin_fill()
    for i in range(4):
        Die.fd(100)
        Die.lt(90)
    Die.end_fill()
    Die.up()
    Die.fd(25)
    Die.lt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.fd(50)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(50)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(50)
    Die.dot(20,"white")
    Die.seth(0)
    Die.home()

def reddiefive():
    Die.up()
    Die.color("black",p1col)
    Die.down()
    Die.begin_fill()
    for i in range(4):
        Die.fd(100)
        Die.lt(90)
    Die.end_fill()
    Die.up()
    Die.fd(25)
    Die.lt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.fd(50)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(50)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(50)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(25)
    Die.rt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.seth(0)
    Die.home()

def reddiesix():
    Die.up()
    Die.color("black",p1col)
    Die.down()
    Die.begin_fill()
    for i in range(4):
        Die.fd(100)
        Die.lt(90)
    Die.end_fill()
    Die.up()
    Die.fd(25)
    Die.lt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.fd(25)
    Die.dot(20,"white")
    Die.fd(25)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(50)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.fd(25)
    Die.dot(20,"white")
    Die.seth(0)
    Die.home()

def bluedieone():
    Die.up()
    Die.color("black",p2col)
    Die.down()
    Die.begin_fill()
    for i in range(4):
        Die.fd(100)
        Die.lt(90)
    Die.end_fill()
    Die.up()
    Die.fd(50)
    Die.lt(90)
    Die.fd(50)
    Die.dot(20,"white")
    Die.seth(0)
    Die.home()

def bluedietwo():
    Die.up()
    Die.color("black",p2col)
    Die.down()
    Die.begin_fill()
    for i in range(4):
        Die.fd(100)
        Die.lt(90)
    Die.end_fill()
    Die.up()
    Die.fd(25)
    Die.lt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.fd(50)
    Die.rt(90)
    Die.fd(50)
    Die.dot(20,"white")
    Die.seth(0)
    Die.home()

def bluediethree():
    Die.up()
    Die.color("black",p2col)
    Die.down()
    Die.begin_fill()
    for i in range(4):
        Die.fd(100)
        Die.lt(90)
    Die.end_fill()
    Die.up()
    Die.fd(25)
    Die.lt(90)
    Die.fd(75)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(25)
    Die.rt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.lt(90)
    Die.fd(25)
    Die.rt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.seth(0)
    Die.home()

def bluediefour():
    Die.up()
    Die.color("black",p2col)
    Die.down()
    Die.begin_fill()
    for i in range(4):
        Die.fd(100)
        Die.lt(90)
    Die.end_fill()
    Die.up()
    Die.fd(25)
    Die.lt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.fd(50)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(50)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(50)
    Die.dot(20,"white")
    Die.seth(0)
    Die.home()

def bluediefive():
    Die.up()
    Die.color("black",p2col)
    Die.down()
    Die.begin_fill()
    for i in range(4):
        Die.fd(100)
        Die.lt(90)
    Die.end_fill()
    Die.up()
    Die.fd(25)
    Die.lt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.fd(50)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(50)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(50)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(25)
    Die.rt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.seth(0)
    Die.home()

def bluediesix():
    Die.up()
    Die.color("black",p2col)
    Die.down()
    Die.begin_fill()
    for i in range(4):
        Die.fd(100)
        Die.lt(90)
    Die.end_fill()
    Die.up()
    Die.fd(25)
    Die.lt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.fd(25)
    Die.dot(20,"white")
    Die.fd(25)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(50)
    Die.dot(20,"white")
    Die.rt(90)
    Die.fd(25)
    Die.dot(20,"white")
    Die.fd(25)
    Die.dot(20,"white")
    Die.seth(0)
    Die.home()


#valid1 = input("P1, please enter your code(an @ followed by your 4 numbers )")
#while valid1 != "@0001":
#    print ("please try again")
#    valid1 = input("please enter your code(an @ followed by your 4 numbers )")
    
print("P1 validation complete")
    

#valid2 = input("P2, please enter your code(an @ followed by your 4 numbers )")
#while valid2 != "@0002":
#    print ("please try again")
#    valid2 = input("please enter your code(an @ followed by your 4 numbers )")
    
print("P2 validation complete")



def rnd():
    global autoplay
    if autoplay == False:
        roll = turtle.textinput("DICEGAME", "P1 roll")#.lower()
    else:
        tex.speed(0)
    #while roll != "roll":
    #    print ("please try again")
    #    roll = input("P1 roll your dice").lower()
    tex.clear()
    Die.clear()
    rolP1()

    if autoplay == False:
        roll = turtle.textinput("DICEGAME", "P2 roll")#.lower()
    #while roll != "roll":
     #   print ("please try again")
     #   roll = input("P1 roll your dice").lower()
    rolP2()
    
    tex.goto(0,0)
    tex.write(("Player1 total =",P1total), True, align="center",font=("Small Fonts",20,"normal"))
    tex.goto(0,50)
    tex.write(("Player2 total =",P2total), True, align="center",font=("Small Fonts",20,"normal"))



def game():
    tex.clear()
    global all_scores
    global P1total
    global P2total
    global rounds
    P1total=0
    P2total=0
    for i in range(rounds):
        rnd()
    tex.speed(3)
    tex.goto(-200,25)
    tex.write(("Game ending..."), True, align="right",font=("Small Fonts",15,"normal"))
    tex.goto(200,25)
    tex.write(("Game ending..."), True, align="left",font=("Small Fonts",15,"normal"))
    tex.speed(1)
    tex.fd(200)
    tex.clear()
    Die.clear()
    tex.speed(0)
    if P1total > P2total:
        tex.goto(0,50)
        tex.write(("P1 WINS!"), True, align="center",font=("Small Fonts",40,"normal"))
        tex.goto(0,0)
        tex.write(("P1 total =",P1total), True, align="center",font=("Small Fonts",30,"normal"))
        tex.goto(0,-40)
        tex.write(("P2 total =",P2total), True, align="center",font=("Small Fonts",30,"normal"))
        print ("PLAYER1 WINS! (P1 total =",P1total," P2 total =",P2total,)
    elif P2total > P1total:
        tex.goto(0,50)
        tex.write(("P2 WINS!"), True, align="center",font=("Small Fonts",40,"normal"))
        tex.goto(0,0)
        tex.write(("P1 total =",P1total), True, align="center",font=("Small Fonts",30,"normal"))
        tex.goto(0,-40)
        tex.write(("P2 total =",P2total), True, align="center",font=("Small Fonts",30,"normal"))
        print ("PLAYER2 WINS! (P1 total =",P1total," P2 total =",P2total)
    else:
        tex.goto(0,50)
        tex.write(("SUDDEN DEATH! Tied: "), True, align="center",font=("Small Fonts",50,"normal"))
        tex.goto(0,0)
        tex.write(("Tied: ",P1total,), True, align="center",font=("Small Fonts",30,"normal"))
        suddendeath()
    all_scores = all_scores + P1total + P2total
    with open("dicegame_totalscore.txt",'w') as f:
        f.write (str(all_scores))
        f.close()
        
    if rounds <= 6:
        if P1total > 0:
            with open ("dicegame_scores.txt",'a') as f:
                f.write(str(P1total) + "\n")
                f.close
            scores.append(P1total)

        if P2total > 0:
            with open ("dicegame_scores.txt",'a') as f:
                f.write (str(P2total) +"\n")
                f.close
            scores.append(P2total)
        scores.sort(reverse=True)
    turtle.textinput("DICEGAME", "end game")
    menu()



def suddendeath():
    print("sudden death! (",P1total,")")
    turtle.textinput("Dice Game", "enter sudden death")
    rnd()
    tex.speed(6)
    tex.goto(-200,25)
    tex.write(("Game ending..."), True, align="right",font=("Small Fonts",15,"normal"))
    tex.goto(200,25)
    tex.write(("Game ending..."), True, align="left",font=("Small Fonts",15,"normal"))
    tex.speed(3)
    tex.fd(200)
    tex.clear()
    Die.clear()
    tex.speed(0)
    if P1total > P2total:
        tex.goto(0,50)
        tex.write(("P1 WINS!"), True, align="center",font=("Small Fonts",50,"normal"))
        tex.goto(0,0)
        tex.write(("P1 total =",P1total,), True, align="center",font=("Small Fonts",30,"normal"))
        tex.goto(0,-40)
        tex.write(("P2 total =",P2total), True, align="center",font=("Small Fonts",30,"normal"))
        print ("PLAYER1 WINS! (P1 total =",P1total," P2 total =",P2total,")")
    elif P2total > P1total:
        tex.goto(0,50)
        tex.write(("P2 WINS!"), True, align="center",font=("Small Fonts",40,"normal"))
        tex.goto(0,0)
        tex.write(("P1 total =",P1total), True, align="center",font=("Small Fonts",30,"normal"))
        tex.goto(0,-40)
        tex.write((" P2 total =",P2total), True, align="center",font=("Small Fonts",30,"normal"))
        print ("PLAYER2 WINS! (P1 total =",P1total," P2 total =",P2total,")")
    else:
        tex.goto(0,50)
        tex.write(("SUDDEN DEATH! Tied: "), True, align="center",font=("Small Fonts",50,"normal"))
        tex.goto(0,0)
        tex.write(("Tied: ",P1total), True, align="center",font=("Small Fonts",30,"normal"))
        suddendeath()
    turtle.textinput("DICEGAME", "end game")



def menu():
    global all_scores
    tex.clear()
    Die.clear()
    print ("MENU")
    print ("type start to start game, scores to view highscores or settings to review game settings")
    
    tex.speed(10)
    tex.goto(0,200)
    tex.write(("DICEGAME"), True, align="center",font=("Small Fonts",50,"normal"))
    print ("HIGHSCORES:")
    print ("#1:",scores[0])
    print ("#2:",scores[1])
    print ("#3:",scores[2])
    print ("#4:",scores[3])
    print ("#5:",scores[4])
    tex.goto(0,150)
    tex.write(("#1:",scores[0]), True, align="center",font=("Small Fonts",20,"normal"))
    tex.goto(0,120)
    tex.write(("#2:",scores[1]), True, align="center",font=("Small Fonts",20,"normal"))
    tex.goto(0,90)
    tex.write(("#3:",scores[2]), True, align="center",font=("Small Fonts",20,"normal"))
    tex.goto(0,60)
    tex.write(("#4:",scores[3]), True, align="center",font=("Small Fonts",20,"normal"))
    tex.goto(0,30)
    tex.write(("#5:",scores[4]), True, align="center",font=("Small Fonts",20,"normal"))
    tex.goto(0,-5)
    tex.write(("TOTAL",(all_scores)), True, align="center",font=("Small Fonts",23,"normal"))

    tex.goto(-100,-50)
    tex.write(("SETTINGS"), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto(100,-50)
    tex.write(("SCORES"), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto(0,-110)
    tex.write(("START"), True, align="center",font=("Small Fonts",40,"normal"))
    tex.goto(0,-160)
    tex.write(("QUIT"), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto(0,-210)
    tex.write(("-dicegame by Cuchulainn Moon"), True, align="center",font=("Small Fonts",10,"normal"))
    hub = turtle.textinput("DICEGAME", "menu")
    if hub.lower().startswith("set"):
        Settings()
    elif hub.lower() == "exit" or hub.lower() == "quit" or hub.lower().startswith("clos"):
        turtle.bye()
        print ("closing")
    elif hub.lower().startswith("star"):
        game()
    elif hub.lower().startswith("scor"):
        scoreboard()
    else:
        menu()

def scoreboard():
    tex.clear()
    tex.goto(0,210)
    tex.write(("ScoreBoard"), True, align="center",font=("Small Fonts",40,"normal"))
    
    score_rows = int(len(scores)/20 + 1)
                     
    d = 0
                     
    for i in range(score_rows):
        d = d + 1
        a = 180 - (d-1) * 20
        b = 0 + (d-1) * 20
        c = 19 + (d-1) * 20
        print (a,b,c,d)
        tex.goto(0,a)
        tex.write((scores[b:c]), True, align="center",font=("Small Fonts",14,"normal"))
    
    turtle.textinput("DICEGAME", "scoreboard")
    menu()

def Settings():
    global rounds
    global p1col
    global p2col
    global autoplay
    global texcol
    
    tex.clear()
    tex.goto(0,200)
    tex.write(("Settings"), True, align="center",font=("Small Fonts",50,"normal"))
    tex.goto (0,100)
    tex.write(("rounds: ",rounds), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto (0,50)
    tex.write(("P1colour: ",p1col), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto (0,0)
    tex.write(("P2colour: ",p2col), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto (0,-50)
    tex.write(("background:",tut.bgcolor()), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto (0,-100)
    tex.write(("text",texcol), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto (0,-250)
    tex.write(("autoplay:",autoplay), True, align="right",font=("Small Fonts",15,"normal"))
    
    SET = turtle.textinput("DICEGAME", "settings")
    if SET.lower().startswith("roun"):
        rounds = int(turtle.numinput("DICEGAME", "settings(rounds)",5,0,999))
    elif SET.lower().startswith("p1col"):
        col = turtle.textinput("DICEGAME", "settings(p1colour)")
        try:
            p1col = col
            Die.color("black",p1col)
        except turtle.TurtleGraphicsError:
            p1col = "maroon"
    elif SET.lower().startswith("p2col"):
        col = turtle.textinput("DICEGAME", "settings(p2colour)")
        try:
            p2col = col
            Die.color("black",p2col)
        except turtle.TurtleGraphicsError:
            p2col = "navy"
    elif SET.lower().startswith("back"):
        col = turtle.textinput("DICEGAME", "settings(background colour)")
        try:
            tut.bgcolor(col)
        except turtle.TurtleGraphicsError:
            tut.bgcolor("saddle brown")
    elif SET.lower().startswith("tex"):
        col = turtle.textinput("DICEGAME", "settings(text colour)")
        try:
            tex.color(col)
        except turtle.TurtleGraphicsError:
            tex.color("white")
    elif SET.lower().startswith("auto"):
        if autoplay == False:
            autoplay = True
        else:
            autoplay = False
    else:menu()
    Settings()
    

global rounds
rounds = 5
global p1col
p1col = "maroon"
global p2col
p2col = "navy"
global texcol
texcol = "white"
tex.color(texcol)
global autoplay
autoplay = False
global all_scores

scores = []
#global scores


#try:
#    with open("agtiwow_scores.txt",'r') as f:
#        print (f.closed())
#        for x in f:
#            print (f.closed())
#            x = x.replace('\n','')
#            scores.append(int(x))
#            f.close()
#            print (f.closed())
#    print ("reading successful")
#except:
#    print ("reading failed")
#    with open("agtiwow_scores.txt",'w') as f:
#        f.write("0\n0\n0\n0\n0")
#        f.close()
#        
#    with open("agtiwow_scores.txt",'r') as f:
#        for x in f:
#            x = x.replace('\n','')
#            scores.append(int(x))
#            f.close()
#scores.sort(reverse=True)
#print (scores)

try:
    with open("dicegame_scores.txt",'r') as f:
        for x in f:
            x = x.replace('\n','')
            scores.append(int(x))
        f.close()
    print("loading successful")
    tex.goto(0,0)
    tex.write(("loading successful"), True, align="center",font=("Small Fonts",40,"normal"))
    tex.clear()

except:
    print("loading failed")
    tex.goto(0,0)
    tex.write(("loading failed"), True, align="center",font=("Small Fonts",40,"normal"))
    tex.clear()
    with open("dicegame_scores.txt",'w') as f:
        f.write("0\n0\n0\n0\n0\n")
        f.close()
    with open("dicegame_scores.txt",'r') as f:
        for x in f:
            x = x.replace('\n','')
            scores.append(int(x))
        f.close()

try:
    with open("dicegame_totalscore.txt",'r') as f:
        all_scores = int(f.readline())
        f.close()
    print("additional loading successful")
    tex.goto(0,0)
    tex.write(("additional loading successful"), True, align="center",font=("Small Fonts",40,"normal"))
    tex.clear()

except:
    try:
        print("additional loading failed... copying")
        tex.goto(0,0)
        tex.write(("additional loading failed"), True, align="center",font=("Small Fonts",40,"normal"))
        tex.clear()
        all_scores = sum(scores)
        with open("dicegame_totalscore.txt",'w') as f:
            f.write (str(all_scores))
            f.close()
        print ("copying successful")
    except:
        print ("files catastrophic!")
        tex.goto(0,0)
        tex.write(("FILES CATASTROPHIC!"), True, align="center",font=("Small Fonts",40,"normal"))
        tex.clear()
        with open("dicegame_totalscore.txt",'w') as f:
            f.write("0")
            f.close()
            
if all_scores < sum(scores):
    all_scores = sum(scores)
    tex.goto(0,0)
    tex.write(("syncing scores"), True, align="center",font=("Small Fonts",40,"normal"))
    tex.clear()

def removezeros():
    if len(scores) >= 10:
        remove_zeros = 5
    else:
        remove_zeros = len(scores) - 5

    return(remove_zeros)
    
print (scores)
for i in range(removezeros()):
    scores.remove(0)
scores.sort(reverse=True)
print (scores)

if len(scores) > 500:
    for x in range(len(scores)-480):
        scores.pop()
menu()
