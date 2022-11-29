import turtle as t1
t=t1.Turtle()
s=t1.Screen()
t1.color("white")
t1.write("")
s.bgcolor('black')
t.speed(0)
col=("pink", "red","white","green","cyan","yellow")
for i in range(1,1000):
       t.pencolor(col[i%6])
       t.circle(150-i/2,150)
       
       t.lt(90)
       t.circle(120-i/3,20)

t.It(120)
s.exitonclick()
