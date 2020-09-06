import turtle

doagain = "Yes"
while doagain == "Yes":
    sides = int(input("How Many Sides You Want"))

    polygon = turtle.Turtle()
    polygon.color("green")
    polygon.pensize(4)

    for i in range(sides):
        polygon.reset()
        turn = 360/sides
        polygon.forward(100)
        polygon.left(turn)

    doagain = str(input("Do You Want To Do Again?"))
    
