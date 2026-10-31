import turtle

wn = turtle.Screen()


leaf = turtle.Turtle()

leaf.speed(0)
# draw_leaf(leaf,leaf_instruction,20)
cmdlist = []
s=5

leaf.begin_fill()
leaf.right(45)
leaf.forward(1*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.left(45)
leaf.forward(3*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.left(140)
leaf.forward(1*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.right(90)
leaf.forward(6*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.left(150)
leaf.forward(5*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.right(110)
leaf.forward(4*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.left(135)
leaf.forward(1*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.right(120)
leaf.forward(2*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.left(150)
leaf.forward(2*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.right(120)
leaf.forward(1*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.left(135)
leaf.forward(4*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.right(110)
leaf.forward(5*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.left(150)
leaf.forward(6*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.right(90)
leaf.forward(2*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.left(140)
leaf.forward(3*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.left(45)
leaf.forward(1*s)
cmdlist.append([leaf.xcor(), leaf.ycor()])
leaf.end_fill()


print(cmdlist)


leaf_shape_s= ((0.7071067811865476, -0.7071067811865476), (3.7071067811865483, -0.7071067811865476), (2.175017894948592, 0.5784684381865316), (6.031743553067829, 5.174735096900401), (1.333280449138286, 3.4646343802720567), (1.333280449138286, 7.464634380272058), (0.6261736679517382, 6.75752759908551), (0.10853557774669642, 8.689379251663647), (-0.4091025124583447, 6.75752759908551), (-1.1162092936448924, 7.464634380272057), (-1.1162092936448913, 3.4646343802720567), (-5.814672397574434, 5.174735096900399), (-1.9579467394551955, 0.5784684381865315), (-3.4900356256931513, -0.7071067811865479), (-0.4900356256931513, -0.7071067811865475), (0.21707115549339617, 2.220446049250313e-16))

turtle.register_shape('leafish_s', leaf_shape_s)

leaf_shape_m = ([1.4142135623730951, -1.4142135623730951], [7.414213562373097, -1.4142135623730951], [5.88212467613514, -0.12863834300001598], [13.595575992373615, 9.063894974427722], [4.198649784514528, 5.643693541171034], [4.198649784514528, 13.643693541171036], [2.7844362221414323, 12.22947997879794], [1.7491600417313486, 16.093183283954215], [0.7138838613212664, 12.22947997879794], [-0.7003297010518292, 13.643693541171034], [-0.700329701051827, 5.643693541171034], [-10.097255908910912, 9.063894974427718], [-2.383804592672435, -0.12863834300001642], [-5.447982365148347, -2.699788781746175], [0.5520176348516532, -2.6997887817461743], [1.9662311972247482, -1.285575219373079])

turtle.register_shape('leafish_m', leaf_shape_m)

leaf_shape_l = ([3.5355339059327378, -3.5355339059327378], [18.53553390593274, -3.5355339059327378], [14.705311690337851, -0.3215958575000397], [33.988939980934035, 22.659737436069303], [10.49662446128632, 14.109233852927584], [10.49662446128632, 34.10923385292759], [6.961090555353581, 30.57369994699485], [4.372900104328372, 40.23295820988553], [1.7847096533031666, 30.573699946994846], [-1.7508242526295725, 34.10923385292758], [-1.750824252629567, 14.10923385292758], [-25.24313977227728, 22.659737436069292], [-5.959511481681091, -0.3215958575000428], [-13.61995591287087, -6.74947195436544], [1.3800440871291304, -6.749471954365437], [4.915577993061868, -3.2139380484326985])

turtle.register_shape('leafish_l', leaf_shape_l)




wn.exitonclick()