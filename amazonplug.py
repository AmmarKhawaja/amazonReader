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

# Need to enable permissions in seller central.
# def generateOrdersReportDateRange(Byear, Bmonth, Bday, Eyear, Emonth, Eday, FILENAME):
#     res = Reports(credentials=credentials).create_report(
#         reportType=ReportType.GET_XML_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL,
#         dataStartTime=datetime(Byear, Bmonth, Bday).isoformat(),
#         dateEndTime=datetime(Eyear, Emonth, Eday).isoformat(),
#     )
#
#     loadingReport(res)
#     Reports(credentials=credentials).get_report_document(
#         Reports(credentials=credentials).get_report(res.payload['reportId']).payload['reportDocumentId'], download=True,
#         file=FILENAME)
#     return parse(FILENAME)