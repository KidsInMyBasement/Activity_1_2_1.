#----- intro -----

# coded by me :)

#-----import statements-----
import turtle as trtl
import random as ran
import time 

#-----countdown variables-----
font_setup = ("italic", 20, "bold")
timer = 15
preview_timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
start_game = False
movement_motion = False
scorex = 0
gameover = False

#-----countdown writer-----

counter =  trtl.Turtle()
player = trtl.Turtle()

#-----game functions-----

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("{Time's up.}", font=font_setup)
    counter.clear()
    timer_up = True
  else:
    counter.write('Seconds left: ' + str(timer), font=font_setup,align='center')
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def startup():
  global preview_timer, timer_up, start_game
  counter.clear()
  if preview_timer <=0:
    wn.ontimer(countdown, counter_interval) 
    layout()
    counter.write('<- Start ->',font=font_setup,align='center')
    counter.clear()
  else:
    counter.write("Aim 'n Tap [Click on the squares & aim for accuracy] - " + str(preview_timer), font=font_setup,align='center')
    preview_timer -=1
    counter.getscreen().ontimer(startup,counter_interval)

def pauseMovement():
  global movement_motion
  movement_motion = False

def layout():
  global timer_up, gameover 
  player.hideturtle()
  player.shape("square")
  colorlist = ['red','green','blue','orange','yellow']
  def score_player(x,y):
    global scorex
    scorex +=1 
    print("Gamescore:",scorex)

  # player.color(ran.randint(1,100),ran.randint(1,100),ran.randint(1,100))
  for num in range(0,timer*counter_interval,1):
    player.shapesize(ran.randint(1,3))
    player.color(colorlist[ran.randint(0,4)])
    num = 50
    x = ran.randint(-350,350)
    y = ran.randint(-350,350)
    player.penup()
    player.goto(x,y)
    if num >= 0 and num <= 10:
      player.penup()
    player.pendown()
    player.showturtle()
    while (num>0):
      player.goto(x,y)
      num = num - 1
    player.speed(0)
    player.hideturtle()
    player.onclick(score_player)
    # wn.onclick(cxr)
    if timer_up == True:
      player.clear
      counter.clear
      player.hideturtle()
      counter.isvisible()
      counter.write("Score: " + str(scorex), font=font_setup,align='center')
      time.sleep(3)
      counter.clear
      gameover = True
      print("Thank you for playing!")
      wn.bye()
      break

#---------events---------

wn = trtl.Screen()
wn.ontimer(startup, counter_interval)

#-----backend processing -----

wn.bgcolor('#FFCCE5')

# ---other---

# - end/loop - 

wn.mainloop()
