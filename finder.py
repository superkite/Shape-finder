from math import *
x1 = 0
y1 = 0

x2 = 0
y2 = 4

x3 = 4
y3 = 4

x4 = 4
y4 = 0

if #Error clauses go here
    print("Undefined")
else:
    mAB = (y2 - y1)/(x2 - x1)
    mBC = (y3 - y2)/(x3 - x2)
    mCD = (y4 - y3)/(x4 - x3)
    mDA = (y1 - y4)/(x1 - x4)

    lAB = sqrt((x2 - x1)**2 + (y2 - y1)**2) #Find some error clauses
    lBC = sqrt((x3 - x2)**2 + (y3 - y2)**2)
    lCD = sqrt((x4 - x3)**2 + (y4 - y3)**2)
    lDA = sqrt((x1 - x4)**2 + (y1 - y4)**2)
    
    dAC = sqrt((x3 - x1)**2 + (y3 - y1)**2)
    dBD = sqrt((x4 - x2)**2 + (y4 - y2)**2)

    if mAB == mCD and mBC == mDA:
        if mAB == mBC == mCD == mDA:
            if lAB == lBC == lCD == lDA:
                if dAC != dBD:
                    print("It's a Rhombus")
                else:
                    print("It's a Square")
            else:
                print("It's a Rectangle")
        else:
            print("It's a Parallelogram")
    elif mAB != mCD and mBC == mDA or mBC != mDA and mAB == mCD:
        print("It's a Trapezoid")
    elif lAB == lBC and lCD == lDA:
        print("It's a Kite")
    else:
        print("It's a Quadrilateral")
