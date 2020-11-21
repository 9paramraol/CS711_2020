import random 
import math 
def di(simu_dict,player,num_times):
    val=0
    #0 
    for i in range(num_times):
        lst=simu_dict[i]
        playerx=lst[player][1][1]
        playery=lst[player][1][0]
        for x in lst:
            if abs(x[1][1]-playerx)<10 and abs(x[1][0]-playery)<10:
                val=val+math.sqrt((x[1][1]-playerx)**2+(x[1][0]-playery)**2)
    return val

def Zminus_deltai(simu_dict,player,num_times):
    val=0
    initialposx=simu_dict[0][player][1][0]
    initialposy=simu_dict[0][player][1][1]
    for i in range(num_times):
        x=simu_dict[i]
        if i==0:
            val+=(1400-math.sqrt((x[player][1][1]-initialposy)**2+(x[player][1][0]-initialposx)**2))
        else:
            y=simu_dict[i-1]
            val+=(1400-math.sqrt((x[player][1][1]-y[player][1][1])**2+(x[player][1][0]-y[player][1][1])**2))
    return val

def Deltai(simu_dict,player,num_times,alpha,beta,gamma,timeOfWorking):
    #salary function checking
    if simu_dict[0][player][0]=='a':
        salary=math.log(timeOfWorking*random.randint(10000,3000000000))
    else:
        salary=0
#     print(salary,di(simu_dict,player,num_times),deltai(simu_dict,player,num_times))
    val=salary+math.log(di(simu_dict,player,num_times)+1)+math.log(Zminus_deltai(simu_dict,player,num_times))
    return val

def fin(simu_dict,num_times,num_players):
    val=0
    for i in range(num_players):
        val+=Deltai(simu_dict,i,num_times,1,1,1,7)
    return val

simulaton1=fin(simu_dict,168,1000)
print(simulaton1)
