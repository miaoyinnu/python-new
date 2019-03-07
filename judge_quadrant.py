
x = int(input("inpur x"))

y = int(input("input y"))

if x>0:
    if y > 0:
        print("第一象限")
    elif y == 0:
        print("x轴正半轴")
    elif y < 0:
        print("第二象限")
elif x == 0:
    if y > 0:
        print("y轴正半轴")
    elif y==0:
        print("原点")
    elif y < 0:
        print("y轴负半轴")
else:
    if y>0:
        print("第二象限")
    elif y == 0:
        print("x轴负半轴")
    elif y < 0:
        print("第四象限")

