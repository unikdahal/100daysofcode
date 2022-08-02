import math

def paint_calc(h,w,coverage):
    numberofcan= math.ceil((h*w)/coverage)
    print(f"The number of can required is {numberofcan}")

test_h=int(input("Height of the wall:"))
test_w=int(input("Width of the wall:"))
coverage=5
paint_calc(test_h,test_w,coverage)
