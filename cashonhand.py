from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports/cash-on-hand-usd.csv"
file_path = Path.cwd()/"summary_report.txt"

def cashonhand():
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        #create a csv reader object to read the contents of the file
        reader = csv.reader(file)
        #to skip first line of the reader
        next(reader)
        #create empty list to store data from csv file
        cash = []
        #x variable created to keep count of the number of deficits and x is made to be 0
        x = 0 
        #for loop created and looped over reader 
        for data in reader:
            #append data from nested list into the empty list 
            cash.append([int(data[0]),int(data[1])])
        #for loop created to loop over the first 10 elements in the cash list
        for i in range(10):
            #if statement is created to check if cash on hand is less than the previous day 
            if cash[i][1] > cash[i+1][1]:
                #x variable will be increased by 1 each time whenever there is a cash deficit
                x += 1
                # calculate the cash deficit using the previous day minus the current day
                deficit = cash[i][1] - cash[i+1][1]
                #file is opened to be appended
                with file_path.open(mode='a') as file:
                    #writing the cash deficits , day and amount.
                    file.write(f"\n[CASH DEFICIT] DAY: {cash[i+1][0]}, AMOUNT: USD{deficit}")
        #if statement created for when there is no cash deficits
        if x == 0:
            #file is opened to be appended
            with file_path.open(mode='a') as file:
                #cash surplus information is written
                file.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY ")