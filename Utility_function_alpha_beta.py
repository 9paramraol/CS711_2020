#delta = alpha*sum(log(salary_i)-leg(penalty_i)) + beta*sum(wfh)

def penalty_of_agents_at_t(simu_dict,ts,proximity_dist,mask_set,mask_f):
    cat_postns = simu_dict[ts]
    ans_list = []
    for i in range(0,len(cat_postns)):
        point = cat_postns[i]
        if (point[0]!='a'):
            ans_list.append(0)
            continue
        curr_penalty = 0
        x1 = point[1][0]; y1 = point[1][1]
        for npoint in cat_postns:
            if ((npoint==point) or npoint[0]=='c'):
                continue
            x2 = npoint[1][0]; y2 = npoint[1][1]
            curr_dist =  ((x1-x2)**2 + (y1-y2)**2)**(0.5)
            if(curr_dist>proximity_dist):
                continue
            else:
                 curr_penalty += (proximity_dist-curr_dist)
        if(i in mask_set):
            curr_penalty /= mask_f
        ans_list.append(curr_penalty)
    return ans_list

def penalty_dict_fn(simu_dict,proximity_dist,mask_set,mask_f,wt):
    penalty_dict = {}
    for ts in simu_dict:
        if((ts%24)>=9 and (ts%24)<(9+wt)):
            plist = penalty_of_agents_at_t(simu_dict,ts,proximity_dist,mask_set,mask_f)
            penalty_dict[ts] = plist
        else:
            penalty_dict[ts] = [0]*len(simu_dict[ts])
    return penalty_dict

def sum_penalty(penalty_dict):
    overall_penalty = [0]*1000
    for ts in penalty_dict:
        overall_penalty = [x+y for x,y in zip(penalty_dict[ts],overall_penalty)]
    return overall_penalty

def salarty_overall(per_hr_wage,wt):
    ans_list = [wt*6*wage for wage in per_hr_wage]
    return ans_list


# penalty_dict = penalty_dict_fn(simu_dict,10,{-1},20,8)
# over_all_penalty = sum_penalty(penalty_dict)