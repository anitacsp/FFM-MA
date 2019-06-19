## DATA CLEANING                            ##
## FORMATTING DATA TO USABLE FORMAT         ##
## @gaybirdy                                ##

import pandas as pd
import os.path
import math
import csv

xls = pd.ExcelFile(r'C:/Users/chias/source/repos/FFM-MA/Clustering/data.xlsx')
summary = pd.read_excel(xls, 'Summary', header=[0])
returns = pd.read_excel(xls,'returns')

print("Data read")
print("Iterating Data...")
all = []
USE = []
DMX = []
AZE = []
CNE = []
UST = []
USHY = []
AZC = []
OIL = []
GOLD = []
COPP = []

for row in summary.iterrows():
    details = row[1]
    num = row[0]
       
    month = details['Month']
    growth = details['Growth']
    inflation = details['Inflation']
    liquidity = details['Liquidity']
    riskApp = details['Risk Appetite']
    drivers = [ growth, inflation, liquidity, riskApp]
    if not math.isnan(riskApp):
        USe = details['US Equities']
        DMx = details['DM ex US Equities']
        AznE = details['Asian Equities']
        CnE = details['China Equities']
        USt = details['US Treasuries']
        UShy = details['US High yield']
        AznC = details['Asian Credits']
        oil = details['Oil']
        gold = details['Gold']
        copper = details['Copper']

        if not math.isnan(USe):
            all.append(drivers + [USe, '0'])
            USE.append(drivers + [USe])
        if not math.isnan(DMx):
            all.append(drivers + [DMx, '1'])
            DMX.append(drivers + [DMx])
        if not math.isnan(AznE):
            all.append(drivers + [AznE, '2'])
            AZE.append(drivers + [AznE])
        if not math.isnan(CnE):
            all.append(drivers + [CnE, '3'])
            CNE.append(drivers + [CnE])
        if not math.isnan(USt):
            all.append(drivers + [USt, '4'])
            UST.append(drivers + [USt])
        if not math.isnan(UShy):
            all.append(drivers + [UShy, '5'])
            USHY.append(drivers + [UShy])
        if not math.isnan(AznC):
            all.append(drivers + [AznC, '6'])
            AZC.append(drivers + [AznC])
        if not math.isnan(oil):
            all.append(drivers + [oil, '7'])
            OIL.append(drivers + [oil])
        if not math.isnan(gold):
            all.append(drivers + [gold, '8'])
            GOLD.append(drivers + [gold])
        if not math.isnan(copper):
            all.append(drivers + [copper, '9'])
            COPP.append(drivers + [copper])

print("Data cleaned, output to csv")           

headers = ['growth', 'inflation', 'liquidity', 'risk app', 'return', 'type']
with open('cleanAssets.csv','w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(all)
f.close()

headers = ['growth', 'inflation', 'liquidity', 'risk app', 'return']
with open('US equities.csv','w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(USE)
f.close()

with open('DM ex US.csv','w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(DMX)
f.close()

with open('Asian equities.csv','w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(AZE)
f.close()

with open('China equities.csv','w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(CNE)
f.close()

with open('US treasuries.csv','w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(UST)
f.close()

with open('US high Yield.csv','w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(USHY)
f.close()

with open('Asian Credit.csv','w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(AZC)
f.close()

with open('oil.csv','w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(OIL)
f.close()

with open('gold.csv','w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(GOLD)
f.close()

with open('copper.csv','w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(COPP)
f.close()

print("output to csv success")