from turtle import *

shape("turtle")

speed(1)

# repeat:draw square and turm left
for i in range(2):
    
    for j in range(4):
        forward(100)
        left(90)
    left(30)
mainloop()