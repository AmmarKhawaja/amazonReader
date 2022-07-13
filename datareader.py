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