from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports/cash-on-hand-usd.csv"
file_path = Path.cwd()/"summary_report.txt"

def cashonhand():
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        cash = []
        x = 0 
        for data in reader:
            cash.append([int(data[0]),int(data[1])])
        for i in range(10):
            if cash[i][1] > cash[i+1][1]:
                x += 1
                deficit = cash[i][1] - cash[i+1][1]
                with file_path.open(mode='a') as file:
                    file.write(f"\n[CASH DEFICIT] DAY: {cash[i+1][0]}, AMOUNT: USD{deficit}")
                #print(f"\n[CASH DEFICIT] Day: {cash[i+1][0]} Amount: USD{deficit}")
        if x == 0:
            with file_path.open(mode='a') as file:
                file.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY ")