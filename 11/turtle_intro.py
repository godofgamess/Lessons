import turtle


W_WIDTH = turtle.window_width()
W_HEIGHT = turtle.window_height()

# Создать черепашку
vadim = turtle.Turtle()

# Настроить черепашку
vadim.color('green')
vadim.shape('turtle')
vadim.turtlesize(1)
vadim.pensize(3)
vadim.speed(3)


vadim.penup()
vadim.goto(-W_WIDTH / 2, -W_HEIGHT / 2 )

vadim.pendown()
vadim.forward(W_WIDTH )
vadim.left(90)
vadim.forward(W_HEIGHT ) 
vadim.left(90)
vadim.forward(W_WIDTH )
vadim.left(90)
vadim.forward(W_HEIGHT )

vadim.penup()
vadim.home()
