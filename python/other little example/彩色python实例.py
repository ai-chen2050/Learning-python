import turtle

def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.pencolor("red")
        turtle.circle(-rad,angle)
        turtle.pencolor("yellow")
    turtle.circle(rad,angle/2)
    turtle.fd(rad)    #   .fd()==.forward()
    turtle.pencolor("purple")
    for i in range(2):
        turtle.left(90)
        turtle.circle(-40,180)
        turtle.left(90)
        #turtle.fd(80)
    turtle.circle(50,180)
    turtle.circle(-50,180)
    turtle.pencolor("pink")
    turtle.circle(-20,85)
    

def main():
    turtle.setup(1400,800,0,0)
    pythonsize=30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")

    turtle.penup()
    turtle.goto(-360,0)
    turtle.pendown()
    turtle.seth(-90)    #  .seth为角度值
    drawSnake(60,180,2,pythonsize/2)

main()
