import amazonplug

if __name__ == "__main__":
    a = amazonplug.xmlParse(amazonplug.generateOrdersReport(7, 'report.xml'))
    print(a)