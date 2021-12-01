import csv
import json
data={}

def child1(lines):

    if lines[4]=="":
        return None

    elif lines[1] in data.values():
        with open("data.json",'a') as jdata:
            #print(data)
            if data["children"]==" ":
                " "
            else:
                json.dump(data,jdata,indent=4)
        return {
        "label": lines[4],
        "id": lines[5],
        "link": lines[6],
        "children": [child2(lines)]
        }

def child2(lines):
    if lines[7]=="":
        return None
    else:
        return {
        "label": lines[7],
        "id": lines[8],
        "link": lines[9],
        "children": [ ]
        }

def parent(lines):

    global data
    if lines[1] in data:
        data[lines[1][3]].append(child1(lines))
    else:
        data ={
        "label": lines[1],
        "id": lines[2],
        "link": lines[3],
        "children": [child1(lines)]
        }

with open("data.csv", 'r') as cf:
    c_read = csv.reader(cf)
    next(c_read)
    for lines in c_read:
        if lines[0] == "":
            continue
        elif lines[7]=="":
            continue
        else:
            parent(lines)
