import amazonplug
from privateinfo import *
from sp_api.api import Orders
from sp_api.api import Reports
from sp_api.api import Feeds
from sp_api.base import SellingApiException
from sp_api.base.reportTypes import ReportType
from datetime import datetime, timedelta


if __name__ == "__main__":

    amazonplug.generateMerchantReport(7)
