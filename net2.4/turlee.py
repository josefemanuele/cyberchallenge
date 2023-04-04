import turtle


with open('draw.txt') as file:
    turtle.pen(fillcolor="white", pencolor="red", pensize="2")
    for line in file.readlines():
        command = line.strip().split(',')
        start = (int(command[3]), int(command[4]))
        end = (int(command[5]), int(command[6]))
        turtle.penup()
        turtle.goto(start)
        turtle.pendown()
        turtle.goto(end)

    turtle.hideturtle()
    turtle.exitonclick()
