import random
import matplotlib.pyplot as plt

"""
This function resturs true if the point lies inside the office space or else it returns false

x   : the x coordinate of the point 
y   : the y coordinate of the point
sog : 'side of grid' the original area
soo : 'side of office' the side of the square of the office, office that lies in the center
"""
def check_point(x,y,sog,soo):
    y_top = x_right = sog/2+soo/2
    y_bot = x_left = sog/2-soo/2
    if (x >= x_left and x<=x_right):
        if(y >= y_bot and y<= y_top):
            return True
        else:
            return False
    else:
        return False
    
"""
Function returns N random points st none of the point lies in the office space

N   : # points required
sog : side of grid
soo : side of office
"""   
def N_random_points(N,sog,soo):
    ans = []
    for i in range(0,N):
        tempx = random.uniform(0, sog)
        tempy = random.uniform(0, sog)
        while (check_point(tempx,tempy,sog,soo)):
            tempx = random.uniform(0, sog)
            tempy = random.uniform(0, sog)
        ans.append((tempx,tempy))
    return ans

"""
Just a scatter_plot plotting give the output of "N_random_points" as inout
"""
def scatter_plot(points_array):
    x = [i[0] for i in points_array]
    y = [i[1] for i in points_array]
    plt.plot(x, y, 'ro')
    plt.show()
