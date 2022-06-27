#Gets data from amazon and returns it in a program friendly method
from privateinfo import *
from sp_api.api import Orders
from sp_api.api import Reports
from sp_api.api import Feeds
from sp_api.base import SellingApiException
from sp_api.base.reportTypes import ReportType
from datetime import datetime, timedelta
import time
import xml.etree.ElementTree as Xet
import pandas as pd
import csv

def xmlParse(FILENAME):
    dic = {}
    xmlparse = Xet.parse(FILENAME)
    root = xmlparse.getroot()
    #child = root.getchildren()
    for i in root.iter():
        dic[i.tag] = []
    for i in root.iter():
        dic[i.tag].append(i.text)
    return dic

def printOrders():
    print(Orders(credentials=credentials).get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat()))

def generateOrdersReport(DAYS,FILENAME):
    res = Reports(credentials=credentials).create_report(
        reportType=ReportType.GET_XML_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL,
        dataStartTime=datetime.utcnow() - timedelta(days=DAYS))

    status = Reports(credentials=credentials).get_report(res.payload['reportId']).payload['processingStatus']
    print("Generating Report")
    while(status != 'DONE'):
        time.sleep(5)
        status = Reports(credentials=credentials).get_report(res.payload['reportId']).payload['processingStatus']
        print("...", end=" ")

    Reports(credentials=credentials).get_report_document(Reports(credentials=credentials).get_report(res.payload['reportId']).payload['reportDocumentId'], download=True, file=FILENAME)
    print("Generated")
    return FILENAME

def generateMerchantReport(DAYS,FILENAME):
    res = Reports(credentials=credentials).create_report(
        reportType=ReportType.GET_MERCHANT_LISTINGS_ALL_DATA,
        dataStartTime=datetime.utcnow() - timedelta(days=DAYS))

    status = Reports(credentials=credentials).get_report(res.payload['reportId']).payload['processingStatus']
    while (status != 'DONE'):
        time.sleep(5)
        status = Reports(credentials=credentials).get_report(res.payload['reportId']).payload['processingStatus']
        print("Generating Report")
    Reports(credentials=credentials).get_report_document(
        Reports(credentials=credentials).get_report(res.payload['reportId']).payload['reportDocumentId'], download=True,
        file=FILENAME)
