#Reads data from amazonplug (CSV)
def parseOrderMonetary(FILE):
    title = ' '
    type = ' '
    dic = {}
    for i in FILE.iter():
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