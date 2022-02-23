import csv 
import itertools

filename = "heart_failure_clinical_records_dataset.csv"
   
colNum = 0
scans = 1
min_sup = 60
lengh = 0
fields = []
rows = []
items = []
finalMatches = dict()

def aprioriStart(items):
    itemL = dict()
    itemL["age"] = 0
    itemL["ane"] = 0
    itemL["cre"] = 0
    itemL["dia"] = 0
    itemL["eje"] = 0
    itemL["hig"] = 0
    itemL["pla"] = 0
    itemL["seC"] = 0
    itemL["seS"] = 0
    itemL["mal"] = 0 #
    itemL["fem"] = 0 #
    itemL["smo"] = 0
    itemL["tme"] = 0
    itemL["dth"] = 0

    for item in items:
        if int(item) == 1:
            itemL["age"] += 1
        elif int(item) == 2:
            itemL["ane"] += 1
        elif int(item) == 3:
            itemL["cre"] += 1
        elif int(item) == 4:
            itemL["dia"] += 1
        elif int(item) == 5:
            itemL["eje"] += 1
        elif int(item) == 6:
            itemL["hig"] += 1
        elif int(item) == 7:
            itemL["pla"] += 1
        elif int(item) == 8:
            itemL["seC"] += 1
        elif int(item) == 9:
            itemL["seS"] += 1
        elif int(item) == 10:
            itemL["mal"] += 1#
        elif int(item) == 14:#
            itemL["fem"] += 1#
        elif int(item) == 11:
            itemL["smo"] += 1
        elif int(item) == 12:
            itemL["tme"] += 1
        elif int(item) == 13:
            itemL["dth"] += 1
    
    for item in itemL:
        if itemL[item] > min_sup:
            finalMatches[item] = itemL[item]
    print("age: %s" %itemL["age"])
    print("anaemia: %s" %itemL["ane"])
    print("creatinine phosphokinase: %s" %itemL["cre"])
    print("diabetes: %s" %itemL["dia"])
    print("ejection fraction: %s" %itemL["eje"])
    print("high blood pressure: %s" %itemL["hig"])
    print("platelets: %s" %itemL["pla"])
    print("serum creatinine: %s" %itemL["seC"])
    print("serum sodium: %s" %itemL["seS"])
    print("male: %s" %itemL["mal"]) #
    print("female: %s" %itemL["fem"]) #
    print("smoking: %s" %itemL["smo"])
    #print("Time: %s" %item["tme"])
    print("Deaths: %s" %itemL["dth"])
    apriori(itemL)

def apriori(itemL):
    i = 0
    itemN = dict()
    for item1 in list(itemL):
        i += 1
        match = 0
        rest = dict(itertools.islice(itemL.items(), i, len(itemL)))
        for item2 in rest:
            if itemL[item1] >= min_sup and (itemL[item2] >= min_sup or item2 == "death"):
                print("Items: %s %s" %(item1, item2))
                newMatch = "%s, %s" %(item1, item2)
                itemN[newMatch] = 0
                match += 1
        if match == 0:
            itemL.pop(item1)
            i -= 1
    print("Creating matches:")
    print(itemN)
    aprioriCon(itemN)

def apriori2(itemL):
    i = 0
    itemN = dict()
    for item1 in list(itemL):
        pair1 = item1.split(", ")
        i += 1
        match = 0
        rest = dict(itertools.islice(itemL.items(), i, len(itemL)))
        for item2 in rest:
            newMatch = ""
            pair2 = item2.split(", ")
            connection = 0
            for pairItem in pair1:
                k = 0
                if pairItem != pair2[0]:
                    continue
                for pairItem2 in pair2:
                    if pairItem == pairItem2:
                        pair2.pop(k)
                        connection += 1 
                    k += 1
            if connection < 1:
                continue
            if itemL[item1] >= min_sup and itemL[item2] >= min_sup and connection == (len(pair1)-1) and len(pair2) > 0:
                for itms in pair1:
                    newMatch += itms + ", "
                for itms in pair2:
                    newMatch += itms + ", "
                cut = len(newMatch)
                newMatch = newMatch[:cut - 2]
                itemN[newMatch] = 0
                match += 1
    print("Creating matches:")
    print(itemN)
    print('\n')
    if len(itemN) > 0:
        aprioriCon(itemN)
    else:
        print("All Matches:")
        print(finalMatches)
        print("Confidence that given other variables, death will occur:")
        for item in finalMatches:
            pair = item.split(", ")
            if pair[(len(pair)-1)] == "dth" and len(pair) > 1:
                pair.pop(len(pair)-1)
                coef = ""
                for itms in pair:
                    coef += itms + ", "
                cut = len(coef)
                coef = coef[:cut - 2]
                confidence = finalMatches[item]/finalMatches[coef]
                print("Given %s, probabilty of death is: %s" %(coef, confidence))

def aprioriCon(itemN):
    itemP = dict()
    itemL = dict()
    itemL["age"] = 0
    itemL["ane"] = 0
    itemL["cre"] = 0
    itemL["dia"] = 0
    itemL["eje"] = 0
    itemL["hig"] = 0
    itemL["pla"] = 0
    itemL["seC"] = 0
    itemL["seS"] = 0
    itemL["mal"] = 0 #
    itemL["fem"] = 0 #
    itemL["smo"] = 0
    itemL["tme"] = 0
    itemL["dth"] = 0
    for pairItem in itemN:
        pair = pairItem.split(", ")
        #print(pair)
        #print('\n')
        matches = 0
        alreadyM = 0
        for item in items:
            if item == -1:
                itemL["age"] = 0
                itemL["ane"] = 0
                itemL["cre"] = 0
                itemL["dia"] = 0
                itemL["eje"] = 0
                itemL["hig"] = 0
                itemL["pla"] = 0
                itemL["seC"] = 0
                itemL["seS"] = 0
                itemL["mal"] = 0 #
                itemL["fem"] = 0 #
                itemL["smo"] = 0
                itemL["tme"] = 0
                itemL["dth"] = 0
                alreadyM = 0
            elif int(item) == 1:
                itemL["age"] = 1
            elif int(item) == 2:
                itemL["ane"] = 1
            elif int(item) == 3:
                itemL["cre"] = 1
            elif int(item) == 4:
                itemL["dia"] = 1
            elif int(item) == 5:
                itemL["eje"] = 1
            elif int(item) == 6:
                itemL["hig"] = 1
            elif int(item) == 7:
                itemL["pla"] = 1
            elif int(item) == 8:
                itemL["seC"] = 1
            elif int(item) == 9:
                itemL["seS"] = 1
            elif int(item) == 10:
                itemL["mal"] = 1
            elif int(item) == 11:
                itemL["smo"] = 1
            elif int(item) == 12:
                itemL["tme"] = 1
            elif int(item) == 13:
                itemL["dth"] = 1
            elif int(item) == 14:
                itemL["fem"] = 1
            match = len(pair)
            for pairI in pair:
                #print(pairI)
                if itemL[pairI] == 1:
                    match -= 1
            if match == 0 and alreadyM == 0:
                alreadyM = 1
                matches += 1
        if matches >= min_sup:
            itemP[pairItem] = matches
            finalMatches[pairItem] = itemP[pairItem]
    print("checking total matches:")
    print(itemP)
    print('\n')
    apriori2(itemP)



with open(filename, 'r') as csvfile:  
    csvreader = csv.reader(csvfile) 

    fields = next(csvreader) 
 
    for row in csvreader: 
        rows.append(row)  
print("Enter Min_Sup")
min_sup = int(input())
#------------------------------------CHANGE STUFF HERE FOR OUTLIERS---------------------------------------------
for row in rows:  
    colNum = 0
    for col in row:	
        colNum += 1
        if colNum == 1:
            if float(col) >= 65:
                print("age: %s" %col)
                items.append(1)
        elif colNum == 2:
            if int(col) == 1:
                print("anaemia: %s" %col)
                items.append(2)
        elif colNum == 3:
            if float(col) >= 450:
                print("creatinine phosphokinase: %s" %col)
                items.append(3)
        elif colNum == 4:
            if int(col) == 1:
                print("diabetes: %s" %col)
                items.append(4)
        elif colNum == 5:
            if float(col) > 90 or float(col) < 33:
                print("ejection fraction: %s" %col)
                items.append(5)
        elif colNum == 6:
            if int(col) == 1:
                print("high blood pressure: %s" %col)
                items.append(6)
        elif colNum == 7:
            if float(col) > 600000 or float(col) < 100000:
                print("platelets: %s" %col)
                items.append(7)
        elif colNum == 8:
            if float(col) > 1.71 or float(col) < .44:
                print("serum creatinine: %s" %col)
                items.append(8)
        elif colNum == 9:
            if float(col) > 160 or float(col) < 120:
                print("serum sodium: %s" %col)
                items.append(9)
        elif colNum == 10:
            if int(col) == 1:
                print("sex: %s" %col)
                items.append(10)
            else:
                items.append(14)
        elif colNum == 11:
            if int(col) == 1:
                print("smoking: %s" %col)
                items.append(11)
        #elif colNum == 12:
            #if int(col) >= 60:
                #print("time: %s" %col)
                #items.append(12)
        elif colNum == 13:
            if int(col) == 1:
                print("DEATH EVENT: %s" %col)
                items.append(13)
            #print("column: %g" %colNum)
        #print(col),
    items.append(-1)
    print('\n') 
aprioriStart(items)