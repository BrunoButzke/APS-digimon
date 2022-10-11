import turtle


player1 = turtle.Turtle()
player2 = turtle.Turtle()
menu = turtle.Turtle()
info = turtle.Turtle()
action = turtle.Turtle()
hp = turtle.Turtle()
life = turtle.Turtle()
hp2 = turtle.Turtle()
life2 = turtle.Turtle()

text = "  JOGUE"

screen = turtle.Screen()
screen.setup(width=1040,height=570)
screen.bgpic("assets/field.gif")


menu_asset = 'assets/menu.gif'
hp_asset = 'assets/hp.gif'
gabumon = 'assets/gabumon.gif'
agumon = 'assets/agumon.gif'
turtle.register_shape(gabumon)
turtle.register_shape(agumon)
turtle.register_shape(menu_asset)
turtle.register_shape(hp_asset)



player1.shape(agumon)
player1.penup()
player1.speed(0)
player1.goto(-270,-150)
player1.speed(1)
player1.left(30)



player2.shape(gabumon)
player2.penup()
player2.speed(0)
player2.goto(250,80)
player2.speed(1)


menu.shape(menu_asset)
menu.penup()
menu.speed(0)
menu.goto(210,-230)
menu.speed(6)


life.penup()
life.speed(0)
life.goto(-360,50)
life.speed(6)
life.pendown()
life.color("red")
life.width(20)
life.forward(220)
life.hideturtle()
life.color("black")

hp.shape(hp_asset)
hp.penup()
hp.speed(0)
hp.goto(-270,50)
hp.speed(6)


life2.penup()
life2.speed(0)
life2.goto(160,250)
life2.speed(6)
life2.pendown()
life2.color("red")
life2.width(20)
life2.forward(220)
life2.hideturtle()
life2.color("black")

hp2.shape(hp_asset)
hp2.penup()
hp2.speed(0)
hp2.goto(250,250)
hp2.speed(6)




info.hideturtle()
info.penup()
info.speed(0)
info.goto(10,-245)
info.color('white')
info.write(text,font=('Arial', 18, 'bold'))

action.penup()
action.speed(0)
action.goto(250,-211)

def move_to_soft_attack():
    action.goto(250,-211)

def move_to_hard_attack():
    action.goto(250,-249)

def move_to_healing():
    action.goto(390,-211)

def confirm():
    player1.forward(30)
    player1.backward(30)
    info.clear()
    text = "AGUARDE"
    info.write(text,font=('Arial', 18, 'bold'))
    
        
screen.onkeypress(move_to_soft_attack, 'Left')
screen.onkeypress(move_to_soft_attack, 'Up')
screen.onkeypress(move_to_healing, 'Right')
screen.onkeypress(move_to_hard_attack, 'Down')
screen.onkeypress(confirm, 'space')

screen.listen()

screen.mainloop()

