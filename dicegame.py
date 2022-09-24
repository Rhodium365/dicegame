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
    Die.up()
    Die.goto(-50,-200)
    diedelete()
    Die.goto(-260,-200)
    Die.seth(0)
    dice1 = random.randint(1,6) #first dice
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
    dice2 = random.randint(1,6) #second dice
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
    if (dice1 + dice2)%2 ==0: #if the total is even add 10 to the total
        P1total=P1total+10
        tex.goto(0,-50)
        tex.write(("EVEN!(+10)"), True, align="center",font=("Small Fonts",20,"normal"))
    else: #if the total is odd deduct 10 from the total
        P1total=P1total-5
        tex.goto(0,-50)
        tex.write(("ODD!(-5)"), True, align="center",font=("Small Fonts",20,"normal"))
    if dice1 ==  dice2: # if both dice are the same roll a third dice
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
    
    P1total = P1total + (dice1+dice2+dice3)
    if P1total < 0: #dont let total go below 0
        P1total = P1total - P1total

def rolP2():
    global P2total
    dice3 = 0
    Die.up
    Die.goto(-50,200)
    diedelete()
    Die.goto(-260,200)
    Die.seth(0)
    dice1 = random.randint(1,6) #first dice
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
    dice2 = random.randint(1,6) #second dice
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
    if (dice1 + dice2)%2 ==0: #if your total is even add 10 to total
        P2total=P2total+10
        tex.goto(0,100)
        tex.write(("EVEN!(+10)"), True, align="center",font=("Small Fonts",20,"normal"))
    else:   # if your total is odd deduct 5 points 
        P2total=P2total-5
        tex.goto(0,100)
        tex.write(("ODD!(-5)"), True, align="center",font=("Small Fonts",20,"normal"))
    if dice1 ==  dice2: #if both dice are the same roll a third dice
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
    P2total = P2total + (dice1+dice2)
    if P2total < 0: #dont let the total go below 0
        P2total = P2total - P2total



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

def rnd():
    global autoplay
    if autoplay == False:
        turtle.textinput("DICEGAME", "P1 roll")
    else:
        tex.speed(0)
    tex.clear()
    Die.clear()
    rolP1()

    if autoplay == False:
        turtle.textinput("DICEGAME", "P2 roll")
    rolP2()
    
    tex.goto(0,0)
    tex.write(("Player1 total =" + str(P1total)), True, align="center",font=("Small Fonts",20,"normal"))
    tex.goto(0,50)
    tex.write(("Player2 total =" + str(P2total)), True, align="center",font=("Small Fonts",20,"normal"))



def game():
    global closing
    if closing == True:
        return
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
        tex.write(("P1 total =" + str(P1total)), True, align="center",font=("Small Fonts",30,"normal"))
        tex.goto(0,-40)
        tex.write(("P2 total =" + str(P2total)), True, align="center",font=("Small Fonts",30,"normal"))
    elif P2total > P1total:
        tex.goto(0,50)
        tex.write(("P2 WINS!"), True, align="center",font=("Small Fonts",40,"normal"))
        tex.goto(0,0)
        tex.write(("P1 total =" + str(P1total)), True, align="center",font=("Small Fonts",30,"normal"))
        tex.goto(0,-40)
        tex.write(("P2 total =" + str(P2total)), True, align="center",font=("Small Fonts",30,"normal"))
    else:
        tex.goto(0,50)
        tex.write(("SUDDEN DEATH! Tied: "), True, align="center",font=("Small Fonts",50,"normal"))
        tex.goto(0,0)
        tex.write(("Tied: " + str(P1total)), True, align="center",font=("Small Fonts",30,"normal"))
        suddendeath()
    all_scores = all_scores + P1total + P2total
    with open("dicegame_totalscore.txt",'w') as f:
        f.write (str(all_scores))
        f.close()
        
    if rounds <= 5: #only games with less than 5 rounds will be saved
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
        tex.write(("P1 total =" + str(P1total)), True, align="center",font=("Small Fonts",30,"normal"))
        tex.goto(0,-40)
        tex.write(("P2 total =" + str(P2total)), True, align="center",font=("Small Fonts",30,"normal"))
    elif P2total > P1total:
        tex.goto(0,50)
        tex.write(("P2 WINS!"), True, align="center",font=("Small Fonts",40,"normal"))
        tex.goto(0,0)
        tex.write(("P1 total =" + str(P1total)), True, align="center",font=("Small Fonts",30,"normal"))
        tex.goto(0,-40)
        tex.write((" P2 total =" + str(P2total)), True, align="center",font=("Small Fonts",30,"normal"))
    else:
        tex.goto(0,50)
        tex.write(("SUDDEN DEATH! Tied: "), True, align="center",font=("Small Fonts",50,"normal"))
        tex.goto(0,0)
        tex.write(("Tied: ",P1total), True, align="center",font=("Small Fonts",30,"normal"))
        suddendeath()
    turtle.textinput("DICEGAME", "end game")



def menu():
    global closing
    if closing == True:
        return
    global all_scores
    tex.clear()
    Die.clear()
    
    tex.speed(10)
    tex.goto(0,200)
    tex.write(("DICEGAME"), True, align="center",font=("Small Fonts",50,"normal"))
    tex.goto(0,150)
    tex.write(("#1: {}".format(scores[0])), True, align="center",font=("Small Fonts",20,"normal"))
    tex.goto(0,120)
    tex.write(("#2: {}".format(scores[1])), True, align="center",font=("Small Fonts",20,"normal"))
    tex.goto(0,90)
    tex.write(("#3: {}".format(scores[2])), True, align="center",font=("Small Fonts",20,"normal"))
    tex.goto(0,60)
    tex.write(("#4: {}".format(scores[3])), True, align="center",font=("Small Fonts",20,"normal"))
    tex.goto(0,30)
    tex.write(("#5: {}".format(scores[4])), True, align="center",font=("Small Fonts",20,"normal"))
    tex.goto(0,-5)
    tex.write(("TOTAL: {}".format(all_scores)), True, align="center",font=("Small Fonts",23,"normal"))

    tex.goto(-100,-50)
    tex.write(("SETTINGS"), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto(100,-50)
    tex.write(("SCORES"), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto(0,-110)
    tex.write(("START"), True, align="center",font=("Small Fonts",40,"normal"))
    tex.goto(0,-160)
    tex.write(("QUIT"), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto(0,-210)
    tex.write(("ver: {}\ndicegame by Cuchulainn Moon (Rhodium365)".format("1.1.0")), True, align="center",font=("Small Fonts",10,"normal"))
    hub = turtle.textinput("DICEGAME", "menu")              #put version here^^^
    if hub == None:
        hub = ""
    if hub.lower().startswith("set"):
        Settings()
    elif hub.lower() == "exit" or hub.lower() == "quit" or hub.lower().startswith("clos"):
        closing = True
        
    elif hub.lower().startswith("star"):
        game()
    elif hub.lower().startswith("scor"):
        scoreboard()
    else:
        menu()

def scoreboard():
    global closing
    if closing == True:
        return
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
        tex.goto(0,a)
        tex.write((scores[b:c]), True, align="center",font=("Small Fonts",14,"normal"))
    
    turtle.textinput("DICEGAME", "scoreboard")
    menu()

def Settings():
    global closing
    if closing == True:
        return
    global rounds
    global p1col
    global p2col
    global autoplay
    global texcol
    global bgcol
    
    tex.clear()
    tex.goto(0,200)
    tex.write(("Settings"), True, align="center",font=("Small Fonts",50,"normal"))
    tex.goto (0,100)
    tex.write(("rounds: {}".format(rounds)), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto (0,50)
    tex.write(("P1colour: {}".format(p1col)), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto (0,0)
    tex.write(("P2colour: {}".format(p2col)), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto (0,-50)
    tex.write(("background: {}".format(tut.bgcolor())), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto (0,-100)
    tex.write(("text: {}".format(texcol)), True, align="center",font=("Small Fonts",30,"normal"))
    tex.goto (-200,-250)
    tex.write(("autoplay: {}".format(autoplay)), True, align="center",font=("Small Fonts",15,"normal"))
    tex.goto (0,-250)
    tex.write(("default"), True, align="center",font=("Small Fonts",15,"normal"))
    tex.goto (200,-250)
    tex.write(("save"), True, align="center",font=("Small Fonts",15,"normal"))
    
    SET = turtle.textinput("DICEGAME", "settings")
    if SET == None:
        SET = ""
    if SET.lower().startswith("rou"):
        try:
            rounds = int(turtle.numinput("DICEGAME", "settings(rounds)",5,0,999))
        except:
            rounds = 5
    elif SET.lower().startswith("p1"):
        col = turtle.textinput("DICEGAME", "settings(p1colour)")
        if col == None:
            col = "maroon"
        try:
            p1col = col
            Die.color("black",p1col)
        except turtle.TurtleGraphicsError:
            p1col = "maroon"
    elif SET.lower().startswith("p2"):
        col = turtle.textinput("DICEGAME", "settings(p2colour)")
        if col == None:
            col = "navy"
        try:
            p2col = col
            Die.color("black",p2col)
        except turtle.TurtleGraphicsError:
            p2col = "navy"
    elif SET.lower().startswith("bac"):
        col = turtle.textinput("DICEGAME", "settings(background colour)")
        if col == None:
            col = "saddle brown"
        try:
            tut.bgcolor(col)
            bgcol = col
        except turtle.TurtleGraphicsError:
            tut.bgcolor("saddle brown")
            bgcol = "saddle brown"
    elif SET.lower().startswith("tex"):
        col = turtle.textinput("DICEGAME", "settings(text colour)")
        if col == None:
            col = "white"
        try:
            tex.color(col)
            texcol = col
        except turtle.TurtleGraphicsError:
            tex.color("white")
            texcol = "white"
    elif SET.lower().startswith("aut"):
        if autoplay == False:
            autoplay = True
        else:
            autoplay = False
    elif SET.lower().startswith("def"):
        rounds,p1col,p2col,autoplay,bgcol,texcol = 5,"maroon","navy",False,"saddle brown","white"
        Die.color("black",p1col)
        Die.color("black",p2col)
        tut.bgcolor("saddle brown")
        tex.color("white")
    elif SET.lower().startswith("sav"):
        tex.clear()
        tex.goto(0,0)
        tex.write(("Saving Settings..."), True, align="center",font=("Small Fonts",40,"normal"))
        with open("dicegame_settings.txt",'w') as f:
            f.write("{}\n{}\n{}\n{}\n{}\n{}".format(str(rounds),p1col,p2col,str(int(autoplay)),bgcol,texcol))
            f.close()
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


#load saved data
scores = []
try:
    tex.goto(0,0)
    tex.write(("Loading Saved Data..."), True, align="center",font=("Small Fonts",40,"normal"))
    with open("dicegame_scores.txt",'r') as f:
        for x in f:
            x = x.replace('\n','')
            scores.append(int(x))
        f.close()
    tex.clear()
    tex.goto(0,0)
    tex.write(("Loading Successful!"), True, align="center",font=("Small Fonts",40,"normal"))

except:
    tex.clear()
    tex.goto(0,0)
    tex.write(("No Saved Data! Creating File..."), True, align="center",font=("Small Fonts",40,"normal"))
    with open("dicegame_scores.txt",'w') as f:
        f.write("0\n0\n0\n0\n0\n")
        f.close()
    with open("dicegame_scores.txt",'r') as f:
        for x in f:
            x = x.replace('\n','')
            scores.append(int(x))
        f.close()
    tex.clear()
    tex.write(("File Created!"), True, align="center",font=("Small Fonts",40,"normal"))

try:
    tex.clear()
    tex.goto(0,0)
    tex.write(("Loading Additonal Data..."), True, align="center",font=("Small Fonts",40,"normal"))
    with open("dicegame_totalscore.txt",'r') as f:
        all_scores = int(f.readline())
        f.close()
    tex.clear()
    tex.goto(0,0)
    tex.write(("Loading Successful!"), True, align="center",font=("Small Fonts",40,"normal"))

except:
    try:
        tex.clear()
        tex.goto(0,0)
        tex.write(("No Data Found! Syncing..."), True, align="center",font=("Small Fonts",40,"normal"))
        all_scores = sum(scores)
        with open("dicegame_totalscore.txt",'w') as f:
            f.write (str(all_scores))
            f.close()
        tex.clear()
        tex.goto(0,0)
        tex.write(("Data Synced!"), True, align="center",font=("Small Fonts",40,"normal"))
    except:
        tex.clear()
        tex.goto(0,0)
        tex.write(("How Did You Get Here?"), True, align="center",font=("Small Fonts",40,"normal")) #nearly impossible to get to
        with open("dicegame_totalscore.txt",'w') as f:
            f.write("0")
            f.close()

tex.clear()    
if all_scores < sum(scores):
    tex.goto(0,0)
    tex.write(("Data Illogical! Syncing..."), True, align="center",font=("Small Fonts",40,"normal"))
    all_scores = sum(scores)
    tex.clear()

def removezeros():
    if len(scores) >= 10:
        remove_zeros = 5
    else:
        remove_zeros = len(scores) - 5

    return(remove_zeros)
    
for i in range(removezeros()):
    scores.remove(0)
scores.sort(reverse=True)

if len(scores) > 500:
    for x in range(len(scores)-480):
        scores.pop()


#load settings
global dset
dset = [5,"maroon","navy",0,"saddle brown","white"]
global pset
try:
    tex.clear()
    tex.goto(0,0)
    tex.write(("Loading Settings..."), True, align="center",font=("Small Fonts",40,"normal"))
    with open("dicegame_settings.txt",'r') as f:
        pset = f.read()
        f.close()
    tex.clear()
    tex.goto(0,0)
    tex.write(("Loading Successful!"), True, align="center",font=("Small Fonts",40,"normal"))

except:
    tex.clear()
    tex.goto(0,0)
    tex.write(("Saving Default Settings..."), True, align="center",font=("Small Fonts",40,"normal"))
    with open("dicegame_settings.txt",'w') as f:
        f.write("5\nmaroon\nnavy\n0\nsaddle brown\nwhite")
        f.close()
    with open("dicegame_settings.txt",'r') as f:
        pset = f.read()
        f.close()
    tex.clear()
    tex.goto(0,0)
    tex.write(("Default Settings Saved!"), True, align="center",font=("Small Fonts",40,"normal"))

pset = pset.split("\n")
pset = [int(pset[0]),str(pset[1]),str(pset[2]),bool(int(pset[3])),str(pset[4]),str(pset[5])]

global bgcol
autoplay = pset[3]
bgcol = pset[4]
tut.bgcolor(pset[4])
rounds = pset[0]
p1col = pset[1]
p2col = pset[2]
texcol = pset[5]
tex.color(pset[5])
global closing
closing = False
menu()
turtle.bye()
