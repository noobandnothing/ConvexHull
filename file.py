from collections import deque
from collections import namedtuple  
import matplotlib.pyplot as plt  
import math
import sys
Point = namedtuple('Point', 'x y')



class my_Convex_Hull_Algorithm:
    __min = None
    __num = None
    __points = []
    __ref = None
    
    def __init__(self,num):
        self.__num = num
        self.__addpoints()
        self.__getSmalestY_Point()
        self.__sortPointList()
        self.__Convex_calc()
    
    def __is_point_in_list(self,point):
        for p in self.__points:
            if p.x == point.x and p.y == point.y:
                return True
        return False

    def __addpoints(self):
        for i in range(0,self.__num):
            x = float(input(f"x  for point {i+1}: "))
            y = float(input(f"y for point {i+1}: "))
            print('#####################################')
            if not self.__is_point_in_list(Point(x=x, y=y)):
                self.__points.append(Point(x=x, y=y))
            else:
                print('INVALID INPUT : POINT EXIST')
                sys.exit()
            

    def __getSmalestY_Point(self):
        min = self.__points[0]
        for counter in range(1,len(self.__points)): 
            if min.y > self.__points[counter].y:
                min = self.__points[counter]
            elif min.y == self.__points[counter]:
                if min.x > self.__points[counter].x :
                    min = self.__points[counter]
        self.__ref = min
    
    def __calculate_angle(self,point):
        if self.__ref is None:
            sys.exit()
        x, y = point
        ref_x, ref_y = self.__ref
        angle = math.atan2(y - ref_y, x - ref_x)
        distance = math.sqrt((x - ref_x)**2 + (y - ref_y)**2)
        return angle ,distance


    
    def __sortPointList(self):
        print('#####################################')
        print('POINTS : ',self.__points)
        self.__points = sorted(self.__points, key=self.__calculate_angle)
        print('#####################################')
        print('SORTED POINTS: ',self.__points)
        print('#####################################')
        
    def __is_ccw (self, p1,  p2,  p3):
        area = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
		# clockwise
        if area < 0 : return -1 
        # counter-clockwise
        if area > 0 : return 1
        # collinear
        return 0
    
    def __plot(self,stack):
        x = [p.x for p in self.__points]
        y = [p.y for p in self.__points]
        plt.plot(x, y, marker='D', linestyle='None')
        # 
        hx = [p.x for p in stack]
        hy = [p.y for p in stack]
        hx.append(hx[0])
        hy.append(hy[0])
        plt.plot(hx, hy)
        plt.title('Noob and Sabaa')
        plt.show()

    def __Convex_calc(self):
        stack = deque()
        stack.append(self.__points[0])
        stack.append(self.__points[1])
        for i in range(2,self.__num):
            next = self.__points[i]
            p = stack.pop()
            while  len(stack) != 0 and self.__is_ccw(stack[-1], p, next) <= 0:
                p =  stack.pop(); 
            stack.append(p);
            stack.append(self.__points[i]);  
        p = stack.pop();
        if self.__is_ccw(stack[-1], p, self.__ref) > 0 :
            stack.append(p);
        
        print("CONVEX HULL POINTS : ")
        if len(stack) >= 3 :
            print(stack)
            lolo = []
            for i in range(0,len(stack)):
                lolo.append(stack.pop())
            self.__plot(lolo)
        else:
            print("NO POINTS DUDE")


######################################
num=int(input("Enter number of points: "))
if num >= 3 and num is not None:
    aa = my_Convex_Hull_Algorithm(num)
else:
    sys.exit()
