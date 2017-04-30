import turtle

def triange(leng,time):
    for i in range(time):
        turtle.fd(leng)
        turtle.seth(120)
        turtle.fd(leng)
        turtle.seth(-120)
        turtle.fd(leng)

    
def main():
    turtle.setup(1400,800,0,0)   
    turtle.pensize(15)
    turtle.pencolor("red")
    turtle.seth(0)
    triange(410,1)

main()
