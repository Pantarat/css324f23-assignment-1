def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s == (4,4,0)

def successors(s):
    x, y, z = s
    
    #pour 8l to 5l
    if x>0 and y<5:
        #pour all
        if y+x <= 5:
            yield ((0,y+x,z),1)
        #5l is full
        else:
            yield (((x-(5-y)),5,z),1)
            
    #pour 8l to 3l
    if x>0 and z<3:
        #pour all
        if z+x <= 3:
            yield ((0,y,z+x),1)
        #3l is full
        else:
            yield (((x-(3-z)),y,3),1)
            
    #pour 5l to 8l
    if y>0 and x<8:
        #pour all
        if x+y <= 8:
            yield ((x+y,0,z),1)
        #8l is full
        else:
            yield ((8,(y-(8-x)),z),1)
            
    #pour 5l to 3l
    if y>0 and z<3:
        #pour all
        if z+y <= 3:
            yield ((x,0,z+y),1)
        #3l is full
        else:
            yield ((x,(y-(3-z)),3),1)
            
    #pour 3l to 8l
    if z>0 and x<8:
        #pour all
        if x+z <= 8:
            yield ((x+z,y,0),1)
        #8l is full
        else:
            yield ((8,y,(z-(8-x))),1)
            
    #pour 3l to 5l
    if z>0 and y<5:
        #pour all
        if y+z <= 5:
            yield ((x,y+z,0),1)
        #5l is full
        else:
            yield ((x,5,(z-(5-y))),1)
    
    return []
