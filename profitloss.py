from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports/profit-and-loss-usd.csv"
file_path = Path.cwd()/"summary_report.txt"

def profitloss():
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        netprofit = []
        x = 0 
        for data in reader:
            netprofit.append([int(data[0]),int(data[4])])
        for i in range(10):
            if netprofit[i][1] > netprofit[i+1][1]:
                x += 1 
                deficit = netprofit[i][1] - netprofit[i+1][1]
                with file_path.open(mode='a') as file:
                    file.write(f"\n[PROFIT DEFICIT] DAY: {netprofit[i+1][0]}, AMOUNT: USD{deficit}")
        if x == 0:
            with file_path.open(mode='a') as file:
                file.write("\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")