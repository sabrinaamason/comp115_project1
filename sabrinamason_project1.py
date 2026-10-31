import turtle
import random


'''setting up window'''
wn = turtle.Screen()
wn.colormode(255)
wn.screensize(500, 500)
wn.bgcolor(255, 202, 128)


'''creating turtle pen shapes'''
leaf_shape_s= ((0.7071067811865476, -0.7071067811865476), (3.7071067811865483, -0.7071067811865476), (2.175017894948592, 0.5784684381865316), (6.031743553067829, 5.174735096900401), (1.333280449138286, 3.4646343802720567), (1.333280449138286, 7.464634380272058), (0.6261736679517382, 6.75752759908551), (0.10853557774669642, 8.689379251663647), (-0.4091025124583447, 6.75752759908551), (-1.1162092936448924, 7.464634380272057), (-1.1162092936448913, 3.4646343802720567), (-5.814672397574434, 5.174735096900399), (-1.9579467394551955, 0.5784684381865315), (-3.4900356256931513, -0.7071067811865479), (-0.4900356256931513, -0.7071067811865475), (0.21707115549339617, 2.220446049250313e-16))

turtle.register_shape('leafish_s', leaf_shape_s)

leaf_shape_m = ([2.121320343559643, -2.121320343559643], [11.121320343559645, -2.121320343559643], [6.525053684845776, 1.7354053145595945], [18.095230659203487, 15.5242052907012], [3.9998413474148578, 10.393903140816168], [3.9998413474148578, 22.39390314081617], [1.878521003855215, 20.27258279725653], [0.3256067332400896, 26.06813775499094], [-1.227307537375034, 20.27258279725653], [-3.3486278809346772, 22.39390314081617], [-3.348627880934674, 10.393903140816171], [-17.4440171927233, 15.524205290701197], [-5.8738402183655865, 1.7354053145595945], [-10.470106877079454, -2.1213203435596437], [-1.4701068770794539, -2.1213203435596424], [0.6512134664801885, 4.440892098500626e-16])

turtle.register_shape('leafish_m', leaf_shape_m)

leaf_shape_l = ([2.8284271247461903, -2.8284271247461903], [14.828427124746193, -2.8284271247461903], [11.76424935227028, -0.25727668600003195], [27.19115198474723, 18.127789948855444], [8.397299569029055, 11.287387082342068], [8.397299569029055, 27.28738708234207], [5.5688724442828645, 24.45895995759588], [3.4983200834626973, 32.18636656790843], [1.4277677226425327, 24.45895995759588], [-1.4006594021036585, 27.287387082342068], [-1.400659402103654, 11.287387082342068], [-20.194511817821823, 18.127789948855437], [-4.76760918534487, -0.25727668600003284], [-10.895964730296694, -5.39957756349235], [1.1040352697033065, -5.399577563492349], [3.9324623944494963, -2.571150438746158])

turtle.register_shape('leafish_l', leaf_shape_l)

leaf_shape_xl = ([3.5355339059327378, -3.5355339059327378], [18.53553390593274, -3.5355339059327378], [14.705311690337851, -0.3215958575000397], [33.988939980934035, 22.659737436069303], [10.49662446128632, 14.109233852927584], [10.49662446128632, 34.10923385292759], [6.961090555353581, 30.57369994699485], [4.372900104328372, 40.23295820988553], [1.7847096533031666, 30.573699946994846], [-1.7508242526295725, 34.10923385292758], [-1.750824252629567, 14.10923385292758], [-25.24313977227728, 22.659737436069292], [-5.959511481681091, -0.3215958575000428], [-13.61995591287087, -6.74947195436544], [1.3800440871291304, -6.749471954365437], [4.915577993061868, -3.2139380484326985])

turtle.register_shape('leafish_xl', leaf_shape_xl)



'''                It's functioning time                '''

def ground_fill(pens,y_start):
    '''Makes an ombre ground'''
    pens.shape('arrow')
    pens.penup()
    pens.goto(-390, y_start)
    pens.setheading(15)
    pens.pendown()
    pens.circle(-400,31)
    pens.circle(500, 11)
    pens.circle(-750, 16)
    pens.left(45)
    pens.circle(-900, 20)
    pens.shape('blank')

'''Drawing Trees'''
def draw_tree(pen,instructions,length):
    '''This function is used to draw the trees'''
    cmdlist = []
    for cmd in instructions:
        if cmd == 'F':
            pen.forward(length)
        elif cmd == 'B':
            pen.backward(length)
        elif cmd == '+':
            pen.right(10)
        elif cmd == '-':
            pen.left(10)
        elif cmd =='[':
            cmdlist.append([pen.heading(), pen.xcor(),pen.ycor()])
            print(cmdlist)
        elif cmd ==']':
            newinfo = cmdlist.pop()
            pen.setheading(newinfo[0])
            pen.setposition(newinfo[1],newinfo[2])

def leaf_confetti(pen, pen_shape, leaf_per_colour, ymax, ymin, y_inup, y_inlow, xmax, xmin, x_inup, x_inlow):
    '''This function stamps leaf prints within the given area'''
    pen.shape(pen_shape)
    leaf_colours = [(255, 0, 5), (255,29,0), (255,114,0), (255,172,0), (255,241,0)]
    for colour in leaf_colours:
        pen.color(colour)
        for _ in range(leaf_per_colour):
            y = random.randrange(ymin,ymax)
            if y > y_inup or y < y_inlow:
                x = random.randrange(x_inlow,x_inup)
            else:
                x = random.randrange(xmin,xmax)
            pen.up()
            pen.setheading(random.randrange(0,360))
            pen.goto(x, y)
            pen.down()
            pen.stamp()



'''                Let's Get Down to Drawing                '''

'''Good morning, the Sun is just rising now (drawing the sun/sky)'''
sky = turtle.Turtle()
increment = 45
sky.speed(0)
sky.pensize(50)
radius = 160
colours = [(255,154,114),(255,185,115), (255,219,119), (255,242,123), (255,255,137), (255,255,163),(255,255,195),(255,255,214), (254,255,245), (236,255,252), (210,253,255), (190,237,255) ,(179,226,255), (148,213,255), (130,200,255),(120,195,255)]
sky.up()
sky.goto(120+160,-170-160)
for colour in colours:
    sky.left(90)
    sky.down()
    sky.color(colour)
    sky.circle(radius)
    sky.up()
    sky.right(90)
    sky.forward(increment)
    radius += increment

sun = turtle.Turtle()
sun.up()
sun.color(255,245,175)
sun.left(90)
sun.goto(135,-170)
sun.begin_fill()
sun.circle(15)
sun.end_fill()
sun.shape('blank')


'''drawing the ground'''
R = 100
G = 66
ground = turtle.Turtle()
ground.color(R,G,0)
ground.speed(0)
ground.pensize(15)
y = -250

ground.penup()          # i know this next portion is a bit repeaty of the ground_fill function, but it was the only way that i could get it to work once my head started to hurt
ground.goto(-390, y)
ground.setheading(15)
ground.pendown()
ground.begin_fill()
ground.circle(-400,31)
ground.circle(500, 11)
ground.circle(-750, 16)
ground.left(45)
ground.circle(-900, 20)
ground.setheading(-90)
ground.forward(250)
ground.right(90)
ground.forward(825)
ground.end_fill()

for _ in range(15):
    ground.color(R,G,0)
    ground_fill(ground,y)
    y += 10
    R += 6
    G += 4


'''Drawing some trees with their leaves'''
tree1_instruction = 'FFFF[---FFFF[++FFBB]BB[+++FFFBBB]BB]  +FFF[++FF[-FFBB]BB[--FB]]  -FFFF[---FFB[++++FF]]BB[---FF]'
tree2_instruction = 'FFFF[----FF[+++FF]]  +FF[+++FFF[---FFB[+++F[--F]]]]  --FFFF[++++FFF[---FFF]]  F[----FF[++++FFFFB[----F[++FF]]]]  +FFFFFFFFBBB[+++F[--F]]' 
tree3_instruction = 'FFF[----FF[+++FFB[---F[++++F]]]]  F[++++FF[---F[++++F[---FF]]F]]  -F[---F[++F]]  FF[-----FF[+++F][+++++F]]  +F[+++F[--F]]  F  -F+FF'

leaf = turtle.Turtle()
leaf.speed(0)

tree = turtle.Turtle()
tree.color(177,149,103)
tree.speed(0)
tree.left(90)

'''   Tree 1   '''
tree.pensize(3)
tree.up()
tree.setposition(-360,-115)
tree.down()
draw_tree(tree,tree2_instruction,10)
'''Tree 1 leaf coverage'''
leaf_confetti(leaf,'leafish_s',17, 85, -60, 30,-30,-320,-385,-340,-383)

'''   Tree 2   '''
tree.up()
tree.setposition(-80,-210)
tree.pensize(5)
tree.down()
draw_tree(tree,tree3_instruction,45)
'''Tree 2 leaf coverage'''
leaf_confetti(leaf,'leafish_m',25,325,-10,200,50,75,-215,-10,-150)

'''   Tree 3   '''
tree.up()
tree.setposition(235,-240)
tree.pensize(3)
tree.down()
draw_tree(tree,tree1_instruction,10)
'''Tree 3 leaf coverage'''
leaf_confetti(leaf,'leafish_s',13, -90,-165,-105,-150,265,200,250,220)

'''   Tree 4   '''
tree.up()
tree.setposition(-260,-350)
tree.pensize(9)
tree.down()
draw_tree(tree,tree1_instruction,45)
'''Tree 4 leaf coverage'''
leaf_confetti(leaf, 'leafish_l', 17, 275,-85,220,-50,-145,-380,-200,-300)

'''   Tree 5   '''
tree.up()
tree.setposition(360,-350)
tree.pensize(11)
tree.down()
draw_tree(tree,tree3_instruction,45)
'''Tree 5 leaf coverage'''
leaf_confetti(leaf,'leafish_l', 17,240,-180,120,-125,386,210,385,285)

'''   Tree 6   '''
tree.up()
tree.setposition(0,-700)
tree.pensize(7)
tree.down()
draw_tree(tree,tree2_instruction,30)
tree.shape('blank')

'''Tree 6 leaf coverage'''
leaf_confetti(leaf,'leafish_xl',7,-120,-400,-200,-315,50,-150,-45,-100)



wn.exitonclick()