
def areamanagment():
    area = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]];
    dot = "."
    space = " ";
    for i in range(21):

            for j in range(11):
                if (i % 2 != 0):
                    area[i].append(space);
                    if(j != 10):
                        area[i].append(space);
                else:
                    area[i].append(dot); #coordinates
                    if(j != 10):
                        area[i].append(space); #odd indexes are direction places
            #print(area[i]);

    return area;


#areamanagment();