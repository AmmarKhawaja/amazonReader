#Gets data from amazon and returns it in a program friendly method
from privateinfo import *
from sp_api.api import Orders
from sp_api.api import Reports
from sp_api.api import ListingsItems
from sp_api.api import Products
from sp_api.api import Inventories
from sp_api.base.reportTypes import ReportType
from datetime import datetime, timedelta
import time

import xml.etree.ElementTree as Xet

def loadingReport(res):
    status = Reports(credentials=credentials).get_report(res.payload['reportId']).payload['processingStatus']
    # Generator Start
    print('Generating Report')
    while (status != 'DONE'):
        time.sleep(5)
        status = Reports(credentials=credentials).get_report(res.payload['reportId']).payload['processingStatus']
        print("...", end=" ")
    print('Generated')

def parse(FILENAME):
    xmlparse = Xet.parse(FILENAME)
    root = xmlparse.getroot()
    return root

def parsetxt(FILENAME):
    data = []
    with open(FILENAME) as f:
        contents = f.readlines()
    for i in range(len(contents)):
        data.append(contents[i].split())
    return data

def printOrders():
    print(Orders(credentials=credentials).get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat()))

def generateOrdersReportFromNow(DAYS,FILENAME):
    if(DAYS > 30):
        print("Days cannot exceed 30")
        return;
    res = Reports(credentials=credentials).create_report(
        reportType=ReportType.GET_XML_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL,
        dataStartTime=datetime.utcnow() - timedelta(days=DAYS)
    )
    loadingReport(res)
    Reports(credentials=credentials).get_report_document(Reports(credentials=credentials).get_report(res.payload['reportId']).payload['reportDocumentId'], download=True, file=FILENAME)
    return parse(FILENAME)

#Heavily rate limited, utilize getInventory when current data has already been retrieved.
def getInventoryReport():
    res = Reports(credentials=credentials).create_report(
        reportType=ReportType.GET_AFN_INVENTORY_DATA,
        dataStartTime=datetime.utcnow() - timedelta(days=7)
    )
    loadingReport(res)
    Reports(credentials=credentials).get_report_document(
        Reports(credentials=credentials).get_report(res.payload['reportId']).payload['reportDocumentId'], download=True,
        file='inventory.txt')
    return parsetxt('inventory.txt')

def getInventory():
    parsetxt('inventory.txt')

def getPrice():
    ListingsItems(credentials=credentials)
    return Products(credentials=credentials).get_product_pricing_for_skus(['CL1163'])
