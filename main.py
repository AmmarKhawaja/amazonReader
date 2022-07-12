import amazonplug as ap
import datareader as dr
if __name__ == "__main__":
    report = ap.generateOrdersReportFromNow(7, 'report.xml')
    list = dr.parseOrderMonetary(report)
    print(list)

