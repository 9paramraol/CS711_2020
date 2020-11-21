import random
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from numpy import random
import numpy as np


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
    
################################### after 12 Nov   
"""
To randomly assign points in the catergory of a,b,c (a+b+c=1)

points : list of tuple of points
a : ratio of agents that are working
b : ratio of agents not working and moving (will not be useful but kept for future purpose)
c : ratio of agents that are home quarentining 
"""

def random_permute(a,b,c,points):
    na = int(a*len(points))
    nb = int(b*len(points))
    nc = len(points) - na - nb
    arr = np.array(points)
    random.shuffle(arr)
    points = arr.tolist()
    ans = []
    for i in range(0,len(points)):
        if (na>0):
            ans.append(('a',points[i]))
            na -= 1
        elif (nb>0):
            ans.append(('b',points[i]))
            nb -= 1
        else:
            ans.append(('c',points[i]))
    return ans


""" 
Just a plotting function ,give the imput of the funcion just above to the given funciton
"""
def dist_scatter_plot(dist_points):
    xa = []; ya = []
    xb = []; yb = []
    xc = []; yc = []
    for point in dist_points:
        if (point[0]=='a'):
            xa.append(point[1][0])
            ya.append(point[1][1])
        elif (point[0]=='b'):
            xb.append(point[1][0])
            yb.append(point[1][1])
        elif (point[0]=='c'):
            xc.append(point[1][0])
            yc.append(point[1][1])
    plt.scatter(xa, ya, c='red', s=10)
    plt.scatter(xb, yb, c='blue', s=10)
    plt.scatter(xc, yc, c='green', s=10)
    plt.show()

"""
helper function of the function just below the given funciton
"""
def get_dist_points(dist_points):
    na = 0; nb = 0; nc = 0
    for point in dist_points:
        if (point[0]=='a'):
            na += 1
        elif (point[0]=='b'):
            nb += 1
        else:
            nc += 1
    return na,nb,nc

"""
assigns radom point in office that are of category 'a', a helper function for the function just below it
"""
def office_place_assignment(dist_points,a_points,origin):
    ans_list = []
    for i in range(0,len(a_points)):
        ans_list.append((dist_points[i][0],[a_points[i][0]+origin[0],a_points[i][1]+origin[1]]))
    for i in range(len(a_points),len(dist_points)):
        ans_list.append(dist_points[i])
    return ans_list


"""
The functions gives a dictionary as output of form (time stamp: [list of positions])

dist_points : 'random_permute' function's input
work_t : hours in a day an agent works
simu_days : #days a simulation works
sog : side of grid
soo : side of office
"""    
def simulation_dictionary(dist_points,work_t,simu_days,sog,soo):
    ans_dict = {}
    na,nb,nc = get_dist_points(dist_points)
    for hr in range(0,simu_days*24):
        time = hr%24
        print(time,end = ',')
        if(time>=9 and time<(9+work_t)):
            a_points = N_random_points(na,soo,0)
            origin = [(sog-soo)/2,(sog-soo)/2]
            curr_pos = office_place_assignment(dist_points,a_points,origin)
            ans_dict[hr] = curr_pos
        else:
            ans_dict[hr] = dist_points
    return ans_dict





"""
just get the x coordinate of simu_dict[time]
simu_dict : output of the above funciton
time : time-stamp
"""
def getXcoord(simu_dict,time):
    day_stat = simu_dict[time]
    x = []
    for point in day_stat:
        x.append(point[1][0])
    return x

"""
same as above function just get the y coordinate of simu_dict[time]
"""
def getYcoord(simu_dict,time):
    day_stat = simu_dict[time]
    y = []
    for point in day_stat:
        y.append(point[1][1])
    return y

### TESTING CODE

points = N_random_points(1000,1000,500)
dist_points = random_permute(0.3,0.0,0.7,points)
simu_dict = simulation_dictionary(dist_points,8,7,1000,500)



fig, ax = plt.subplots()
ax.set_xlim([0,1000])
ax.set_ylim([0,1000])

for i in np.arange(168):
    x=getXcoord(simu_dict,i)
    y=getYcoord(simu_dict,i)
    bha=ax.scatter(x,y)
    plt.draw()
    plt.pause(0.5)
    bha.remove()

plt.show()
