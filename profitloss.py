#import path
from pathlib import Path
import csv
#create file path to current working directory
fp = Path.cwd()/"csv_reports/profit-and-loss-usd.csv"
file_path = Path.cwd()/"summary_report.txt"

def profitloss():
    '''create function to print whether profit and loss is higher than the previous day, and calculate deficit from previous day 
    if profit is not higher'''
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        #read profit and loss file
        reader = csv.reader(file)
        #skip header in the file
        next(reader)
        #create empty list 
        netprofit = []
        #create temporary variable 'x' for file to start reading from day 0
        x = 0 
        #create a for loop to append data from file to the empty list 'netprofit'
        for data in reader:
            #append data from file, [0] to refer to the first item in the sublist, which is the day, [4] refers to the sublist for net profit
            netprofit.append([int(data[0]),int(data[4])])
        #create a for loop to print the output accordingly, according to whether there was a profit or deficit, 'i' acts as a
        #temporary variable to refer to items inside the list
        for i in range(10):
            #if netprofit the previous day is higher than the net profit the next day, calculate deficit from previous day 
            #[1] referring to current day, [i+1] to add one more day to the current day, referring to the next day
            if netprofit[i][1] > netprofit[i+1][1]:
                #add 1 to variable 'x' whenever there is a cash deficit, 'x' acts as a variable to keep track of profit deficits
                x += 1 
                #create a variable 'deficit' to calculate the deficit by subtracting the next day's net profit from
                # the current day's net profit 
                deficit = netprofit[i][1] - netprofit[i+1][1]
                with file_path.open(mode='a') as file:
                    #print the output if there is a deficit in net profit compared to the previous day, with the amount in USD
                    file.write(f"\n[PROFIT DEFICIT] DAY: {netprofit[i+1][0]}, AMOUNT: USD{deficit}")
        #if there is no deficit, print statement that states that the net profit on each day is higher than the previous day
        if x == 0:
            with file_path.open(mode='a') as file:
                file.write("\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")