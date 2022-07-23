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
        elif (i.tag == 'Type'):
            type = i.text
        elif (i.tag == 'Amount'):
            dic[title][type] = i.text
    return dic

def getSalesByItem(REPORT):
    dic = parseOrderMonetary(REPORT)
    sales = {}
    print(dic)
    for i in dic:
        print(i)
        inst = dic[i]
        if 'ProductName' in inst and 'Principal' in inst:
            if inst['ProductName'] in sales:
                sales[inst['ProductName']]['Total Principal'] += float(inst['Principal'])
                sales[inst['ProductName']]['Total Sales'] += 1
                sales[inst['ProductName']]['Avg Price'] = sales[inst['ProductName']]['Total Principal'] / sales[inst['ProductName']]['Total Sales']
            else:
                sales[inst['ProductName']] = {'Total Principal': 0, 'Total Sales': 0, 'Avg Principal': 0}
    return sales

