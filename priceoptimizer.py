import datareader as dr
import amazonplug as ap
def run(DAYS_RAN, SKU, MINIMUM_PRICE, PHASE):
    #Run once per day
    report = ap.generateOrdersReportFromNow(DAYS_RAN, 'report.xml')
    profitChangeReport = dr.getProfitChangeByPrice(report, SKU, MINIMUM_PRICE)
    if DAYS_RAN <= 14:
        #If profit changes less than 1.0 for 7 days, cancel to highest
        #Increase price by 1.5%
        return 1;
    if DAYS_RAN == 9:
        print("9")

        #Get mean change in profit
    #Get report from now to now - days ran
    #PART 1: First 8 days, increase Price by 2.5%/2 day
    #If profit is upward sloping, skip PART 2
    #PART 2: Second 8 days, decrease Price by 2.5%/2 day

    #Look at 8 day average price change, and repeat
        #If 8 day profit is decreasing, Price = peak, terminate.