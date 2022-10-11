import turtle

class userInterface():
    def __init__(self):
        self.text = "  JOGUE"
        self.player1 = turtle.Turtle()
        self.player2 = turtle.Turtle()
        self.innitializePlayers()
        self.menu = turtle.Turtle()
        self.innitializeMenu()
        self.info = turtle.Turtle()
        self.innitializeInfo()
        self.actionSelector = turtle.Turtle()
        self.innitializeActionSelector()
        self.hp = turtle.Turtle()
        self.life = turtle.Turtle()
        self.hp2 = turtle.Turtle()
        self.life2 = turtle.Turtle()
        self.innitializeLifeBars()
        self.mainLoopWindow()

        self.action_id = 1
        self.action_name = "Ataque Leve"

    def mainLoopWindow(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=1040,height=570)
        self.screen.bgpic("assets/field.gif")

        self.screen.onkeypress(self.move_to_soft_attack, 'Left')
        self.screen.onkeypress(self.move_to_soft_attack, 'Up')
        self.screen.onkeypress(self.move_to_healing, 'Right')
        self.screen.onkeypress(self.move_to_hard_attack, 'Down')
        self.screen.onkeypress(self.confirm, 'space')

        self.screen.listen()

        self.screen.mainloop()

    def innitializeLifeBars(self):
        hp_asset = 'assets/hp.gif'
        turtle.register_shape(hp_asset)

        self.life.penup()
        self.life.speed(0)
        self.life.goto(-360,50)
        self.life.speed(6)
        self.life.pendown()
        self.life.color("red")
        self.life.width(20)
        self.life.forward(220)
        self.life.hideturtle()
        self.life.color("black")

        self.hp.shape(hp_asset)
        self.hp.penup()
        self.hp.speed(0)
        self.hp.goto(-270,50)
        self.hp.speed(6)


        self.life2.penup()
        self.life2.speed(0)
        self.life2.goto(160,250)
        self.life2.speed(6)
        self.life2.pendown()
        self.life2.color("red")
        self.life2.width(20)
        self.life2.forward(220)
        self.life2.hideturtle()
        self.life2.color("black")

        self.hp2.shape(hp_asset)
        self.hp2.penup()
        self.hp2.speed(0)
        self.hp2.goto(250,250)
        self.hp2.speed(6)

    def innitializePlayers(self):
        agumon = 'assets/agumon.gif'
        turtle.register_shape(agumon)
        self.player1.shape(agumon)
        self.player1.penup()
        self.player1.speed(0)
        self.player1.goto(-270, -150)
        self.player1.speed(1)
        self.player1.left(30)

        gabumon = 'assets/gabumon.gif'
        turtle.register_shape(gabumon)
        self.player2.shape(gabumon)
        self.player2.penup()
        self.player2.speed(0)
        self.player2.goto(250,80)
        self.player2.speed(1)

    def innitializeMenu(self):
        menu_asset = 'assets/menu.gif'
        turtle.register_shape(menu_asset)
        self.menu.shape(menu_asset)
        self.menu.penup()
        self.menu.speed(0)
        self.menu.goto(210,-230)
        self.menu.speed(6)

    def innitializeInfo(self):
        self.info.hideturtle()
        self.info.penup()
        self.info.speed(0)
        self.info.goto(10,-245)
        self.info.color('white')
        self.info.write(self.text,font=('Arial', 18, 'bold'))

    def innitializeActionSelector(self):
        self.actionSelector.penup()
        self.actionSelector.speed(0)
        self.actionSelector.goto(250,-211)

    def move_to_soft_attack(self):
        self.actionSelector.goto(250,-211)
        self.action_id = 1
        self.action_name = "Ataque Leve"

    def move_to_hard_attack(self):
        self.actionSelector.goto(250,-249)
        self.action_id = 2
        self.action_name = "Ataque Pesado"

    def move_to_healing(self):
        self.actionSelector.goto(390,-211)
        self.action_id = 3
        self.action_name = "Regenerar"

    def confirm(self):
        self.player1.forward(30)
        self.player1.backward(30)
        self.info.clear()
        self.text = "Usou "
        self.info.write((self.text + self.action_name),font=('Arial', 18, 'bold'))
    
        
userInterface()

