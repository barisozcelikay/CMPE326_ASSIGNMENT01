import area;

def logo_(logo_name , directions):
    def addlogo(list):
        contain = False;
        length = len(list) if len(list)>0 else 1;

        for i in range(length):
            if(len(list) == 0): # first element
                list.append({
                    "logo_name": logo_name,
                    "directions": directions,
                    "starting_coordinates": ["",""]
                });
                print(list[0]["logo_name"],"defined");
                contain = True;


            elif logo_name in list[i]["logo_name"]: #
                contain = True;
                print(logo_name,"is already defined");
                break;

        if(contain == False):
            list.append({
                "logo_name": logo_name,
                "directions": directions,
                "starting_coordinates": ["",""]
            });
            print(list[i + 1]["logo_name"], "defined");

    return addlogo;

def engrave_(list_of_logos,logo_name,x,y):
        temp = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]];
        vertical = "|";
        horizontal = "_";


        contain = False;
        length = len(list_of_logos) if len(list_of_logos) > 0 else 1;

        for i in range(length):
            if len(list_of_logos) == 0 :
                print("You did not enter any LOGO");


            elif logo_name == list_of_logos[i]["logo_name"] :
                #print("this is engrave",logo_name,"exist.");
                    contain = True;
                    def update(area):
                        temp = area;

                        list_of_logos[i]["starting_coordinates"][0] = x;
                        list_of_logos[i]["starting_coordinates"][1] = y;
                        coordinates = [x,y];
                        direction_list = list(list_of_logos[i]["directions"]);



                        current_location = (coordinates);  # current_location[0] => x , [1] => y
                        #print("İlk durum",current_location);
                        current_location[0] = int(int(current_location[0]) - 1) * 2 ; # indexes starts with 0  0 so it suited for 1 1
                        current_location[1] = int(int(current_location[1]) - 1) * 2 ;
                        #print("İlk durum", current_location);
                        #temp[current_location[0]][current_location[1]] = "#"; # showing starting coordinate
                        # normal konumlari cikan degerlerin yarisi
                        for j in range(len(direction_list)):
                        # LİSTEDE YUKARI ÇIKMAK İNDEX ARTMASI VE GÖSTERGEDE AŞAĞI İNMESİ DEMEK O YÜZDEN D İLE F NİN YERİ FARKLI DİKKAT ET BUNA !!!!!!!!!!
                            if(direction_list[j] == "D"):
                                temp[current_location[0] + 1][current_location[1]] = vertical;
                                #print("vertical ekledim", current_location[0] + 1,",",current_location[1]);

                                current_location[0] = ((int(current_location[0]) + 2));
                                #print("Asagiya indim");


                            elif(direction_list[j] == "U"):
                                temp[current_location[0] - 1][current_location[1]] = vertical;
                                #print("vertical ekledim", current_location[0] - 1,",",current_location[1]);

                                current_location[0] = (int(current_location[0]) - 2);
                                #print("Yukariya Ciktim");

                            elif(direction_list[j] == "R"):
                                temp[current_location[0]][current_location[1] + 1] = horizontal;
                               # print("horizontal ekledim",current_location[0],",",current_location[1] + 1);
                                current_location[1] = (int(current_location[1]) + 2);
                                #print("Saga Gittim");

                            elif(direction_list[j] == "L"):
                                temp[current_location[0]][current_location[1] - 1] = horizontal;
                                #print("horizontal ekledim", current_location[0],",",current_location[1] - 1);
                                current_location[1] = ((int(current_location[1]) - 2));
                                #print("Sola Gittim");

                        for n in range(21):
                            for c in range(21):
                                print(list_of_area[n][c], end="");
                            print();

                        return temp;


        def notupdate(area):
            return list_of_logos;

        if(contain == True):
            return update;
        else :
            print(logo_name,"is not defined. ")
            return notupdate;

def same_(list_of_logos,logo1,logo2):
    length = len(list_of_logos) if len(list_of_logos) > 0 else 1;
    contain = 0;
    comparedLogos = [];
    if(logo1==logo2):
        print("Yes");
    else:
        for i in range(length):

            if(len(list_of_logos) == 0):
                print("You did not enter any LOGO");
                return None;
            else:
                if (logo1 in list_of_logos[i]["logo_name"] or logo2 in list_of_logos[i]["logo_name"]):
                    comparedLogos.append(list_of_logos[i]);
                    contain += 1



        if(contain == 2):
            if(logo1 == logo2):
                print("OYEEEE")
            direction_of_logo1 = list(comparedLogos[0]["directions"]);
            direction_of_logo2 = list(comparedLogos[1]["directions"]);
            edge_list = [];

        # We have to minimize direction amount
            x = 0;
            y = 0;
            #print("logo 1 in 0 0 dan sonraki hareketleri",direction_of_logo1);
            for j in range(len(direction_of_logo1)):

                if(direction_of_logo1[j] == "D"):
                    flag = False;
                    for k in range(len(edge_list)):
                        if (([x, y] == edge_list[k]["ending_points"] and [x, y - 1] == edge_list[k]["starting_points"] or [x, y] == edge_list[k]["starting_points"] and [x, y - 1] == edge_list[k]["ending_points"])):
                            #print("this edge is exist")
                            flag = True;
                            y = y - 1;
                    if(flag == False):
                        edge_list.append({
                            "edge_number": len(edge_list) + 1,
                            "starting_points":[x,y],
                            "ending_points":[x,y-1],
                            "move":"D",
                            "v/h":"V"
                        })
                        y = y -1 ;
                    #print("D")

                elif(direction_of_logo1[j] == "U"):
                    flag = False;
                    for k in range(len(edge_list)):

                        if(([x,y] == edge_list[k]["ending_points"] and [x,y+1] == edge_list[k]["starting_points"]) or ([x,y] == edge_list[k]["starting_points"] and [x,y+1] == edge_list[k]["ending_points"])):
                            #print("this edge is exist")
                            flag = True;
                            y = y + 1;

                    if(flag == False):
                        edge_list.append({
                            "edge_number": len(edge_list) + 1,
                            "starting_points": [x,y],
                            "ending_points": [x,y+1],
                            "move": "U",
                            "v/h": "V"
                        })
                        y = y + 1;
                    #print("U")
                elif(direction_of_logo1[j] =="R"):
                    flag = False
                    for k in range(len(edge_list)):

                        if(([x,y] == edge_list[k]["ending_points"] and [x+1,y] == edge_list[k]["starting_points"]) or ([x,y] == edge_list[k]["starting_points"] and [x+1,y] == edge_list[k]["ending_points"])):
                            #print("this edge is exist")
                            flag = True;
                            x = x + 1;

                    if(flag == False):
                        edge_list.append({
                            "edge_number": len(edge_list) + 1,
                            "starting_points": [x,y],
                            "ending_points": [x+1,y],
                            "move": "R",
                            "v/h": "H"
                        })
                        x = x+1;
                    #print("R")
                elif(direction_of_logo1[j] == "L"):
                    flag = False;
                    for k in range(len(edge_list)):

                        if(([x,y] == edge_list[k]["ending_points"] and [x-1,y] == edge_list[k]["starting_points"]) or ([x,y] == edge_list[k]["starting_points"] and [x-1,y] == edge_list[k]["ending_points"])):
                            #print("this edge is exist")
                            flag = True;
                            x = x - 1;
                    if(flag == False):
                        edge_list.append({
                            "edge_number": len(edge_list) + 1,
                            "starting_points": [x,y],
                            "ending_points": [x-1,y],
                            "move": "L",
                            "v/h": "H"
                        })
                        x = x - 1 ;
                    #print("L")
            #print("Edge List 1")
            #print(edge_list);
            x = 0;
            y = 0;
            ######################################
            edge_list2 = []
            #print("logo 2 in 0 0 dan sonraki hareketleri", direction_of_logo2);
            for j in range(len(direction_of_logo2)):

                if (direction_of_logo2[j] == "D"):
                    flag = False;
                    for k in range(len(edge_list2)):
                        if (([x, y] == edge_list2[k]["ending_points"] and [x, y - 1] == edge_list2[k]["starting_points"] or [x, y] == edge_list2[k]["starting_points"] and [x, y - 1] == edge_list2[k]["ending_points"])):
                            #print("this edge is exist")
                            flag = True;
                            y = y - 1;

                    if (flag == False):
                        edge_list2.append({
                            "edge_number": len(edge_list2) + 1,
                            "starting_points": [x, y],
                            "ending_points": [x, y - 1],
                            "move": "D",
                            "v/h": "V"
                        })
                        y = y - 1;
                    #print("D")

                elif (direction_of_logo2[j] == "U"):
                    flag = False;
                    for k in range(len(edge_list2)):

                        if (([x, y] == edge_list2[k]["ending_points"] and [x, y + 1] == edge_list2[k]["starting_points"]) or ([x, y] == edge_list2[k]["starting_points"] and [x, y + 1] == edge_list2[k]["ending_points"])):
                            #print("this edge is exist")
                            flag = True;
                            y = y + 1;

                    if (flag == False):
                        edge_list2.append({
                            "edge_number": len(edge_list2) + 1,
                            "starting_points": [x, y],
                            "ending_points": [x, y + 1],
                            "move": "U",
                            "v/h": "V"
                        })
                        y = y + 1;
                    #print("U")
                elif (direction_of_logo2[j] == "R"):
                    flag = False
                    for k in range(len(edge_list2)):

                        if (([x, y] == edge_list2[k]["ending_points"] and [x + 1, y] == edge_list2[k]["starting_points"]) or ([x, y] == edge_list2[k]["starting_points"] and [x + 1, y] == edge_list2[k]["ending_points"])):
                            #print("this edge is exist")
                            flag = True;
                            x = x + 1;

                    if (flag == False):
                        edge_list2.append({
                            "edge_number": len(edge_list2) + 1,
                            "starting_points": [x, y],
                            "ending_points": [x + 1, y],
                            "move": "R",
                            "v/h": "H"
                        })
                        x = x + 1;
                    #print("R")
                elif (direction_of_logo2[j] == "L"):
                    flag = False;
                    for k in range(len(edge_list2)):

                        if (([x, y] == edge_list2[k]["ending_points"] and [x - 1, y] == edge_list2[k]["starting_points"]) or ([x, y] == edge_list2[k]["starting_points"] and [x - 1, y] == edge_list2[k]["ending_points"])):
                            #print("this edge is exist")
                            flag = True;
                            x = x - 1;
                    if (flag == False):
                        edge_list2.append({
                            "edge_number": len(edge_list2) + 1,
                            "starting_points": [x, y],
                            "ending_points": [x - 1, y],
                            "move": "L",
                            "v/h": "H"
                        })

                        x = x - 1;
                    #print("L")
            #print("Edge List 2")
            #print(edge_list2);

            #print(edge_list);

            #print(edge_list2);

            if(len(edge_list) == len(edge_list2)):
                point_list1 = []
                point_list2 = []
                match = 0;
                same = False;
                for x in range(len(edge_list)):
                    if(edge_list[x]["ending_points"] not in point_list1):
                        point_list1.append(edge_list[x]["ending_points"]);



                    if(edge_list2[x]["ending_points"] not in point_list2):
                        point_list2.append(edge_list2[x]["ending_points"]);

                for h in range(4):
                    for t in range(len(point_list1)):
                        if(point_list1[t] in point_list2):
                            if(match == len(point_list1)):
                                same = True;
                            else:
                                match += 1;

                        else:

                            temp = point_list1[t][0];
                            point_list1[t][0] = point_list1[t][1]
                            point_list1[t][1] = temp * (-1);
                            # print("Boyle oldu", point_list1[t][0], point_list1[t][1]);
                            t = 0;
                    if(same ==True):
                        print("Yes");
                        break;

                if(same == False):
                    print("No");

            else:
                print("No");
        else:
            print("Some of logos are not defined");




list_of_logos = [];
while True :
    main_command = input("Enter a Command (q for exit) : ").split();
    list_of_area = area.areamanagment();

    try:
        if(main_command[0] == "LOGO"):

            if(len(main_command) != 3):
                print("You entered less or extra property for LOGO command");
            else:
                logo_name = main_command[1];
                directions = main_command[2];

                directions_check = False
                for v in directions:
                    if (v.upper() not in ["U", "D", "R", "L"]):
                        directions_check = True;

                if (directions_check == True):
                    print(directions,"includes wrong type of directions");

                else:
                    logo_list = logo_(logo_name, directions);
                    logo_list(list_of_logos);

        elif(main_command[0] == "ENGRAVE"):

            if (len(main_command) != 4):
                print("You entered less or extra property for ENGRAVE command");
            else:
                engraved_logo_name = main_command[1];
                x_coordinate = main_command[2];
                y_coordinate = main_command[3];
                update_area = engrave_(list_of_logos,engraved_logo_name,x_coordinate,y_coordinate);
                list_of_area = update_area(list_of_area);


        elif(main_command[0] =="SAME"):
            if (len(main_command) != 3):
                print("You entered less or extra property for SAME command");
            else:
                logo_name1 = main_command[1];
                logo_name2 = main_command[2];
                same_(list_of_logos,logo_name1,logo_name2);
        elif(main_command[0].lower() =="q"):
            break;
        else:
            print("Entered wrong command");


    except IndexError:
        continue;






#x, y , z = input("Command : ").split();











