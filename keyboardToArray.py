from graphics import *
WINDOW_WIDTH,WINDOW_HEIGHT = 475, 475
win = GraphWin("5*5 Mosaic", WINDOW_WIDTH, WINDOW_HEIGHT)
c = 0
counter_text = Text(Point(250,25),"count : " + str(c))
counter_text.draw(win)

b1 = Rectangle(Point(50,50),Point(100,100))
b2 = Rectangle(Point(125,50),Point(175,100))
b3 = Rectangle(Point(200,50),Point(250,100))
b4 = Rectangle(Point(275,50),Point(325,100))
b5 = Rectangle(Point(350,50),Point(400,100))
b6 = Rectangle(Point(50,125),Point(100,175))
b7 = Rectangle(Point(125,125),Point(175,175))
b8 = Rectangle(Point(200,125),Point(250,175))
b9 = Rectangle(Point(275,125),Point(325,175))
b10 = Rectangle(Point(350,125),Point(400,175))
b11 = Rectangle(Point(50,200),Point(100,250))
b12 = Rectangle(Point(125,200),Point(175,250))
b13 = Rectangle(Point(200,200),Point(250,250))
b14 = Rectangle(Point(275,200),Point(325,250))
b15 = Rectangle(Point(350,200),Point(400,250))
b16 = Rectangle(Point(50,275),Point(100,325))
b17 = Rectangle(Point(125,275),Point(175,325))
b18 = Rectangle(Point(200,275),Point(250,325))
b19 = Rectangle(Point(275,275),Point(325,325))
b20 = Rectangle(Point(350,275),Point(400,325))
b21 = Rectangle(Point(50,350),Point(100,400))
b22 = Rectangle(Point(125,350),Point(175,400))
b23 = Rectangle(Point(200,350),Point(250,400))
b24 = Rectangle(Point(275,350),Point(325,400))
b25 = Rectangle(Point(350,350),Point(400,400))
submit = Rectangle(Point(400,420),Point(450,450))
submit.setFill("red")
text = Text(Point(425,435),"submit")
submit.draw(win)
text.draw(win)
b1.draw(win)
b2.draw(win)
b3.draw(win)
b4.draw(win)
b5.draw(win)
b6.draw(win)
b7.draw(win)
b8.draw(win)
b9.draw(win)
b10.draw(win)
b11.draw(win)
b12.draw(win)
b13.draw(win)
b14.draw(win)
b15.draw(win)
b16.draw(win)
b17.draw(win)
b18.draw(win)
b19.draw(win)
b20.draw(win)
b21.draw(win)
b22.draw(win)
b23.draw(win)
b24.draw(win)
b25.draw(win)
x = 0
y = 0
myRList=[[b1,b2,b3,b4,b5],[b6,b7,b8,b9,b10],[b11,b12,b13,b14,b15],[b16,b17,b18,b19,b20],[b21,b22,b23,b24,b25]]
def arrayMaking():
    myList=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    myRList=[[b1,b2,b3,b4,b5],[b6,b7,b8,b9,b10],[b11,b12,b13,b14,b15],[b16,b17,b18,b19,b20],[b21,b22,b23,b24,b25]]
    for x in range(5):
        for y in range(5):
            myList[x][y] =getColor((myRList[x][y]))
    return myList
def changeColor(rectangle):
    global c
    if rectangle.config["fill"] == "black":
        rectangle.setFill("") 
        c= c - 1
        counter_text.setText("count : "+ str(c))
    else:
        rectangle.setFill("black")
        c= c + 1
        counter_text.setText("count : " + str(c))
def getColor(rectangle):
    n = 0
    if rectangle.config["fill"] == "black":
        n = 1
    return n
def inside(point,rectangle):
    ll = rectangle.getP1()
    ur = rectangle.getP2()
    
    return ll.getX()< point.getX() < ur.getX() and ll.getY() < point.getY()< ur.getY()
while True:

    k = win.checkKey()

    if (k =='Left' and x > 0) :#move it to the left
        myRList[y][x].setOutline('black')
        x = x - 1
        print('x equal '+str(x))
        print('y equal '+ str(y))
    if(k == 'Left' and x == 0):
        x = x
        print('x equal '+str(x))
        print('y equal '+ str(y))
    if(k =='Right' and x <4 ):#move it to the right
        myRList[y][x].setOutline('black')
        x = x + 1
        print('x equal '+str(x))
        print('y equal '+ str(y))
    if(k == 'Right' and x == 4):
        x = x
        print('x equal '+str(x))
        print('y equal '+ str(y))
    if (k =='Up' and y > 0 ) :#move it to the left
        myRList[y][x].setOutline('black')
        y = y - 1
        print('x equal '+str(x))
        print('y equal '+ str(y))
    if(k == 'Down' and y == 4):
        y = y
        print('x equal '+str(x))
        print('y equal '+ str(y))
    if(k =='Down' and y < 4):#move it to the right
        myRList[y][x].setOutline('black')
        y = y + 1
        print('x equal '+str(x))
        print('y equal '+ str(y))
    if(k == 'Up' and y == 0):
        y = y
        print('x equal '+str(x))
        print('y equal '+ str(y))
    myRList[y][x].setOutline('blue')
    if(k == 'space'):
        changeColor(myRList[y][x])
    if(k == 'o'):
        break
arrayMaking()
print(arrayMaking())
