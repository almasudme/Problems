keyword=dict()

with open("sample_data.txt","r") as file:
    for line in file:
        if "FAIL in line":
            temp1 = line.split()
            temp2 = temp1[5:]
            deck = temp1[1]
            if (len(temp2)>0):
                
                for item in temp2:
                    if item[1] != "=" and "=" in item:
                        temp3 =item.split("=")[0]
                        if temp3 not in keyword:
                            keyword[temp3]=[]
                            keyword[temp3].append(deck)
                        else:
                            keyword[temp3].append(deck)                        
                    else:
                        next
        else:
            next
            
for item in keyword:
    tests=",".join(keyword[item])
    print(f"{item}\t{len(keyword[item])}\t{tests} ")
