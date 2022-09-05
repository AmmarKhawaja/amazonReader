import datareader as dr
import amazonplug as ap
def run(SKU, DAYS, PROCESSTIME, MINORDER):
    totalSales = dr.getNumberOfSales(ap.generateOrdersReportFromNow(DAYS, 'report.txt'), SKU)
    avg_sales = totalSales/DAYS
    for i in ap.retrieveInventory():
        if i[0] == SKU:
            current_inventory = float(i[5])
    expected_stock = current_inventory / avg_sales
    print(totalSales)
    print(avg_sales)
    print(expected_stock)
    if expected_stock < PROCESSTIME:
        restock_amount = avg_sales * DAYS - current_inventory
        if(restock_amount < avg_sales * PROCESSTIME):
            restock_amount = avg_sales * PROCESSTIME - current_inventory
        if(restock_amount < MINORDER):
            restock_amount = MINORDER
        return restock_amount
    else:
        return 0

#Gets average number of items sold per day
#Recommends restock date