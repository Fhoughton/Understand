import json
import operator

with open('underlords_heroes.json', 'r') as data_file:
    data = json.load(data_file)

def average(mylist):
    return sum(mylist) / len(mylist)

def sanitizeData(data):
    popme = []
        
    #Add all units with no gold cost or a gold cost of 0 to pop list since these are summons or loot round enemies
    for key, value in data.items():
        try:
            if value['goldCost'] == 0:
                popme.append(key)
        except KeyError:
            popme.append(key)
            pass
        
    #Actually pop them from dict
    for i in popme:
        data.pop(i)
    
   
def getSortedKeyValues(x):
    mydict = {}
    try:
        for primkey, value in data.items():
            for key in sorted(value.keys()):
                if key == x:
                    if value[key] != '':
                        mydict[primkey] = value[key]
        return sorted(mydict.items(),key=operator.itemgetter(1))
    except:
        return mydict
    
def getDps():
    dps = {}

    for key, value in data.items():
        if key == "slark":
            x = 0.8
        else:
            x = getSortedKeyValues("attackRate")[key]
            
        dmgmin = dict(getSortedKeyValues("damageMin"))[key]
        dmgmax = dict(getSortedKeyValues("damageMax"))[key]
            
        y = ((average(dmgmin)+average(dmgmax))/2)
        dps[key] = round(x*y)
        
    return dps

def getDpsList():
    dps = {}

    for key, value in data.items():
        if key == "slark":
            x = 0.8
        else:
            x = getSortedKeyValues("attackRate")[key]
            
        dmgmin = dict(getSortedKeyValues("damageMin"))[key]
        dmgmax = dict(getSortedKeyValues("damageMax"))[key]

        z=[]
        
        z.append(round(((dmgmin[0]+dmgmax[0])/2) * x))
        z.append(round(((dmgmin[1]+dmgmax[1])/2) * x))
        z.append(round(((dmgmin[2]+dmgmax[2])/2) * x))
        dps[key] = z
        
    return dps

def listTierDps():
    dps = getDpsList() 
    goldCost = getSortedKeyValues("goldCost")
    
    for key, value in goldCost:
        print(value,":",key,":",dps[key])
    
#VALID VALUES TO CALL
"""
'abilities'
'armor'
'attackAnimationPoint'
'attackRange'
'attackRate'
'damageMin'
'damageMax'
'displayName'
'dota_unit_name'
'draftTier'
'goldCost'
'health'
'id'
'keywords'
'magicResist'
'maxmana'
'model'
'model_scale'
'texturename'
'soundSet'
'movespeed'
'healthBarOffset'
'key'
"""
    
#CLEAN DATA
sanitizeData(data)

#PRINT WELCOME MESSAGE
print("Welcome to Understand, a tool to analyze the units of the game Dota Underlords.")

#REPL
while True:
    x = input("Enter a stat to check or type 'h' for help or 'q' to quit: ")
    if x == "h":
        for key, value in data.items():
            for k, v in value.items():
                print(k)
                if k == "dota_unit_name":
                    print("dps")
            break
    elif x == "q":
        exit(0)
    elif x == "dps":
        for key, value in getDpsList():
            print(key,value)
    else:
        for key, value in getSortedKeyValues(x):
            print(key,value)