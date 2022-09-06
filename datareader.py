#Reads data from amazonplug (CSV)
def parseOrderMonetary(REPORT):
    title = ' '
    type = ' '
    dic = {}
    if REPORT is None:
        return -1;
    for i in REPORT.iter():
        if (i.tag == 'AmazonOrderID'):
            title = i.text
            dic[title] = {}
        elif (i.tag == 'SKU'):
            dic[title][i.tag] = i.text
        elif(i.tag == 'PurchaseDate'):
            dic[title][i.tag] = i.text[0:10]
        elif (i.tag == 'Type'):
            type = i.text
        elif (i.tag == 'Amount'):
            dic[title][type] = i.text
    return dic

def getNumberOfSales(REPORT, SKU):
    dic = parseOrderMonetary(REPORT)
    total = 0
    for i in dic:
        inst = dic[i]
        if 'SKU' in inst and 'Principal' in inst and inst['SKU'] == SKU:
            total += 1
    return total

def getSalesByItemPrice(REPORT):
    dic = parseOrderMonetary(REPORT)
    sales = {}
    for i in dic:
        inst = dic[i]
        if 'SKU' in inst and 'Principal' in inst:
            if inst['SKU'] in sales:
                if inst['Principal'] in sales[inst['SKU']]:
                    sales[inst['SKU']][inst['Principal']] += 1
                else:
                    sales[inst['SKU']][inst['Principal']] = 1
            else:
                sales[inst['SKU']] = {}
    return sales

def getProfitByItemPrice(REPORT, SKU, COST):
    dic = parseOrderMonetary(REPORT)
    sales = {}
    for i in dic:
        inst = dic[i]
        if 'SKU' in inst and 'Principal' in inst and inst['SKU'] == SKU:
            if inst['SKU'] in sales:
                if inst['Principal'] in sales[inst['SKU']]:
                    sales[inst['SKU']][inst['Principal']] += float(inst['Principal']) - COST
                else:
                    sales[inst['SKU']][inst['Principal']] = float(inst['Principal']) - COST
            else:
                sales[inst['SKU']] = {}
    return sales

def getProfitChangeByPrice(REPORT, SKU, COST):
    newReport = getProfitByItemPrice(REPORT, SKU, COST)
    profitChanges = {}
    pastProfit = 1
    for i in newReport['CL1163']:
        if profitChanges == {}:
            profitChanges[i] = 1
        else:
            profitChanges[i] = newReport['CL1163'][i] / pastProfit
        pastProfit = newReport['CL1163'][i]
    return profitChanges

def getSalesByDate(REPORT, SKU):
    dic = parseOrderMonetary(REPORT)
    sales = {}
    for i in dic:
        inst = dic[i]
        if inst['SKU'] == SKU:
            if inst['PurchaseDate'] in sales:
                sales[inst['PurchaseDate']] += 1
            else:
                sales[inst['PurchaseDate']] = 1
    return sales