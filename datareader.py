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
        elif (i.tag == 'ProductName'):
            dic[title][i.tag] = i.text
        elif(i.tag == 'PurchaseDate'):
            dic[title][i.tag] = i.text[0:10]
        elif (i.tag == 'Type'):
            type = i.text
        elif (i.tag == 'Amount'):
            dic[title][type] = i.text
    return dic

def getSalesByItemPrice(REPORT):
    dic = parseOrderMonetary(REPORT)
    sales = {}
    for i in dic:
        inst = dic[i]
        if 'ProductName' in inst and 'Principal' in inst:
            if inst['ProductName'] in sales:
                if inst['Principal'] in sales[inst['ProductName']]:
                    sales[inst['ProductName']][inst['Principal']] += 1
                else:
                    sales[inst['ProductName']][inst['Principal']] = 1
            else:
                sales[inst['ProductName']] = {}
    return sales

